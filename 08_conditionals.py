### Conditionals ###

#Como dato importante, cuando dentro de un if metemos una condición, siempre espera un valor booleano, es decir, true o false

my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")

my_condition = 7 * 3

if my_condition == 10:
    print("Se ejecuta la condición del if que vale 10") #Se ejecuta si es igual a 10
else:
    print("Se ejecuta si no es igual a 10") #Se ejecuta en cualquier otro caso diferente a 10

if my_condition > 5 and my_condition < 20:
    print("Se ejecuta si cumplen las dos condiciones")
    print("Se ejecuta si cumplen las dos condiciones")
    print("Se ejecuta si cumplen las dos condiciones")
    print("Se ejecuta si cumplen las dos condiciones")
    print("Se ejecuta si cumplen las dos condiciones")


    print("Se ejecuta si cumplen las dos condiciones") #Todo esto se ejecuta mientras este tabulado (si se cumple la condición, claro está)

elif my_condition == 21:
    print("Si llega aquí, es que my_condition vale exactamente 21")

texto = "Mi cadena de texto" #True si no está vacía, false si está vacía

if texto:
    print("Mi cadena de texto no está vacía")

if texto == "Mi cadena de texto":
    print("Es igual y no está vacía")

print("La ejecución continúa")