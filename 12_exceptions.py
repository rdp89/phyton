### Exceptions Handling ###

numberOne = 10
numberTwo = "20"

try:
    print(numberOne + numberTwo) #Intentamos sumar un int y un string
    print("No se ha producido error")
except:
    print("Se ha producido un error, cambia el tipo de la variable a tipo int")