import os
os.system("cls")

salario=int(input("Ingrese el salario del profesor:"))
if salario < 18000:
    salario += (salario * 0.12)
    print ("El nuevo salario del profesor es",salario)
elif 18000 <= salario <= 30000:
    salario += (salario * 0.08)
    print("El nuevo salario del profesor es",salario)
elif 30000 < salario <= 50000:
    salario += (salario * 0.08)
    print("El nuevo salario del profesor",salario)
else:
    salario += (salario * 0.06)
    print("El nuevo salario del profesor es",salario)
    