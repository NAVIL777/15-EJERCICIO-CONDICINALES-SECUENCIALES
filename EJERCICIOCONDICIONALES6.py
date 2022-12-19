import os
os.system("cls")

edad=input(input("INTRODUCE TU EDAD"))
# Decision del precio en funcion de la edad

if edad< 4:
    precio= 0
elif edad <= 18:
    precio= 4
else:
    precio= 10
# Mostrar precio
print("EL PRECIO DE LA ENTRADA ES", precio, "$.")

'El precio de la entrada es S/. 4 '

