import pulp
from enum import Enum
from juego_piedras_bt import Color


def juego_piedras_pl(tablero):
    n = len(tablero)

    if n == 0:
        return 0, [], []

    m = len(tablero[0])

    if m == 0:
        return n, [[] for _ in range(n)], []

    modelo = pulp.LpProblem("Juego_de_piedras", pulp.LpMaximize)

    #Variables 
    verde = pulp.LpVariable.dicts("verde", range(m), cat=pulp.LpBinary) #x_{j,V}
    celeste = pulp.LpVariable.dicts("celeste", range(m), cat=pulp.LpBinary) #x_{j,C}
    cubierta = pulp.LpVariable.dicts("cubierta", range(n), cat=pulp.LpBinary) #y_i

    #Función objetivo
    modelo += pulp.lpSum(cubierta[i] for i in range(n))

    #Restricciones

    #un solo color por columna
    for j in range(m):
        modelo += verde[j] + celeste[j] <= 1

    #Fila cubierta: y_i <= piedras conservadas en la fila i
    for i in range(n):
        piedras_conservadas = []

        for j in range(m):
            if tablero[i][j] == Color.VERDE:
                piedras_conservadas.append(verde[j])
            elif tablero[i][j] == Color.CELESTE:
                piedras_conservadas.append(celeste[j])

        modelo += cubierta[i] <= pulp.lpSum(piedras_conservadas)

   
    modelo.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[modelo.status] != "Optimal":
        raise RuntimeError("No se encontró una solución óptima")

    
    colores_col = colores_columnas(verde, celeste, m)
    tablero_sol = reconstruir_tablero(tablero, colores_col)

    filas_cubiertas = round(pulp.value(modelo.objective))
    filas_vacias = n - filas_cubiertas


    return filas_vacias, tablero_sol, colores_col

#Color de cada columna a aprtir de la solución encontrada
def colores_columnas(verde, celeste, m):
    colores_col = [Color.VACIO] * m

    for j in range(m):
        if pulp.value(verde[j]) > 0.5:
            colores_col[j] = Color.VERDE
        elif pulp.value(celeste[j]) > 0.5:
            colores_col[j] = Color.CELESTE

    return colores_col

def reconstruir_tablero(tablero, colores_col):
    n = len(tablero)
    m = len(colores_col)
    tablero_sol = [[Color.VACIO] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if tablero[i][j] == colores_col[j]:
                tablero_sol[i][j] = tablero[i][j]
    return tablero_sol