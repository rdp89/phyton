### Functions ###

def my_function():
    print("Esto es una función")

my_function()

def generate_full_name():
    first_name = 'Rafael'
    last_name = 'Delgado'
    space = ' '
    full_name = first_name + space + last_name
    return full_name #Esta función devuelve el nombre completo
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total #Devuelve la suma de los números establecidos
print(add_two_numbers())

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings('Rafa')) #Llamamos a la función pasándole el nombre con el que queremos que nos salude

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    #area = int(area) #Pasamos a entero el valor decimal
    return area
print(area_of_circle(10)) #Nos calcula el area de círculo pasándole a la función como parámetro el valor del radio
print(area_of_circle(4))

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Rafael','Delgado')) #LLamamos a la función para que nos muestre nuestro nombre completo

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Edad:', calculate_age(2024, 1989)) #Llamamos a la función para que nos calcule nuestra edad

#Ahora vamos a asegurarnos que le pasamos el valor correcto a las funciones con índice y valor

print('Nombre completo sin importar el orden:',generate_full_name(last_name ='Delgado', first_name='Rafa')) #Aquí no importa el orden en el que pongamos nuestros argumentos

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # Si es par devuelve True
print(is_even(7)) # Si no es par devuelve False

#Valor por defecto para una función
def greetings (name = 'Oooh!'): #Si no le pasamos ningún parámetro, por defecto nos mostrará lo establecido
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings()) #Sin argumento nos mostrará oooh!
print(greetings('Rafa'))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon

#Funciones con un arbitrario número de parámetros

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # A la variable total se le va sumando todos los parámetros que le pongamos
    return total
print(sum_all_nums(20, 3, 5)) # 10

def generate_groups(equipo, *miembros):
    print(equipo)
    for i in miembros:
        print(i) 
generate_groups('Equipo actimel:','Rafa','Leti','Jesús','Eva')