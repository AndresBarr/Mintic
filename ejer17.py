#escriba un numero de 4 digitos, y diga cuantos digitos son pares
x=input() 

x_str=str(x)

x1=x_str[0]
x2=x_str[1]
x3=x_str[2]
x4=x_str[3]

x1int= int(x1)
x2int= int(x2)
x3int= int(x3)
x4int= int(x4)


x_1=x1int % 2
x_2=x2int % 2
x_3=x3int % 2
x_4=x4int % 2

if x_1 == 0:
    y_1='Par'
    z_1=x1int
else:
    y_1='no'
    z_1=0
if x_2 == 0: 
    y_2='Par'
    z_2=x2int
else:
    y_2='no'
    z_2=0
if x_3 == 0: 
    y_3='Par'
    z_3=x3int
else:
    y_3='no'
    z_3=0
if x_4 == 0: 
    y_4='Par'
    z_4=x4int
else:
    y_4='no'
    z_4=0

z= z_1+z_2+z_3+z_4

y=y_1+y_2+y_3+y_4

if y.count('Par') == 4:
    print('Todos son pares')
if y.count('Par') == 3:
    print('3 son pares')
if y.count('Par') == 2:
    print('2 son pares')
if y.count('Par') == 1:
    print('1 es par')
if y.count('Par') == 0:
    print('Todos son impares')

print('La suma de los numeros pares es:',z)