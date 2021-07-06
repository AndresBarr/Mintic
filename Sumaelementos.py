lista = [[1,2,3,4,5],[6,7,8,9,10]]
for k in range (len(lista)):
    suma=0
    for x in range (len(lista[k])):
        suma=suma+lista[k][x]
    print(suma)
    