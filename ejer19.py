#  A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. Si la
#cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% para las
#horas extras. Calcular el salario del trabajador dadas las horas trabajadas y la tarifa
#ingresadas por el usuario

print('Digite las horas trabajadas')
x=int(input())
print('Digite cuanto gana por hora')
y=int(input())

if x <= 40:
    print('El salario de esta semana es:{} $'.format(x*y))
else:
    z= (40*y)+1.5*y*(x-40)
    print('El salario de esta semana es:{} $'.format(z))