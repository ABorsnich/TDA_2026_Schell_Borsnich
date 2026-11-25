from juego_piedras_bt import juego_piedras
from juego_piedras_pl import juego_piedras_pl
from casos_prueba import casos

for i, (tablero, esperado) in enumerate(casos):
    resultado_bt = juego_piedras(tablero)
    resultado_pulp = juego_piedras_pl(tablero)

    assert resultado_bt[0] == esperado, (f"Caso {i + 1}: BT dio {resultado_bt[0]}, esperado {esperado}")
    assert resultado_pulp[0] == esperado, (f"Caso {i + 1}: PL dio {resultado_pulp[0]}, esperado {esperado}")

    print(f"Caso {i + 1}: OK")