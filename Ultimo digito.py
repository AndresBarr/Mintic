
def ultdig(num1,num2):
    ud1= num1-num1//10*10
    ud2= num2-num2//10*10
    
    if (ud1==ud2):
        print('Mismo digito')
    else:
        print('Diferente digito')
    


ultdig(3089,49090)