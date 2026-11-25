from enum import Enum
import sys

class Color (Enum): 
    VACIO = 0
    VERDE = 1
    CELESTE = 2


def juego_piedras(tablero):
    n = len(tablero)
    if n == 0:
        return 0, [], []
    m = len(tablero[0])

    colores_actuales = [Color.VACIO] * m

    min_filas_vacias, mejor_sol = bt_juego_piedras(tablero, 0, colores_actuales, -1, [Color.VACIO]*m)
    
    tablero_sol = reconstruir_tablero(tablero, mejor_sol)
    
    return min_filas_vacias, tablero_sol, mejor_sol 

def contar_filas_vacias(tablero, colores_col):
    n = len(tablero)
    m = len(tablero[0])
    filas_vacias = 0

    for i in range(n):
        fila_cubierta = False
        for j in range(m):
            color_elegido = colores_col[j]
            if color_elegido != Color.VACIO and tablero[i][j] == color_elegido:
                fila_cubierta = True
                break
        if not fila_cubierta:
            filas_vacias += 1
    return filas_vacias

def columna_tiene_piedras(tablero, columna):
    vacia = False

    for fila in tablero:
        if fila[columna] != Color.VACIO:
            vacia = True
            break
    
    return vacia

def bt_juego_piedras(tablero, columna, colores_actuales, mejor_vacias, mejor_sol):
    
    n = len(tablero)
    m = len(tablero[0])

    if mejor_vacias == 0:
        return mejor_vacias, mejor_sol

    if columna == m:
        vacias = contar_filas_vacias(tablero, colores_actuales)
        if mejor_vacias == -1 or vacias < mejor_vacias:
            return vacias, colores_actuales[:]
        return mejor_vacias, mejor_sol

    if not columna_tiene_piedras(tablero, columna):
        colores_actuales[columna] = Color.VACIO
        return bt_juego_piedras(tablero, columna + 1, colores_actuales, mejor_vacias, mejor_sol)

    for opcion in (Color.VERDE, Color.CELESTE, Color.VACIO):
        colores_actuales[columna] = opcion
        
        mejor_vacias, mejor_sol = bt_juego_piedras(
            tablero, columna + 1, colores_actuales, mejor_vacias, mejor_sol
        )

    colores_actuales[columna] = Color.VACIO
    return mejor_vacias, mejor_sol

def reconstruir_tablero(tablero, colores_col):
    n = len(tablero)
    m = len(tablero[0]) if n > 0 else 0
    resultado = [[Color.VACIO] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if tablero[i][j] == colores_col[j]:
                resultado[i][j] = tablero[i][j]

    return resultado

def obtener_piedras_removidas(tablero, resultado):
    removidas = []
    n = len(tablero)
    m = len(tablero[0])

    for i in range(n):
        for j in range(m):
            if tablero[i][j] != Color.VACIO and resultado[i][j] == Color.VACIO:
                removidas.append((i, j))

    return removidas

def obtener_filas_vacias(resultado):
    filas_vacias = []
    for i, fila in enumerate(resultado):
        if all(celda == Color.VACIO for celda in fila):
            filas_vacias.append(i)
    return filas_vacias

def formatear_solucion(tablero, mejor_colores, min_filas_vacias, resultado):
    simbolos_col = {
        Color.VERDE: "V",
        Color.CELESTE: "C",
        Color.VACIO: "-",
    }
    simbolos_celda = {
        Color.VERDE: "V",
        Color.CELESTE: "C",
        Color.VACIO: ".",
    }

    colores_str = " ".join(simbolos_col[c] for c in mejor_colores)
    removidas = obtener_piedras_removidas(tablero, resultado)
    removidas_str = ", ".join(f"({i}, {j})" for i, j in removidas)

    lineas_tablero = [
        "".join(simbolos_celda[celda] for celda in fila)
        for fila in resultado
    ]

    if min_filas_vacias > 0:
        indices_vacias = obtener_filas_vacias(resultado)
        linea_vacias = f"Filas vacías: {min_filas_vacias} -> {indices_vacias}"
    else:
        linea_vacias = f"Filas vacías: {min_filas_vacias}"

    lineas = [
        f"Colores por columna: {colores_str}",
        f"Piedras removidas: {removidas_str}",
        "Tablero resultante:",
        *lineas_tablero,
        linea_vacias,
    ]
    return "\n".join(lineas)


def leer_tablero(ruta):
    mapa = {
        ".": Color.VACIO,
        "V": Color.VERDE,
        "C": Color.CELESTE,
    }
    tablero = []
    with open(ruta) as f:
        for linea in f:
            fila_str = linea.strip()
            if not fila_str or fila_str.startswith("#"):
                continue
            fila = [mapa[celda] for celda in fila_str if celda in mapa]
            if fila:
                tablero.append(fila)
    return tablero

def main():
    if len(sys.argv) != 2:
        print("Se usa asi: python3 tp3.py ruta/a/entrada.txt")
        return

    ruta = sys.argv[1]
    tablero = leer_tablero(ruta)

    if not tablero:
        print("El tablero está vacío o no se pudo leer.")
        return

    min_vacias, solucion, colores = juego_piedras(tablero)
    salida = formatear_solucion(tablero, colores, min_vacias, solucion)
    print(salida)


if __name__ == "__main__":
    main()
