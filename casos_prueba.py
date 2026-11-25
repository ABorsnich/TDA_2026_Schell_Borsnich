
from juego_piedras_bt import Color

V = Color.VERDE
C = Color.CELESTE
N = Color.VACIO

casos = [
    # Caso 1: Tablero pequeño donde se pueden cubrir todas las filas.
    ([[V, C], [C, V]], 0),

    # Caso 2: Columna con mayoría de piedras verdes.
    ([[V, N], [V, N], [C, N]], 1),

    # Caso 3: Dos columnas con distintas distribuciones de colores.
    ([[V, C], [V, C], [C, N]], 0),

    # Caso 4: Tres columnas con distintas distribuciones de colores.
    ([[V, N, C], [N, C, V], [C, V, N]], 0),

    # Caso 5: No es posible cubrir todas las filas.
    ([[V, N], [N, C], [V, C], [C, N]], 1),

    # Caso 6: Tablero con una columna completamente vacía.
    ([[N, N], [V, C], [C, V]], 1),

    # Caso 7: Tablero con varias alternativas de asignación.
    ([[V, V, C], [C, C, V], [V, C, N], [N, V, C]], 0),

    # Caso 8: Tablero de cuatro columnas con distribuciones variadas.
    ([[V, N, C, N], [N, C, N, V],
      [C, N, V, N], [N, V, N, C]], 0),

    # Caso 9: Tablero con muchas combinaciones posibles.
    ([[V, C, V], [C, V, C], [V, C, V], [C, V, C]], 0),

    # Caso 10: Tablero donde algunas filas no pueden cubrirse.
    ([[V, N, N], [N, C, N], [N, N, V],
      [C, N, N], [N, V, N]], 2),

    # Caso 11: Tablero vacío.
    ([], 0)
]
