import sys


def resolver(monedas):

    izquierda = 0
    derecha = len(monedas) - 1

    decisiones = []
    ganancia_sophia = 0

    turno_sophia = True

    while izquierda <= derecha:

        if turno_sophia:
            # Sophia elige la mondea de mayor valor disponible.
            if monedas[izquierda] >= monedas[derecha]:
                ganancia_sophia += monedas[izquierda]
                decisiones.append("Primera moneda para Sophia")
                izquierda += 1
            else:
                ganancia_sophia += monedas[derecha]
                decisiones.append("Última moneda para Sophia")
                derecha -= 1

        else:
            # Sophia decide que moneda recibe Mateo.
            # Le asigna la de menor vlaor disponible.
            if monedas[izquierda] <= monedas[derecha]:
                decisiones.append("Primera moneda para Mateo")
                
                izquierda += 1
            else:
                decisiones.append("Última moneda para Mateo")
                derecha -= 1

        turno_sophia = not turno_sophia

    return decisiones, ganancia_sophia


def leer_entrada(ruta):
    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()

            # Ignorar lineas vacias y comentarios.
            if not linea or linea.startswith("#"):
                continue

            valores = linea.split(";")

            monedas = []

            for valor in valores:
                valor = valor.strip()

                if valor:
                    monedas.append(int(valor))

            return monedas

    return []


def main():
    if len(sys.argv) != 2:
        print("Se usa asi: python3 tp1.py ruta/a/entrada.txt")
        return

    ruta = sys.argv[1]
    monedas = leer_entrada(ruta)

    decisiones, ganancia_sophia = resolver(monedas)

    print("; ".join(decisiones))
    print(f"Ganancia de Sophia: {ganancia_sophia}")




if __name__ == "__main__":
    main()