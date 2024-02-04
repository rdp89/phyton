### Funciones ###

def my_function():
    print("Esto es una función")

my_function()
my_function() #Podemos llamar a la función las veces que queramos sin tener que repetir código

def sum_two_values(first_value, second_value): #Esta función pide dos valores
    print(first_value + second_value) #Sumamos los dos números y lo imprimimos

sum_two_values(5,3) #Suma de enteros

sum_two_values("6","3") #Aquí lo coge como texto, con lo cual, lo concatena, hay que tener en cuenta que no podemos restart ni dividir cadenas xDDDDD

sum_two_values(4.5, 3.2) #Podemos pasarle cualquier tipo de dato, se lo come igualmente


def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value #Nos retorna un valor o salida

total = sum_two_values_with_return(10, 5)
print(total)
print(sum_two_values_with_return(10, 5)) #Podemos imprimir directamente la llamada de la función y el retorno del valor

def print_name(name, surname):
    print (f"{name} {surname}")

print_name("Delgado", "Rafa")

print_name(surname="Delgado", name="Rafa") #Podemos forzar a que lo muestre en el orden correcto a pesar de ponerselo al revés

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Rafa", "Delgado", "RDP89")
print_name_with_default("Rafa","Delgado") #No estamos obligados a poner alias, ya que le hemos puesto un valor por defecto, en caso de no pasarle nosotros uno

#Ahora vamos a definir una función cuyos parámetros pueden ser uno o varios, no se define el número concreto (dinámico)
def print_texts(*texts):
    print(texts)

print_texts("Hola", "Python", "RDP89")
print_texts("RDP89") #Podemos mandar todos los parámetros que queramos

def print_texts_mayusculas(*texts):
    for text in texts: #Podemos meter nuestro bucle for dentro de la función e iterar dichos parámetros
        print(text.upper()) #Convertimos la salida en mayuscula

print_texts_mayusculas("Hola", "Python", "RDP89")