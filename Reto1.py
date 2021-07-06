def escobita(id,mes1,mes2,mes3,mes4,mes5,mes6):
    prom= float (mes1+mes2+mes3+mes4+mes5+mes6)/6
    promformat= '{0:.2f}'.format(prom) 
    
    if prom>=25 and prom<=50:   
        salida= "de acuerdo con tu promedio: Buen trabajo!!"
    if prom>1 and prom<25:  
        salida= "de acuerdo con tu promedio: Debes intentar mejorar tu desempenio"
    if prom<1: 
        salida= "de acuerdo con tu promedio: Debes ingresar numeros positivos"
    return "El promedio mensual de kilometros de barrido del escobita {}, es: {}, {}".format(id,promformat,salida)        

print("\nCaso de prueba 1:")
print(escobita(12345,20,28,27,30,18,32))

print("Caso de prueba 2:")
print(escobita(67890,50,30,22,29,42,49))

print("Caso de prueba 3:")
print(escobita(11111,-1,-1,-1,-1,-1,-1))


