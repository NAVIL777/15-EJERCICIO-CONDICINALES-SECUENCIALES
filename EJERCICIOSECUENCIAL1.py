import os
os.system("cls")
a= int(input("ingresa el numero de mujeres: "))
b= int(input("ingresa el numero de hombres: "))

total= a+b

print("el porcentaje de mujeres es: ",(a/total)*100,"%")
print("el porcentaje de hombres es: ",(b/total)*100,"%")