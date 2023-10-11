### Listas (no es lo mismo que un array)###

my_list = list() # Forma 1
my_other_list = [] # Forma 2 (al final es lo mismo)

print(len(my_list)) # 0

my_list = [35, 24, 62, 30, 34]

print(my_list)

my_other_list = [34, 1.76, "Rafa", "Delgado"]

print(type(my_other_list))
print(type(my_list))

# Acceso a la lista
print(my_other_list[0]) # Primer elemento de la lista
print(my_other_list[-1]) # Último elemento de la lista, pero esto petaría en otros lenguajes
#print(my_other_list[8]) Esto da error porque no existe el elemento de la posición 8
print(my_list.count(62)) # Cuenta las coincidencias dentro de la lista, en este caso, 62 solo hay uno
age, height, name, surname = my_other_list
print(name) #Se asigna cada variable al valor que tiene la lista, obviamente, tienen que coincidir, sino peta