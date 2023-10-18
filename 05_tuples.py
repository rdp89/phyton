### Tuples ###

my_tuple = tuple() #Se define de esta forma
my_other_tuple = () # O de esta forma

my_tuple = (35, 1.76, "Rafa", "Delgado")
my_other_tuple = (1, 2, 3, 4, 5, 6, 7)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple.count("Delgado")) #Cuenta las coincidencias que le pasemos como parámetro
print(my_tuple.index("Delgado")) #Nos devuelve el índice de la coincidencia

#my_tuple[1] = 1.80 Esto no se puede hacer, las tuplas son inmutables

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6]) #Mostrar un rango de valores de la tupla, primer valor se muestra hasta el valor último que este no se muestra, es decir, se van a mostrar los valores de los índices 3, 4 y 5

#Las tuplas están pensadas para ser inmutables, si queremos que se puedan modificar, para eso están las listas, podemos transformarla:

my_tuple = list(my_tuple) #Aquí ya es una lista
print(type(my_tuple))

#Ya podemos modificarla
my_tuple.insert(1, 1.82) 
del my_tuple[2]
print(my_tuple)

#Volvemos a transformarla en tupla
my_tuple = tuple(my_tuple)

print(type(my_tuple))
print(my_tuple)

#del my_tuple[2] No se pueden borrar valores dentro de índices en las tuplas
del my_tuple #Eliminamos la tupla