### Diccionarios ###

my_dict = dict()

print(type(my_dict))

my_other_dict = {"Nombre":"Rafa", "Apellido":"Delgado", "Edad":34, 1:"Python"}

my_dict = { #Esto es simplemente otro formato para una mayor legibilidad
    "Nombre":"Rafa",
    "Apellido":"Delgado",
    "Edad":34,
    "Lenguajes": {"Python","Swift","JavaScript"},
    1:1.76
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) #4
print(len(my_dict)) #5

print(my_other_dict["Nombre"]) #Imprime el valor del índice("Nombre")

#Ahora actualizamos el valor
my_other_dict["Nombre"] = "Pancracio"
print(my_other_dict["Nombre"])

print(my_other_dict[1]) #Para indicar el indice, hay que hacerlo también en su formato, en este caso entero y no "1"

#También podemos añadir nuevos valores al diccionario

my_dict["Peso"] = "74Kg"

print(my_dict) #Aquí ya nos mostrará el nuevo valor

#Para borrar un elemento del diccionario:

del my_dict["Peso"]

print("Nombre" in my_dict) #Comprueba si existe la clave(índice) y no el valor de él
print("Rafa" in my_dict) #False

print(my_dict.items()) #Obtenemos todos los/las clave:valor
print(my_dict.keys()) #Obtenemos todas las claves
print(my_dict.values()) #Obtenemos todos los valores

my_new_dict = dict.fromkeys(("Nombre", 1)) #Creamos un nuevo diccionario con la palabra reservada dict (también podemos partir de otro objeto diccionario que ya existe, pero eso no tendría sentido)
print(my_new_dict)

#También podemos darle índices desde una lista a un diccionario, por ejemplo:

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

#Vamos a meterle valores

my_new_dict = dict.fromkeys(my_dict, "Rafa") #Le metemos a todos los indices el valor Rafa, esto no tendría mucho sentido

my_new_new_dict = my_new_dict.values() #Imprimimos los valores del diccionario
print(my_new_new_dict)
print(type(my_new_new_dict)) #Tipo dict_values