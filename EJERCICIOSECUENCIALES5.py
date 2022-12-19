import os
os.system("cls")

capacidad_en_GB=float(input('Ingresa el valor de capacidad de GB:'))
capacidad_en_MB=capacidad_en_GB*1024
capacidad_en_KB=capacidad_en_MB*1024
capacidad_en_B=capacidad_en_KB*1024
print('Valor de capacidad en B: ' + repr(capacidad_en_B))
print('Valor de capacidad en KB: ' + repr(capacidad_en_KB))
print('Valor de capacidad en MB: ' + repr(capacidad_en_MB))
print()
