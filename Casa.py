class Casa:
    #metodo constructor
    def __init__(self, color, tamano):
        self.color = color
        self.tamano = tamano
        self.consumo_energia = 0
        self.consumo_agua = 0

    def tocar_timbre(self):
        print('Aca estoy gastando energia con el timbre')
        self.consumo_energia +=10
    
    def abrir_ducha(self):
        print('Aca abri la ducha')
        self.consumo_agua += 1

#herencia Oficina<-- Casa
class Oficina(Casa):
    
    def tocar_timbre(self):
        print('Aca estoy gastando energia con el timbre en oficina')
        self.consumo_energia +=20

    def abrir_ducha(self):
        print('Aca abri la ducha en oficina')
        self.consumo_agua += 15


mi_casa = Casa('rojo', 10)
mi_casa.area = 100
print('area:',mi_casa.area)

print('uso de getattr')
print(getattr(mi_casa, 'area'))

print(mi_casa.color)
print(mi_casa.tamano)
mi_casa.tocar_timbre()
mi_casa.tocar_timbre()
print(mi_casa.consumo_energia)
mi_casa.abrir_ducha()
mi_casa.abrir_ducha()
print(mi_casa.consumo_agua)

mi_oficina = Oficina('Blanca', 50)
print('Oficina: ', mi_oficina.color, mi_oficina.tamano)
mi_oficina.tocar_timbre()
print(mi_oficina.consumo_energia)
mi_oficina.abrir_ducha()
print(mi_oficina.consumo_agua)



#mi_casa2 = Casa('verde', 20)
#print(mi_casa2.color)
#print(mi_casa2.tamano)