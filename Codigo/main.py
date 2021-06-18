import numpy as np
print ("<<  MULTIPLICACION DE MATRICES  >>\n")

print ("MATRIZ 1:")
f_mat_1 = int(input("Número de filas: "))
c_mat_1 = int(input("Número de columnas: "))

print ("\nMATRIZ 2:")
f_mat_2 = int(input("Número de filas: "))
c_mat_2 = int(input("Número de columnas: "))

while (c_mat_1 != f_mat_2):
    print("\nDatos Ingresado erroneos.Vuelva a ingresar...\n")
    c_mat_1 = int(input("Numero de columnas de la Matriz 1: "))
    f_mat_2 = int(input("Numero de filas de la Matriz 2: "))
    if (c_mat_1 == f_mat_2):
        break

Mat1 = np.zeros((f_mat_1, c_mat_1))  # aqui columnas (columnas, filas)
Mat2 = np.zeros((f_mat_2, c_mat_2))
Resul = np.zeros((f_mat_1, c_mat_2))

print("\nDatos Matriz 1\n")
for i in range(f_mat_1):
    for j in range(c_mat_1):
        Mat1[i][j] = int(input("Fila {} , Columna {}  : ".format(i + 1, j + 1)))

print("\nDatos Matriz 2\n")
for i in range(f_mat_2):
    for j in range(c_mat_2):
        Mat2[i][j] = int(input("Fila {} , Columna {}  : ".format(i + 1, j + 1)))

print("\nMultiplicacion de las matrices: \n", np.dot(Mat1, Mat2))