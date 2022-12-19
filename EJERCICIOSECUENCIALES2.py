import os
os.system("cls")

metro=float(input('Ingresa el valor de metro:'))
centimetro=metro*100
pulgadas=centimetro/2.54
pies=pulgadas/12
yarda=pies/3
print("Valor de centimetro:" ,format(centimetro," .2f"),"cm")
print("Valor de pies: " ,format(pies,".2f"),"ft")
print("Valor de pulgadas: " ,format(pulgadas,".2f"),"in")
print("Valor de yarda: " ,format(yarda,".2f"),"yd")
print()
