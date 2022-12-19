import os
os.system("cls")

a=float(input("Ingrese el primer lado del triangulo: "))
b=float(input("Ingrese el segundo lado del triangulo: "))
c=float(input("Ingrese el tercer lado del triangulo: "))

if (a+b)>c and (a+c)>b and (b+c)>a:
    print("\n los lados corresponde a un triangulo.")

    s=(a+b+c)/2
    area=(s * (s-a) * (s-b) * (s-c)) **0.5
    print("El area del triangulo es",area)

    if(a==b==c):
        print("Se trata de un triangulo equilatero.")
    elif(a==b or a==c or b==c):
        print("Se trata de un triangulo isoceles.")
    else:
        print("Se trata de un triangulo escaleno.")
else:
    print("\n los lados no corresponde a un triangulo.")