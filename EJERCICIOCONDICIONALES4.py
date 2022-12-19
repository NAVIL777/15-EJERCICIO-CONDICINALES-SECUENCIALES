import os
os.system("cls")
# Presentacion del menu con los tipos de pizza
print("Bienvenido a la pizzeria Napoles.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
ingrediente = input("Introduce el numero correspondiente al tipo de pizza que quieres:")
# Decision sobre el tipo de pizza 
if type == "1":
    print("Ingredientes de pizza vegetariana\n\t 1- Pimiento\n\t2- tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamon\n\t3- Salmon\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamon")
    else:
        print("salmon")
        
