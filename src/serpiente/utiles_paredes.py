import random
from typing import List, Tuple

def genera_posicion_aleatoria_pared(filas: int, columnas: int, tamaño_pared: int) -> Tuple[int, int, str]:
    '''
    Genera una posición y orientación aleatorias para una pared.

    Args:
    filas (int): Número de filas en el tablero de juego.
    columnas (int): Número de columnas en el tablero de juego.
    tamaño_pared (int): Tamaño de la pared a generar.

    Returns:
    Tuple[int, int, str]: Posición inicial y orientación de la pared.

    Tests:
    >>> genera_posicion_aleatoria_pared(5, 5, 3)  # Esto es un ejemplo; el resultado será aleatorio.
    (2, 1, 'vertical')
    '''
    # TODO: Implemente la función
    return (0, 0, 'vertical')

def crea_pared(x: int, y: int, orientacion: str, tamaño_pared: int) -> List[Tuple[int, int]]:
    '''
    Crea una pared basada en una posición inicial, orientación y tamaño.

    Args:
    x_position (int): Posición inicial en x de la pared.
    y_position (int): Posición inicial en y de la pared.
    orientacion (str): Orientación de la pared ('horizontal' o 'vertical').
    tamaño_pared (int): Tamaño de la pared.

    Returns:
    List[Tuple[int, int]]: Lista de tuplas representando las posiciones de la pared.

    Tests:
    >>> crea_pared(0, 0, 'horizontal', 3)
    [(0, 0), (1, 0), (2, 0)]
    >>> crea_pared(0, 0, 'vertical', 3)
    [(0, 0), (0, 1), (0, 2)]
    '''
    # TODO: Implemente la función
    return []

def hay_superposicion(pared: List[Tuple[int, int]], serpiente: List[Tuple[int, int]], 
                      paredes_existentes: List[List[Tuple[int, int]]]) -> bool:
    '''
    Comprueba si hay una superposición entre la pared propuesta, la serpiente y las paredes existentes.

    Args:
    pared (List[Tuple[int, int]]): Lista de tuplas representando las posiciones de la pared propuesta.
    serpiente (List[Tuple[int, int]]): Lista de tuplas representando las posiciones de la serpiente.
    paredes_existentes (List[List[Tuple[int, int]]]): Lista de listas de tuplas representando las posiciones de las paredes existentes.

    Returns:
    bool: True si hay superposición, False en caso contrario.

    Tests:
    >>> hay_superposicion([(2,2)], [(0,0), (1,1)], [[(3,3), (3,4)]])
    False
    >>> hay_superposicion([(0,0)], [(0,0), (1,1)], [])
    True
    '''
    # TODO: Implemente la función
    return False

def hay_distancia_suficiente(cabeza_serpiente: Tuple[int, int], pared: List[Tuple[int, int]], 
                             distancia_minima: int = 5) -> bool:
    '''
    Comprueba si la distancia entre la cabeza de la serpiente y la pared propuesta es suficiente.

    Args:
    cabeza_serpiente (Tuple[int, int]): Posición de la cabeza de la serpiente.
    pared (List[Tuple[int, int]]): Lista de tuplas representando las posiciones de la pared propuesta.
    distancia_minima (int, opcional): Distancia mínima requerida. Por defecto es 5.

    Returns:
    bool: True si la distancia es suficiente, False en caso contrario.

    Tests:
    >>> hay_distancia_suficiente((0,0), [(6,6)])
    True
    >>> hay_distancia_suficiente((0,0), [(4,4)])
    False
    '''
    # TODO: Implemente la función
    return False

def genera_paredes_aleatorias(serpiente: List[Tuple[int, int]], filas: int, columnas: int, 
                              num_paredes: int = 4, tam_min: int = 3, tam_max: int = 6) -> List[List[Tuple[int, int]]]:
    '''
    Genera una lista de paredes de tamaño y posición aleatorios, asegurándose de que no haya superposiciones
    ni estén demasiado cerca de la cabeza de la serpiente. 

    Args:
    serpiente (List[Tuple[int, int]]): Lista de tuplas representando las posiciones de la serpiente.
    filas (int): Número de filas en el tablero de juego.
    columnas (int): Número de columnas en el tablero de juego.
    num_paredes (int, opcional): Número de paredes a generar. Por defecto es 4.
    tam_min (int, opcional): Tamaño mínimo de las paredes. Por defecto es 3.
    tam_max (int, opcional): Tamaño máximo de las paredes. Por defecto es 6.

    Returns:
    List[List[Tuple[int, int]]]: Lista de listas de tuplas representando las posiciones de las paredes generadas.
    '''
    # TODO: Implemente la función
    return []

