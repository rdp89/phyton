### Strings ###

my_string = "Mi String"
my_other_string = 'Mi String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \ncon salto de línea"

print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"

print(my_tab_string)

my_scape_string = "\\Este es un string escapado poniendo caracteres especiales \\n"

print(my_scape_string)

#Formateo

name, surname, age = "Rafa", "Delgado", 34
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #Esta es la peor forma
print(f"Mi nombre es {name} {surname} y mi edad es {age}".format(name, surname, age))