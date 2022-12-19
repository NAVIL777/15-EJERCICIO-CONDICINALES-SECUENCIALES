import os
os.system("cls")

salario=float(input("Ingrese el salario del trabajdor: "))
categoria=float(input("Ingrese el categoria del trabajdor: "))

if categoria == 1:
    numero_horas_extra=int(input("Ingrese la cantidad de horas extra que ha hecho el trabajador: "))
    if numero_horas_extra < 30:
        salario += (numero_horas_extra *40)
        print("El salario a pagar es",salario)
    else:
        salario += (30 * 40)
        print("El salario a pagar es",salario)

if categoria == 2:
    numero_horas_extra=int(input("Ingrese la cantidad de horas extra que ha hecho el trabajador: "))
    if numero_horas_extra < 30:
        salario += (numero_horas_extra *40)
        print("El salario a pagar es",salario)
    else:
        salario += (30 * 50)
        print("El salario a pagar es",salario)

if categoria == 3:
    numero_horas_extra=int(input("Ingrese la cantidad de horas extra que ha hecho el trabajador: "))
    if numero_horas_extra < 30:
        salario += (numero_horas_extra *40)
        print("El salario a pagar es",salario)
    else:
        salario += (30 * 85)
        print("El salario a pagar es",salario)

else:
    print("El salario a pagar es", salario)