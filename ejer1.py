
cadena= "Hola como estas"
lista=cadena.split()
print(lista)
y= []
for x in lista:
    y.append(len(x))
print(y)


cadena1='Mi hermano como te ha ido'
lista1=cadena1.split()

lista2 = list(map(len,lista1))
print (lista2)