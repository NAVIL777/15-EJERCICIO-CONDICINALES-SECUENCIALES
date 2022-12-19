import os
os.system("cls")

n1=int(input("Ingrese el primer nuemro:"))
n2=int(input("Ingrese el segundo nuemro:"))
n3=int(input("Ingrese el tercer nuemro:"))

if n1 < n2 < n3:
    print("Los numeros estan ordenados de forma creciente")
else:
    print("Los numeros no estan ordenados de forma creciente.")