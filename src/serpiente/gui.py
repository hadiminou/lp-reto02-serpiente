import tkinter as tk
import random
from collections import deque
import utiles_serpiente
import utiles_paredes
import platform
if platform.system() == "Windows":
    import winsound
    from threading import Thread

FILAS = 30
COLUMNAS = 40
NUM_PAREDES = 6
MIN_TAM_PAREDES = 4
MAX_TAM_PAREDES = 8
SONIDO = True # El sonido sólo está implementado para Windows y puede fallar

class SerpienteGUI(tk.Canvas):
    def __init__(self, filas=FILAS, columnas=COLUMNAS, tam_bloque=20):
        self.filas = filas
        self.columnas = columnas
        self.tam_bloque = tam_bloque
        self.ancho = columnas * tam_bloque
        self.alto = filas * tam_bloque
        self.retraso_ms = 100   # A menor valor, mayor velocidad
        self.plataforma = platform.system()

        super().__init__(width=self.ancho, height=self.alto, background="white", highlightthickness=0)

        self.serpiente = [(5, 5), (4, 5), (3, 5)]              
        self.paredes = utiles_paredes.genera_paredes_aleatorias(self.serpiente, self.filas, self.columnas,num_paredes=NUM_PAREDES,tam_min=MIN_TAM_PAREDES,tam_max=MAX_TAM_PAREDES)
        self.comida = utiles_serpiente.genera_comida_aleatoria(self.serpiente, self.paredes, self.filas, self.columnas)
        self.puntuacion = 0
        self.direccion = "Right"
        self.ultima_direccion = self.direccion  
        self.cola_direcciones = deque()  # Lo usaremos para guardar pulsaciones más rápidas que el retardo

        self.bind_all("<Key>", self.al_pulsar_tecla)
        self.carga_imagenes()
        self.crea_objetos()

        if platform.system() == "Windows" and SONIDO:
            self.carga_sonidos()

        self.after(100, self.bucle_juego)

    def carga_sonidos(self):        
        with open("assets/comida.wav", "rb") as file:
            self.sonido_comida = file.read()
        with open("assets/paredes.wav", "rb") as file:
            self.sonido_paredes = file.read()
        with open("assets/crash.wav", "rb") as file:
            self.sonido_crash = file.read()


    def convierte_a_pixeles(self, posicion):
        return posicion[0] * self.tam_bloque + self.tam_bloque/2, posicion[1] * self.tam_bloque + self.tam_bloque/2

    def carga_imagenes(self):
        self.imagenes_serpiente = [
            tk.PhotoImage(file="assets/piel_serpiente1.png"), 
            tk.PhotoImage(file="assets/piel_serpiente2.png"), 
            tk.PhotoImage(file="assets/piel_serpiente3.png")]

        self.imagen_comida = tk.PhotoImage(file="assets/comida.png")
        self.imagen_pared = tk.PhotoImage(file="assets/pared.png")
        
    def crea_objetos(self):
        self.create_text(
            65, 12, text=f"Puntuación: {self.puntuacion}", tag="score", fill="black", font=10
        )

        
        for i, posicion in enumerate(self.serpiente):
            x, y = self.convierte_a_pixeles(posicion)
            self.create_image(x, y, image=self.imagenes_serpiente[i%len(self.imagenes_serpiente)], tag="snake")
        
        self.create_image(*self.convierte_a_pixeles(self.comida), image=self.imagen_comida, tag="food")

        self.crea_objetos_paredes()
    
    def crea_objetos_paredes(self):
        for pared in self.paredes:
            for posicion in pared:
                x, y = self.convierte_a_pixeles(posicion)
                self.create_image(x, y, image=self.imagen_pared, tag="wall")
                
        
    def mueve_serpiente(self):
        # Actualizar la dirección con la próxima en la cola, si es válida
        # Utilizamos una cola de próximos movimientos para evitar comportamientos
        # extraños si se producen varias pulsaciones más rápidas de lo que dura
        # cada pausa entre frames del juego
        while self.cola_direcciones:
            siguiente_direccion = self.cola_direcciones.popleft()
            if (self.ultima_direccion == "Left" and siguiente_direccion != "Right") or \
               (self.ultima_direccion == "Right" and siguiente_direccion != "Left") or \
               (self.ultima_direccion == "Up" and siguiente_direccion != "Down") or \
               (self.ultima_direccion == "Down" and siguiente_direccion != "Up"):
                self.direccion = siguiente_direccion
                break

        utiles_serpiente.mueve_serpiente(self.serpiente, self.direccion, self.filas, self.columnas)

        for segmento, posicion in zip(self.find_withtag("snake"), self.serpiente):
            self.coords(segmento, self.convierte_a_pixeles(posicion))
            
        # Actualiza la última dirección después de mover la serpiente
        self.ultima_direccion = self.direccion

    def bucle_juego(self):
        if utiles_serpiente.comprueba_choque(self.serpiente):
            self.game_over()
            return

        self.mueve_serpiente()

        if any(self.serpiente[0] in pared for pared in self.paredes):
            self.reproduce_sonido(self.sonido_crash)          
            self.game_over()
            return

        self.comprueba_serpiente_come_crece()
        self.after(self.retraso_ms, self.bucle_juego)

    def game_over(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game over! Puntuación: {self.puntuacion}",
            fill="black",
            font=('TkDefaultFont', 24)
        )

    def al_pulsar_tecla(self, e):
        if e.keysym in {"Left", "Right", "Up", "Down"}:
            self.cola_direcciones.append(e.keysym)


    def comprueba_serpiente_come_crece(self):
        if utiles_serpiente.come_serpiente(self.serpiente, self.comida):
            self.reproduce_sonido(self.sonido_comida)

            self.puntuacion += 1
            utiles_serpiente.crece_serpiente(self.serpiente)
            if self.retraso_ms > 50:
                self.retraso_ms -= 1 # Cuanto más come, más rápido se moverá

            # Cada ocho puntos, se generan nuevas paredes
            if self.puntuacion % 6 == 0:   
                self.reproduce_sonido(self.sonido_paredes)             
                self.paredes = utiles_paredes.genera_paredes_aleatorias(self.serpiente, self.filas, self.columnas,num_paredes=NUM_PAREDES,tam_min=MIN_TAM_PAREDES,tam_max=MAX_TAM_PAREDES)
                self.delete("wall")
                self.crea_objetos_paredes()


            self.create_image(*self.convierte_a_pixeles(self.serpiente[-1]), image=self.imagenes_serpiente[(len(self.serpiente)-1)%2], tag="snake")
            
            self.comida = utiles_serpiente.genera_comida_aleatoria(self.serpiente, self.paredes, self.filas, self.columnas)
            self.coords(self.find_withtag("food"), self.convierte_a_pixeles(self.comida))
            
            score = self.find_withtag("score")
            self.itemconfigure(score, text=f"Puntuación: {self.puntuacion}")

                
    def reproduce_sonido(self, sonido):    
        if self.plataforma == "Windows" and SONIDO:    
            self.thread = Thread(target=lambda :winsound.PlaySound(sonido, winsound.SND_MEMORY))
            self.thread.start() 

root = tk.Tk()
root.title("Juego Serpiente")

board = SerpienteGUI()
board.pack()

root.mainloop()
