from juego_piedras_bt import juego_piedras
from casos_prueba import casos

for i, (tablero, esperado) in enumerate(casos, 1):
    filas_vacias, _, _ = juego_piedras(tablero)

    if filas_vacias != esperado:
        print(
            f"Caso {i}: ERROR - "
            f"esperado {esperado}, obtenido {filas_vacias}"
        )
    else:
        print(f"Caso {i}: OK - resultado {filas_vacias}")
