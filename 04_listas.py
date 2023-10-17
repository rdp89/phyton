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

#Asignación manual
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

#Se pueden concatenar listas
print(my_list + my_other_list)

#Añadir elementos a una lista con append()

my_other_list.append("Devops")
print(my_other_list)

#Insertar con insert() en la posición elegida, se desplazan los elementos de la lista
my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list.remove("Azul") #Eliminamos por coincidencia del valor (Si tenemos dos borra el primero)
print(my_other_list)


print(my_other_list) 
print(my_other_list.pop()) #Elimina el último elemento de la lista y nos devuelve el valor que ha borrado

print(my_other_list)
my_pop_element = my_other_list.pop(2) #Guardamos el valor que vamos a borrar
print(my_other_list.pop(2)) #Le pasamos el índice del elemento de la lista que queremos borrar

del my_list[2] #Con esto borramos sin más el índice 2 de la lista (pide el índice)

my_new_list = my_list.copy() #Copiamos la lista anterior en una nueva lista con copy()

print(my_new_list)
my_new_list.reverse() #Le da la vuelta a los valores de la lista
print(my_new_list)

my_new_list.sort() #Ordena los elementos de la lista, como son int, los ordena de menor a mayor

print(my_new_list[0:2]) #Sublistas, va a mostrar lo que hay entre esos dos índices, sin incluir éstos

my_list.clear() #Con esto borramos todos los elementos de la lista (la limpiamos)