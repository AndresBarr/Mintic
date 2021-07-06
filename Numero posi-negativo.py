
num= int(input('escriba un numero '))
if num > 0:
    print('El numero es positivo')
    if 10 <= num <= 99:
        print ('El numero tiene 2 digitos')
    else:
        print ('El numero no tiene 2 digitos')
else:
    print('El numero es negativo')
    if -100 <= num <= -999:
        print ('El numero tiene 2 digitos')
    else:
        print ('El numero no tiene 2 digitos')
