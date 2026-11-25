VACIA, VERDE, CELESTE = ".", "V", "C"

def validador_piedras(T, T_prima):
    n = len(T)
    if n == 0:
        return len(T_prima) == 0
    m = len(T[0])

    if len(T_prima) != n:
        return False
    for i in range(n):
        if len(T_prima[i]) != m:
            return False

    # solo se pueden remover piedras (no agregar ni cambiar de color
    for i in range(n):
        for j in range(m):
            if T_prima[i][j] not in (VACIA, VERDE, CELESTE):
                return False
            if T_prima[i][j] != VACIA and T_prima[i][j] != T[i][j]:
                return False

    # c/fila debe tener al menos una piedra
    for i in range(n):
        tiene_piedra = False
        for j in range(m):
            if T_prima[i][j] != VACIA:
                tiene_piedra = True
                break
        if not tiene_piedra:
            return False

    # ninguna columna puede tener piedras de ambos colores
    for j in range(m):
        hay_verde = False
        hay_celeste = False
        for i in range(n):
            if T_prima[i][j] == VERDE:
                hay_verde = True
            elif T_prima[i][j] == CELESTE:
                hay_celeste = True
        if hay_verde and hay_celeste:
            return False

    return True
