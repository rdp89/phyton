### Classes ###

class MyEmptyPerson:
    pass #Clase vacía, para que no de error mientras definimos una clase

class Person:
    def __init__(self, name, surname):
        self.name = name #Asignamos a la propiedad self.name (lo hemos llamado así, se podría llamar self.nombre o self.huerto) el valor del parámetro
        self.surname = surname

my_person = Person("Rafael", "Delgado")
print(my_person.name) #Rafael
print(my_person.surname) #Delgado

#Ahora con formato
print(f"{my_person.name} {my_person.surname}")

#Ahora algo más complejo y más práctico

class PersonFull:
    def __init__(self, name, surname, alias="sin alias"):
        self.fullname = f"{name} {surname} ({alias})" #Creamos la propiedad de la clase fullname, asignandole el valor de los dos parámetros recibidos y el alias por defecto opcional
    def walk(self):
        print(f"{self.fullname} está caminando") #También podemos crear una función dentro de la clase que haga algo

person_full = PersonFull("Rafa","Delgado", "Alias RDP89")
my_other_person = PersonFull("Rafa", "Delgado") #Esta vez sin alias
print(person_full.fullname)
print(my_other_person.fullname)

person_full.walk() #Mostrará el nombre de la persona que está caminando
my_other_person.walk() #Lo mismo pero con alias

#Podemos asignarle un valor directamente así:

my_other_person.fullname = "Spaguetti de Carboeira alias Portimao"

print(my_other_person.fullname)

#Hay que recordar que a python se la pela el tipado por lo que podemos asignarle un número así sin más:

my_other_person.fullname = 656

print(my_other_person.fullname)

#Podemos privatizar una propiedad de una clase y acceder a ella con una función (getter)

class PersonPrivate:
    def __init__(self, name, surname, alias="sin alias"):
        self.fullname = f"{name} {surname} ({alias})"
        self.__name = name #Aquí lo privatizamos con dos guiones bajos
    def get_name(self):
        return self.__name
    
private_person = PersonPrivate("Nombre privado", "apellido público")
print(private_person.get_name()) #Mostramos el nombre pero no lo podemos modificar:

private_person.__name = "Lo que quiera" #Esto no hace nada

print(private_person.get_name()) #Esto va a seguir mostrando el nombre privado