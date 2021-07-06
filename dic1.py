mi_diccionario = dict()
for y in range(3, 11):
    mi_diccionario[(y, y**3)] = []
    for x in range(4, 31, 2):
        if x%y == 0:
            mi_diccionario[(y, y**3)].append(x**2)

print(mi_diccionario)

#mi_diccionario = { (x, x**3) : [ y**2 for y in range(4,31,2) if y%x == 0 ] for x in range(3, 11) }
#print(mi_diccionario)