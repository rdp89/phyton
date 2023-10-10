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

# Formateo

name, surname, age = "Rafa", "Delgado", 34
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #Esta es la peor forma
print(f"Mi nombre es {name} {surname} y mi edad es {age}".format(name, surname, age))

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#División

language_slice = language[1:3] #yt
print(language_slice)

language_slice = language[1:] #ython
print(language_slice)

language_slice = language[0:6:2] #Muestre todas (0-6) pero con saltos de dos en dos
print(language_slice)

#Reverse

reversed_language = language[::-1] #nohtyP
print(reversed_language)

# Funciones

print(language.capitalize()) # Pone la primera en mayuscula
print(language.upper()) # Todo a mayuscula
print(language.count("t")) # Cuenta cuantas t, en este caso, hay en la palabra python
print(language.isnumeric()) #False
print("1".isnumeric()) # True
print(language.lower()) # Todo a minuscula
print(language.upper().isupper()) # True
print(language.startswith("py")) # True