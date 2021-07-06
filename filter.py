
#ejemplo 1
def mayor_A_cinco (elemento):
    return elemento > 5

tupla= (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
resultado= list(filter(mayor_A_cinco,tupla))
resultado= len(resultado)
print (resultado)

#resultado2= list(filter(lambda x:x>5,tupla))
#print(len(resultado2))

#ejemplo 2

items=[1,2,3,4,4,5,6,6,7,7,8,6,4,3,3,43,4,34,3]

pares=[]
for i in items:
    if i%2==0:
        pares.append(i)
print (pares)        


#pares1= list(filter(lambda x:x%2==0,items))
#print(pares1)