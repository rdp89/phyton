### Loops ###

# while

my_condition = 0
while my_condition <= 10:
    print(my_condition)
    my_condition = my_condition + 1 #my_condition += 1 también se puede usar
else: #Es opcional
    print("my_condition es mayor que 10") #Esto no lo tienen todos los lenguajes, un else dentro de un while

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break #Palabra reservada para detener inmediatamente un bucle

print("La ejecución continúa")

# for

my_list = [35, 24, 62, 30, 34]

for element in my_list:
    print(element)

my_tuple = (35, 1.76, "Rafa", "Delgado")

for element in my_tuple:
    print(element)

my_set = {"Rafael", "Delgado", 34}

for element in my_set:
    print(element)

my_dict = {
    "Nombre":"Rafa",
    "Apellido":"Delgado",
    "Edad":34,
    "Lenguajes": {"Python","Swift","JavaScript"},
    1:1.76
    }

print("Bucle for con indices de my_dict")
for element in my_dict:
    print(element) #Imprime las keys (índices)
    if element == "Edad":
        break #Aquí se rompe el bucle cuando llega al indice edad
    elif element == 1:
        print("El índice vale 1") #Aquí no va a llegar nunca porque el índice Edad está antes que 1

print("Bucle for con los valores de my_dict")
for element in my_dict.values():
    print(element) #Aquí imprimimos los valores (values)
else:
    print("El bucle for ha finalizado")

print("Bucle for con indices de my_dict con un continue")
for element in my_dict:
    print(element) #Imprime las keys (índices)
    if element == "Edad":
        continue #Es lo contrario que break, la ejecución sigue adelante volviendo a empezar el for con el siguiente elemento
    elif element == 1:
        print("El índice vale 1") #Aquí no va a llegar nunca porque el índice Edad está antes que 1