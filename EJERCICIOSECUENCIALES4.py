import os
os.system("cls")
'1 metro= 100 cm, 1 pie= 12 pulgadas, 1 yarda= 3 pies, 1 pulgadas= 2.54cm'
pies=float(input("pies:"))
pulgadas=float(input("pulgadas:"))

estatura=(((pies*12)+ pulgadas)*2.54)/100

print("la estatura en metros es:",format(estatura,".2f"))
