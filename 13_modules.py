### Modules ###

#Solo podemos importar ficheros que empiecen por texto, no acepta números, como es nuestro caso

#import my_module

from my_module import sumar #Importamos en este caso la función concreta del fichero my_module.py en vez de todo el fichero como en el ejemplo de arriba comentado
sumar(2, 6, 5) #Accedemos a la función situada en el fichero my_module.py

#Podemos acceder a una función determinada también

from my_module import restar
restar(10, 5, 1)

#También podemos importarlo todo desde la misma linea: from my_module import sumar, restar

#Python tiene diferentes módulos para poder usar a nuestro gusto

import math

print(math.pi) #Número pi
print(math.pow(2, 8)) #Potencias

from math import pow as POTENCIA #Podemos importarlo con un alias para que nos resulte más amigable
print(POTENCIA(5, 2))