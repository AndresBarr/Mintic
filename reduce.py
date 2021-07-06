#ejercicio1
lista = [1,2,3,4]
acumulador = 0

for i in lista:
    acumulador+=i

print(acumulador)

from functools import reduce

lista=[1,2,3,4]

def funcion_acumulador (acumulador,elemento):
    return acumulador + elemento

resultado = reduce(funcion_acumulador,lista)
print(resultado)

#resultado=reduce(lambda acumulador,elemento:acumulador+elemento,lista)

#ejercicio2
from functools import reduce

lista=['python','java','Ruby','Elixir']
resultado = reduce(lambda acumulador,elemento:acumulador+'-'+elemento,lista)
print(resultado)

#ejercicio3
items=(1,4,5)
suma10=reduce (lambda x,y:x+y,items,10)
print(suma10)