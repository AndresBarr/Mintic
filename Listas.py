'''lista = [1, 2.5, 'DevCode', [5,6] ,4]

print(lista[0]) # 1
print(lista[1]) # 2.5
print(lista[2]) # DevCode
print(lista[3]) # [5,6]
print(lista[3][0]) # 5
print(lista[3][1]) # 6
print('Hicimos este cambio ->',lista[1:4]) # [2.5, 'DevCode',[5,6]]
print(lista[1:6]) # [2.5, 'DevCode', [5, 6], 4]
print(lista[1:6:2]) # [2.5, [5, 6]]
print("Hola Estructura de Lenguajes")'''

preguntas = ['nombre', 'objetivo', 'sistema operativo']
respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']

for pregunta, respuesta in zip(preguntas, respuestas):
    print('¿Cual es tu {0}?, la respuesta es: {1}.'.format(pregunta, respuesta))