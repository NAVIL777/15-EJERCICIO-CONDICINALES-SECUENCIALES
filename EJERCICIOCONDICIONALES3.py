import os
os.system("cls")
name = input("¿Como te llamas? ")
gender = input("¿Cual es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
if name.lower() < "m":
    group ="A"
else:
    group ="B"
print("tu grupo es "+ group)
