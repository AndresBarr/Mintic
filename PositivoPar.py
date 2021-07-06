print ("Teclea un numero")
num = int(input())
if num < 0:
    print("El número debe ser positivo")
else:
    if int(num/2)*2 ==num:
        print("El número es par")
    else:
         print("El número no es par")