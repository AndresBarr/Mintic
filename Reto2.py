def desempeño(operario:dict)->str:
    kms=operario['kms']
    bolsas=operario['bolsas']
    if kms > 25 and bolsas >= 600:
        Sal='Operario con alto desempeño'
    elif 15<=kms<=25 and 450<=bolsas<600:
        Sal='Operario con medio desempeño'
    else:
        Sal='Operario con bajo desempeño'
    return Sal
#Caso de prueba3
'''operario = {
    'id_operario':12345,
    'edad':35,
    'nombre':'Juan',
    'apellido':'Perez',
    'kms':30,
    'bolsas':601
}'''

#Caso de prueba2
'''operario = {
    'id_operario':12346,
    'edad':45,
    'nombre':'Carlos',
    'apellido':'Lopez',
    'kms':20,
    'bolsas':450
}'''

#Caso de prueba3
operario = {
    'id_operario':12347,
    'edad':55,
    'nombre':'Joaquin',
    'apellido':'marin',
    'kms':10,
    'bolsas':100
}

print(desempeño(operario))