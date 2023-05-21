#INTEGRANTES:
#FERNANDO NÚÑEZ BAUTISTA
import numpy as np
def resolver_sistema():
    n = int(input("Introduce el número de ecuaciones: "))
    A = np.zeros((n, n))
    B = np.zeros((n, 1))
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input(f"Introduce el coeficiente A[{i+1}][{j+1}]: "))
        B[i][0] = float(input(f"Introduce el término independiente B[{i+1}]: "))
    X = np.linalg.solve(A, B)
    print("La solución del sistema de ecuaciones es:")
    print(X)
def suma_matrices(A, B):
    return np.add(A, B)
def resta_matrices(A, B):
    return np.subtract(A, B)
def producto_matrices(A, B):
    return np.dot(A, B)
def determinante_gauss_jordan(A):
    n = len(A)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        A[i], A[max_index] = A[max_index], A[i]
        for j in range(i+1, n):
            c = A[j][i] / A[i][i]
            for k in range(i, n+1):
                A[j][k] -= c * A[i][k]
    det = 1
    for i in range(n):
        det *= A[i][i]
    return det
def main():
    while True:
        print("\n¿Qué operación deseas realizar?\n1. Resolver un sistema de ecuaciones\n2. Sumar matrices\n3. Restar matrices\n4. Multiplicar matrices\n5. Calcular determinante por el método de Gauss-Jordan\n6. Salir")
        opcion = int(input("Introduce el número de la opción que deseas: "))
        if opcion == 1:
            resolver_sistema()
        elif opcion == 2:
            n = int(input("Introduce el número de filas de las matrices: "))
            m = int(input("Introduce el número de columnas de las matrices: "))
            A = np.zeros((n, m))
            B = np.zeros((n, m))
            for i in range(n):
                for j in range(m):
                    A[i][j] = float(input(f"Introduce el elemento A[{i+1}][{j+1}]: "))
                    B[i][j] = float(input(f"Introduce el elemento B[{i+1}][{j+1}]: "))
            C = suma_matrices(A, B)
            print("La suma de las matrices es:")
            print(C)
        elif opcion == 3:
            n = int(input("Introduce el número de filas de las matrices: "))
            m = int(input("Introduce el número de columnas de las matrices: "))
            A = np.zeros((n, m))
            B = np.zeros((n, m))
            for i in range(n):
                for j in range(m):
                    A[i][j] = float(input(f"Introduce el elemento A[{i+1}][{j+1}]: "))
                    B[i][j] = float(input(f"Introduce el elemento B[{i+1}][{j+1}]: "))
            C = resta_matrices(A, B)
            print("La resta de las matrices es:")
            print(C)
        elif opcion == 4:
            n = int(input("Introduce el número de filas de la matriz A: "))
            m = int(input("Introduce el número de columnas de la matriz A: "))
            p = int(input("Introduce el número de columnas de la matriz B: "))
            A = np.zeros((n, m))
            B = np.zeros((m, p))
            for i in range(n):
                for j in range(m):
                    A[i][j] = float(input(f"Introduce el elemento A[{i+1}][{j+1}]: "))
            for i in range(m):
                for j in range(p):
                    B[i][j] = float(input(f"Introduce el elemento B[{i+1}][{j+1}]: "))
            C = producto_matrices(A, B)
            print("El producto de las matrices es:")
            print(C)
        elif opcion == 5:
            n = int(input("Introduce el número de filas de la matriz: "))
            A = np.zeros((n, n+1))
            for i in range(n):
                for j in range(n):
                    A[i][j] = float(input(f"Introduce el elemento A[{i+1}][{j+1}]: "))
                A[i][n] = float(input(f"Introduce el término independiente B[{i+1}]: "))
            det = determinante_gauss_jordan(A)
            print(f"El determinante de la matriz es: {det}")
        elif opcion == 6:
            print("Calculadora apagada.")
            break
        else:
            print("Opción inválida, ingresa solo números que coincidan con el menú.")
if __name__ == "__main__":
    main()
