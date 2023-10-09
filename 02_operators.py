### Operadores aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2) # Resto
print(10 // 3) # División para redondear el resultado
print(2 ** 3) #Exponente
print(2 ** 3 + 3 - 7 / 1 // 4)
print("Hola " + " Python") #En este caso se concatena
print("Hola " + str(5)) # Convertimos el entero 5 en texto y así se concatena, de lo contrario no
print("Hola " * 5)

# print("Hola" * 2.5 * 2) esto da error
my_float = 2.5 * 2 #5.0
print("Hola " * int(my_float)) #Imprimirá 5 veces hola también ya que lo hemos convertido a int

### Operadores comparativos ###

print(3 > 4) # False
print(3 < 4) # True
print(3 <= 4) # True
print(3 >= 4) # False
print(3 == 4) # False
print(3 != 4) # True
print(3 == 3 >= 3) # True

# Con cadenas también (Ordenación alfabética por ASCII)

print("Hola" > "Python")
print("Hola" < "Python")
print(len("Hola") == len("Pyth")) #Aqui compara longitud de caracteres
print("Hola" != "Python")

### Operadores lógicos ###

print(3 > 4 and "Hola" > "Python") #False
print(3 > 4 or "Hola" > "Python") #False
print(3 < 4 or "Hola" > "Python") #True
#print(3 > 4 not "Hola" > "Python") así no funciona
print(not(3 > 4)) #Se hace así, da lo contrario, en este caso true not(false)