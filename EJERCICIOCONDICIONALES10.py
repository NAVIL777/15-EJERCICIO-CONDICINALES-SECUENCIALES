import os
os.system("cls")

n= float(input("Introduce el dividendo: "))
m= float(input("Introduce el divisor: "))
if m== 0:
    print("¡ERROR! No se puede dividir por 0.")
else:
    print(n/m)