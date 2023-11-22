### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Rafael","Delgado",34}
print(type(my_other_set)) #Como le hemos metido datos, ahora es un set xD

print(len(my_other_set))

my_other_set.add("RDP89")
print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add(1.76) 
my_other_set.add("Rafael") #Un set no admite repetidos, si añadiésemos otro dato igual no lo admimitiria
print(my_other_set)

#Comprueba si existe ese dato en el set y devuelve:
print("Pedro" in my_other_set) #False
print("Rafael" in my_other_set) #True

#Borramos el elemento Rafael 
my_other_set.remove("Rafael")
print(my_other_set)

my_other_set.clear() #Borramos todos los datos del set
print(len(my_other_set)) #0

del my_other_set #Lo borramos directamente con del

my_set = {"Rafael", "Delgado", 34}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"JavaScript", "Java", "Python"}

my_new_set = my_set.union(my_other_set) #Une los valores no repetidos del otro set
print(my_new_set)

my_new_set = my_new_set.union({"HTML xD"}) #Le añadimos un valor nuevo con union
print(my_new_set)

print(my_new_set.difference(my_set)) #Extrae los valores que coinciden con my_set de my_new_set