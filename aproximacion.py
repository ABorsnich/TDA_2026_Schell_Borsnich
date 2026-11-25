import random
from juego_piedras_bt import Color, reconstruir_tablero, contar_filas_vacias

def aproximacion_gringo(tablero):
    n = len(tablero)
    if n == 0:
        return 0, [], []
    m = len(tablero[0])

    colores = [Color.VACIO] * m

    for j in range(m):
        if random.random() < 0.5:
            colores[j] = Color.VERDE
        else:
            colores[j] = Color.CELESTE

    tablero_sol = reconstruir_tablero(tablero, colores)
    filas_vacias = contar_filas_vacias(tablero, colores)

    return filas_vacias, tablero_sol, colores
