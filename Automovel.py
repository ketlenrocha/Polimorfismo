from Veiculo import Veiculo

class Automovel (Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaMotor):
        
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        
        self.potenciaMotor = potenciaMotor
       

    def imprimir (self):
        print (f" Marca: {self.marca}    Quantidade de rodas: {self.qtdRodas} Modelo: {self.modelo}       Velocidade Inicial: {self.velocidade}km/h   Potência do motor: {self.potenciaMotor}")
