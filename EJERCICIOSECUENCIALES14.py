import os
os.system("cls")

print("")
horas_trabajadas=float(input("Ingrese las horas trabajadas : "))
tarifa_horaria=float(input("Ingrese la tarifa horaria : "))

sueldo_basico=tarifa_horaria*horas_trabajadas
bonificacion=sueldo_basico*0.20
sueldo_bruto=sueldo_basico+bonificacion
descuento=sueldo_bruto*0.10
sueldo_neto=sueldo_bruto-descuento

print("")
print("sueldo basico: s/.",format(sueldo_basico,".2f"))
print("sueldo bruto: s/.",format(sueldo_bruto,".2f"))
print("sueldo neto: s/.",format(sueldo_neto,".2f"))
