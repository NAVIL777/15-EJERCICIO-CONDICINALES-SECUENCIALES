import os
os.system("cls")

compra=int(input("Ingrese el monto de la compra:"))
if compra < 800:
    print ("El total a pagar es",compra)
elif 800 <= compra <= 1500:
    compra -= (compra * 0.10)
    print("El total a pagar, con su respectivo descuento es",compra)
elif 1500 < compra <= 5000:
    compra -= (compra * 0.15)
    print("total a pagar, con su respectivo descuento es",compra)
else:
    compra -= (compra * 0.20)
    print("El total a pagar, con su respectivo descuento es",compra)
