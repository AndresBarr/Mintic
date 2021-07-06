def parqueadero_buses (Cbus,Nbus):
    Lote =Cbus/3
    
    if Cbus % 3 == 0:
        if Cbus > Nbus:
            if Lote >= Nbus :
                sal="Parquee en el lote 1"
            if Lote*2 >= Nbus >Lote:
                sal="Parquee en el lote 2"
            if Lote*3 >= Nbus >Lote*2:
                sal="Parquee en el lote 3"
        else:
            sal= 'El numero esta mal'
    else: 
        sal= 'La cantidad de buses no es multiplo de 3'
    return sal

print(parqueadero_buses(30,25))