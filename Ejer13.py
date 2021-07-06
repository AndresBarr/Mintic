# Leer un número entero menor que 50 y positivo y determinar si es un número primo.

def primo(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def Nprimos(num1,num2):
    cont=0
    for i in range(num1,num2):
        if primo(i) == True:
            cont += 1
    print(cont)    

Nprimos(1,15)








