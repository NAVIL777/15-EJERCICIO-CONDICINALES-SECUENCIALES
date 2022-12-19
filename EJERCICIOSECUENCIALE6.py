import os
os.system("cls")

from math import pi

def volumen_cilindro(r, h):
    volumen=pi * r**2 * h

    return volumen

def area_total_cilindro(r, h):
    area= 2 * pi * r**2 + 2 * pi * r* h

    return area

radio= 6
altura= 8
print(f'Volumen del cilindro: {volumen_cilindro(radio, altura)}')
