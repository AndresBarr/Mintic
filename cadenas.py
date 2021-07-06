'''fruta= 'fresa'
print(fruta[-1])
print(fruta[-2])
print(fruta[-3])
print(fruta[-4])
print(fruta[-5])
print(fruta[0])
print(fruta[1])
print(fruta[2])
print(fruta[3])
print(fruta[4])
print(fruta[:])

saludo = '¡Hola, mundo!'
nuevo_saludo = 'J' + saludo[0:]
print(nuevo_saludo)


print('resa' in 'fresa' )



palabra = 'arroz'

if palabra < 'banana':
    print('Tu palabra,' + palabra + ', viene antes de banana')
elif palabra > 'banana':
    print('Su palabra,' + palabra + ', viene después de banana.')
else:
    print('Está bien, su palabra es banana')

palabra = 'andRes'
palabra_nueva =  palabra[:1].upper()+palabra[1:].lower()
print(palabra_nueva)

palabra1 = 'banana'
index = palabra1.count('na')
print(index)

palabra1 = 'banana'
index = palabra1.find('na',3)
print(index)

linea = '        Aquí vamos            '
print(linea.strip())


data = 'De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
enlaposicion = data.find(' ')
print(enlaposicion)

espacioenlaposicion = data.find(' ',enlaposicion+1)
print(espacioenlaposicion)

host = data[enlaposicion+1:espacioenlaposicion]
print(host)

print (r'hola\nbors')
print ('hola\nbors')

cadena = "un uno, un dos, un tres"

print (cadena.replace("un", "UN"))        
print (cadena.replace("un", "UN", 4))'''

# saca "El valor es 12
print ("El valor es {}".format(12))

# saca "El valor es 12.3456
print ("El valor es {}".format(12.3456))

# Tres conjuntos {}, el primero para el primer parámetro de format(), el segundo para el segundo
# y así sucesivamente.
# saca "Los valores son 1, 2 y 3"
print ("Los valores son {}, {} y {}".format(1,2,3))

# Entre las llaves podemos poner la posición del parámetro. {2} es el tercer parámetro de format()
# {0} es el primer parámetro de format.
# saca "Los valores son 3, 2 y 1"
print ("Los valores son {2}, {1} y {0}".format(1,2,3))