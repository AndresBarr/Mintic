def productocartesiano (lista1,lista2):
    respuesta= []
    for k in range(len(lista1)):
        for i in range(len(lista2)):
            respuesta.append((lista1[k],lista2[i]))
    return respuesta   

print(productocartesiano ([1,2,3],['a','b','c']))

print(productocartesiano (['a','b','c'],['x','y','z']))

print(productocartesiano ([1,2,3,4,5],['rojo','verde','azul']))