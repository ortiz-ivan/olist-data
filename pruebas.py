def crear_matriz(columnas, filas):
    matriz = [["." for _ in range(columnas)] for _ in range(filas)]
    return matriz


def agregar_personajes(matriz, pos_gato, pos_raton):
    fila_gato, col_gato = pos_gato
    fila_raton, col_raton = pos_raton

    matriz[fila_gato][col_gato] = "G"
    matriz[fila_raton][col_raton] = "R"


def movimientos_validos(fila_actual, columna_actual, columnas, filas):
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    movimientos = []
    for df, dc in direcciones:
        nueva_fila = fila_actual + df
        nueva_columna = columna_actual + dc
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            movimientos.append((nueva_fila, nueva_columna))
    return movimientos


def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))


def main():
    columnas = 5
    filas = 5
    matriz = crear_matriz(columnas, filas)
    pos_xgato = 4
    pos_ygato = 4
    pos_xraton = 0
    pos_yraton = 0
    pos_gato = pos_xgato, pos_ygato
    pos_raton = pos_xraton, pos_yraton
    agregar_personajes(matriz, pos_gato, pos_raton)
    mostrar_matriz(matriz)


main()
