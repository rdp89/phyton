### Exceptions Handling ###

numberOne = 10
#numberTwo = 20
numberTwo = "20"

#try except
try:
    print(numberOne + numberTwo) #Intentamos sumar un int y un string
    print("No se ha producido error")
except:
    print("Se ha producido un error, cambia el tipo de la variable a tipo int") #Aquí llega si se produce la excepción

#try except else
    
try:
    print(numberOne + numberTwo) #Intentamos sumar un int y un string
    print("No se ha producido error")
except:
    print("Se ha producido un error, cambia el tipo de la variable a tipo int")
else: #Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")

#try except else finally
try:
    print(numberOne + numberTwo) #Intentamos sumar un int y un string
    print("No se ha producido error")
except:
    print("Se ha producido un error, cambia el tipo de la variable a tipo int")
else: #Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: #Se ejecuta siempre, pase lo que pase
    print("La ejecución continúa") #Tanto el else como el finally son opcionales
    
#Captura de excepciones por tipo
    
try:
    print(numberOne + numberTwo) #Intentamos sumar un int y un string
    print("No se ha producido error")
except ValueError:
    print("No se ha producido error tipo ValueError")
except TypeError:
    print("Se ha producido un error tipo TypeError")

#Captura de la información de la excepción
try:
    print(numberOne + numberTwo) #Intentamos sumar un int y un string
    print("No se ha producido error")
except Exception as mierror: #Como variable (la podemos llamar como queramos sin usar palabras reservadas) podemos mostrar con un print los detalles del error
    print(f"Se ha producido un error tipo TypeError, los detalles del error son los siguientes: {mierror}")