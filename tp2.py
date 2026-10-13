import sys

def resolver(monedas):
    n = len(monedas)
    if n == 0:
        return [], 0, 0


    opt = [[0] * n for _ in range(n)]

    # Caso base queda una sola moneda
    for i in range(n):
        opt[i][i] = monedas[i]

    for largo in range(2, n + 1):
        for i in range(n - largo + 1):
            j = i + largo - 1

            # sophia toma la moneda izquierda
            if monedas[i + 1] >= monedas[j]:
                if i + 2 <= j:
                    futuro_izq = opt[i + 2][j]
                else:
                    futuro_izq = 0
            else:
                if i + 1 <= j - 1:
                    futuro_izq = opt[i + 1][j - 1]  
                else:
                    futuro_izq = 0
            izq = monedas[i] + futuro_izq

            # sophia toma la moneda derecha
            if monedas[i] >= monedas[j - 1]:
                if i + 1 <= j - 1:
                    futuro_der = opt[i + 1][j - 1]  
                else:
                    futuro_der = 0
            else:
                if i <= j - 2:
                    futuro_der = opt[i][j - 2]
                else:
                    futuro_der = 0
            der = monedas[j] + futuro_der

            # en caso de empate se elige el extremo izquierdo
            if izq >= der:
                opt[i][j] = izq
            else:
                opt[i][j] = der

    return reconstruir_elecciones(opt, monedas)

def reconstruir_elecciones(opt, monedas):
    n = len(monedas)
    decisiones = []
    i = 0
    j = n - 1

    ganancia_mateo = 0

    while i <= j:
        if i == j:
            # Caso base: queda unicamente esa moneda
            decisiones.append(f"Sophia toma la izquierda ({monedas[i]})")
            break

        # uso alternativa de tomar la izquierda para deducir la decisión
        if monedas[i + 1] >= monedas[j]:
            if i + 2 <= j:
                futuro_izq = opt[i + 2][j]
            else:
                futuro_izq = 0
        else:
            if i + 1 <= j - 1:
                futuro_izq = opt[i + 1][j - 1]  
            else:
                futuro_izq = 0
        valor_si_izq = monedas[i] + futuro_izq

        # Si el valor calculado coincide con la matriz, Sophia eligio la izquierda
        if opt[i][j] == valor_si_izq:
            decisiones.append(f"Sophia toma la izquierda ({monedas[i]})")
            i += 1
        else:
            decisiones.append(f"Sophia toma la derecha ({monedas[j]})")
            j -= 1

        # Turno de Mateo (Estrategia Greedy)
        if i <= j:
            if monedas[i] >= monedas[j]:
                decisiones.append(f"Mateo toma la izquierda ({monedas[i]})")
                ganancia_mateo += monedas[i]
                i += 1
            else:
                decisiones.append(f"Mateo toma la derecha ({monedas[j]})")
                ganancia_mateo += monedas[j]
                j -= 1

    return decisiones, opt[0][n-1], ganancia_mateo

def leer_entrada(ruta):
    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            valores = linea.split(";")
            return [int(v.strip()) for v in valores if v.strip()]
    return []

def main():
    if len(sys.argv) != 2:
        print("Se usa asi: python3 tp2.py ruta/a/entrada.txt")
        return
    ruta = sys.argv[1]
    monedas = leer_entrada(ruta)
    
    if not monedas:
        print("No se encontraron monedas validas.")
        return

    decisiones, ganancia_sophia, ganancia_mateo = resolver(monedas)

    print("; ".join(decisiones))
    print(f"Ganancia Sophia: {ganancia_sophia}")
    print(f"Ganancia Mateo: {ganancia_mateo}")

if __name__ == "__main__":
    main()