from mtf import move_to_front
from utils import imprimir_resultado

def main():
    lista_inicial = [0, 1, 2, 3, 4]

    secuencias = {
        "Secuencia 1": [0, 1, 2, 3, 4] * 4,
        "Secuencia 2": [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4],
        "Secuencia 3 (mejor caso)": [0] * 20,
        "Secuencia 4 (peor caso)": [4, 3, 2, 1, 0] * 4,
        "Secuencia 5 (repetido 2)": [2] * 20,
        "Secuencia 6 (repetido 3)": [3] * 20
    }

    for nombre, secuencia in secuencias.items():
        print(f"\n--- {nombre} ---")
        costo_total, historial = move_to_front(lista_inicial.copy(), secuencia)
        imprimir_resultado(historial, costo_total)

if __name__ == "__main__":
    main()
