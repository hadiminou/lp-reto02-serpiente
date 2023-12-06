import random
from typing import List, Tuple

def comprueba_choque(serpiente: List[Tuple[int, int]]) -> bool:
    '''
    Comprueba si la serpiente se ha chocado consigo misma. Tenga en cuenta
    que la serpiente avanza siempre por su cabeza, que está situada en la 
    primera posición de la lista.

    Args:
    serpiente (List[Tuple[int, int]]): Lista de tuplas representando las posiciones de la serpiente.

    Returns:
    bool: True si la serpiente se ha chocado consigo misma, False en caso contrario.

    Tests:
    >>> comprueba_choque([(0,0), (1,0), (0,0)])
    True
    >>> comprueba_choque([(0,0), (1,0), (2,0)])
    False
    '''
    # TODO: Implemente la función
    return False

def come_serpiente(serpiente: List[Tuple[int, int]], posicion_comida: Tuple[int, int]) -> bool:
    '''
    Comprueba si la cabeza de la serpiente está en la misma posición que la comida.

    Args:
    serpiente (List[Tuple[int, int]]): Lista de tuplas representando las posiciones de la serpiente.
    posicion_comida (Tuple[int, int]): Tupla representando la posición de la comida.

    Returns:
    bool: True si la cabeza de la serpiente está en la misma posición que la comida, False en caso contrario.

    Tests:
    >>> come_serpiente([(0,0), (1,0)], (0,0))
    True
    >>> come_serpiente([(0,0), (1,0)], (2,2))
    False
    '''
    # TODO: Implemente la función
    return False

def genera_comida_aleatoria(serpiente: List[Tuple[int, int]], paredes: List[List[Tuple[int, int]]], filas: int, columnas: int) -> Tuple[int, int]:
    '''
    Genera una posición aleatoria para la comida que no esté en la misma posición que la serpiente o las paredes.

    Args:
    serpiente (List[Tuple[int, int]]): Lista de tuplas representando las posiciones de la serpiente.
    paredes (List[List[Tuple[int, int]]]): Lista de listas de tuplas representando las posiciones de las paredes.
    filas (int): Número de filas en el tablero de juego.
    columnas (int): Número de columnas en el tablero de juego.

    Returns:
    Tuple[int, int]: Posición aleatoria para la comida.

    Tests:
    >>> genera_comida_aleatoria([(0,0)], [[(1,0), (2,0)]], 5, 5)  # Esto es un ejemplo; el resultado será aleatorio.
    (3, 3)
    '''
    # TODO: Implemente la función
    return (10, 3)

def mueve_serpiente(serpiente: List[Tuple[int, int]], direccion: str, filas: int, columnas: int) -> None:
    '''
    Mueve la serpiente en el tablero según la dirección dada. El tablero es circular, lo que significa
    que si la serpiente se sale por la derecha, debe aparecer por la izquierda, y viceversa (y lo 
    mismo si se sale por arriba o por abajo).

    Args:
    serpiente (List[Tuple[int, int]]): Lista de tuplas representando las posiciones de la serpiente.
    direccion (str): Dirección en la que se debe mover la serpiente ('Left', 'Right', 'Down', 'Up').
    filas (int): Número de filas en el tablero de juego.
    columnas (int): Número de columnas en el tablero de juego.

    Returns:
    None: La función no retorna nada, pero modifica la lista 'serpiente' en su lugar.

    Tests:
    >>> serpiente = [(2,2), (2,1), (2,0)]
    >>> mueve_serpiente(serpiente, "Up", 5, 5)
    >>> serpiente
    [(2, 3), (2, 2), (2, 1)]
    >>> mueve_serpiente(serpiente, "Left", 5, 5)
    >>> serpiente
    [(1, 3), (2, 3), (2, 2)]
    '''
    # TODO: Implemente la función
    pass

def crece_serpiente(serpiente: List[Tuple[int, int]]) -> None:
    '''
    Hace crecer la serpiente añadiendo duplicando la posición de la cola

    Args:
    serpiente (List[Tuple[int, int]]): Lista de tuplas representando las posiciones de la serpiente.

    Returns:
    None: La función no retorna nada, pero modifica la lista 'serpiente' en su lugar.

    Tests:
    >>> serpiente = [(2,2), (2,1), (2,0)]
    >>> crece_serpiente(serpiente)
    >>> serpiente
    [(2,2), (2,1), (2,0), (2,0)]
    '''
    # TODO: Implemente la función
    pass

