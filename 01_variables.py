# Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:",my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Rafa", "Delgado", "RDP89", 34
print("Me llamo:",name,surname,"y tengo:",age,"años. Y mi alias es:",alias)

# Inputs

first_name = input("What's your name?: ")
age = input("How old are you?: ")

print(first_name)
print(age)

# Cambiamos su tipo

first_name = 34
age = "Rafa"

#Forzamos tipado ¿?
address: str = "Mi dirección" # Solo indicamos que nos gustaría que fuese tipo string ya que python es un lenguaje de tipado flojo
address = 32
print(address)