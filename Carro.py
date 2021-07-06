from Automovel import Automovel

class Carro (Automovel):
    def __init__ (self, marca, qtdRodas, modelo, velocidade, potenciaMotor, qtdPortas):
        
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaMotor)
        
        self.qtdPortas = qtdPortas

    def imprimir (self):
        print (f" Marca: {self.marca}  Quantidade de rodas: {self.qtdRodas} Modelo: {self.modelo}    velocidade inicial é {self.velocidade}km/h Potência do carro: {self.potenciaMotor} Quantidade de Portas: {self.qtdPortas}")