from utiles_paredes import *

def test_genera_posicion_aleatoria_pared():
    print("genera_posicion_aleatoria_pared...", end="")

    filas = columnas = 5
    tamaño_pared = 3

    for _ in range(100): 
        x, y, orientacion = genera_posicion_aleatoria_pared(filas, columnas, tamaño_pared)

        # Verificar que las coordenadas están dentro de los límites del tablero
        assert 0 <= x < columnas and 0 <= y < filas, "Error: posición fuera de los límites del tablero."

        # Verificar que la pared cabe en el tablero
        if orientacion == "horizontal":
            assert x + tamaño_pared <= columnas, "Error: la pared horizontal se sale del tablero."
        else:
            assert y + tamaño_pared <= filas, "Error: la pared vertical se sale del tablero."

    print("OK")

def test_crea_pared():
    print("crea_pared...", end="")

    # Prueba para una pared horizontal
    x, y = 0, 0
    orientacion = "horizontal"
    tamaño_pared = 3
    pared_esperada_horizontal = [(0, 0), (1, 0), (2, 0)]
    pared_horizontal = crea_pared(x, y, orientacion, tamaño_pared)
    assert pared_horizontal == pared_esperada_horizontal, "Error: la pared horizontal no se creó correctamente."

    # Prueba para una pared vertical
    orientacion = "vertical"
    pared_esperada_vertical = [(0, 0), (0, 1), (0, 2)]
    pared_vertical = crea_pared(x, y, orientacion, tamaño_pared)
    assert pared_vertical == pared_esperada_vertical, "Error: la pared vertical no se creó correctamente."

    print("OK")

def test_hay_superposicion():
    print("hay_superposicion...", end="")

    # Caso de prueba donde no hay superposición
    pared = [(2, 2)]
    serpiente = [(0, 0), (1, 1)]
    paredes_existentes = [[(3, 3), (3, 4)]]
    assert not hay_superposicion(pared, serpiente, paredes_existentes), "Error: se indicó una superposición inexistente."

    # Caso de prueba donde hay superposición con la serpiente
    pared_con_serpiente = [(0, 0)]
    assert hay_superposicion(pared_con_serpiente, serpiente, paredes_existentes), "Error: no se detectó la superposición con la serpiente."

    # Caso de prueba donde hay superposición con una pared existente
    pared_con_pared_existente = [(3, 3)]
    assert hay_superposicion(pared_con_pared_existente, serpiente, paredes_existentes), "Error: no se detectó la superposición con una pared existente."

    print("OK")

def test_hay_distancia_suficiente():
    print("hay_distancia_suficiente...", end="")

    # Caso de prueba donde la distancia es suficiente
    cabeza_serpiente = (0, 0)
    pared_lejos = [(6, 6)]
    assert hay_distancia_suficiente(cabeza_serpiente, pared_lejos), "Error: se indicó que la distancia no es suficiente cuando sí lo es."

    # Caso de prueba donde la distancia no es suficiente
    pared_cerca = [(4, 4)]
    assert not hay_distancia_suficiente(cabeza_serpiente, pared_cerca), "Error: se indicó que la distancia es suficiente cuando no lo es."

    # Caso de prueba con distancia mínima personalizada
    distancia_minima_personalizada = 3
    pared_cerca_con_distancia_personalizada = [(3, 3)]
    assert not hay_distancia_suficiente(cabeza_serpiente, pared_cerca_con_distancia_personalizada, distancia_minima_personalizada), "Error: no se respetó la distancia mínima personalizada."

    print("OK")

def test_genera_paredes_aleatorias():
    print("genera_paredes_aleatorias...", end="")
    
    serpiente = [(0, 0), (0, 1), (1, 1), (2, 1)]
    filas = columnas = 10
    num_paredes = 4
    
    conjuntos_paredes = set()

    for _ in range(100):
        paredes_generadas = genera_paredes_aleatorias(serpiente, filas, columnas, num_paredes)

        # Verificar que el número de paredes generadas es correcto
        assert len(paredes_generadas) == num_paredes, "Error: número incorrecto de paredes generadas."

        # Verificar que no hay superposición y que las paredes están a una distancia suficiente
        for pared in paredes_generadas:
            assert not hay_superposicion(pared, serpiente, [otra_pared for otra_pared in paredes_generadas if otra_pared != pared]), "Error: hay superposición entre paredes, o entre una pared y la serpiente."
            assert hay_distancia_suficiente(serpiente[0], pared), "Error: una pared está demasiado cerca de la cabeza de la serpiente."

        # Convertir cada lista de paredes a una tupla y añadirla al conjunto para verificar después la variabilidad
        conjuntos_paredes.add(tuple(tuple(pared) for pared in paredes_generadas))

    # Verificar que se generaron conjuntos de paredes variados
    assert len(conjuntos_paredes) > 90, "Error: no hay suficiente variación en las paredes generadas."

    print("OK")


if __name__ == '__main__':
    print("Ejecutando tests de utiles_paredes")    
    test_genera_posicion_aleatoria_pared()
    test_crea_pared()
    test_hay_superposicion()
    test_hay_distancia_suficiente()
    test_genera_paredes_aleatorias()
    print("Todos los tests superados.")