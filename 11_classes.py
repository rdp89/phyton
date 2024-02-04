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
    def __init__(self, name, surname):
        self.fullname = f"{name} {surname}" #Creamos la propiedad de la clase fullname, asignandole el valor de los dos parámetros recibidos
    def walk(self):
        print(f"{self.fullname} está caminando") #También podemos crear una función dentro de la clase que haga algo

person_full = PersonFull("Rafa","Delgado")
print(person_full.fullname)

person_full.walk() #Mostrará el nombre de la persona que está caminando