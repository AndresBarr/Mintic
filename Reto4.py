def palindrome(lista):
    lista1= list(map(lambda x:(''.join(reversed(x))), lista))
    result=[i for i, j in zip(lista, lista1) if i == j]
    return result

print(palindrome(['ara','tos','sometemos']))

print(palindrome(['rule','geeks','geeg','keek','practice','ara','pencil']))

print(palindrome(['mom','civic','elevator','madam','rotator','wow']))

print(palindrome(['kayak','level','racecar','noon','testser']))