#ejemplo1 
def cuadrado (x):
    return x * x

lista=[1,2,3,4,5,6,7,8,9,10]
resultado = list(map(cuadrado,lista))


print(resultado)
#resultado = list(map(lambda x:x * x, lista))


#ejemplo2

from math import pow #pow es una funcion que se encuentra en math donde se ingresa base y exponente

numeros = [2,3,4]
Potencias = [3,2,4]

potenciados = list(map(pow,numeros,Potencias))
print (potenciados)
