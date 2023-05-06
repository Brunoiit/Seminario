class Coche:
    #atributos
    ruedas = 4
    color = ''
    aceleracion=0
    velocidad=0
    puertas=0

    #metodo constructor
    def __init__(self, color, aceleracion):
        #con self se llama al de afuera
        self.color=color
        self.aceleracion=aceleracion
        self.velocidad=0

    def acelerar(self):
        self.velocidad+=self.aceleracion
        return self.velocidad
    
class CocheVolador(Coche): #HERENCIA
    #atributos
    alas=False
    ruedas=6

    def __init__(self, color, aceleracion, estaVolando=False):
        super().__init__(color, aceleracion)
        self.estaVolando=estaVolando

    def vuela(self):
        self.estaVolando=True
        return "Estoy Volando"
    
#llamar objetos
c1=Coche('rojo', 20)
print(c1.color, " ", c1.acelerar())

#llamar auto volador
cv1=CocheVolador('negro', 600)
print(cv1.color)
print(cv1.vuela())
print(cv1.acelerar())