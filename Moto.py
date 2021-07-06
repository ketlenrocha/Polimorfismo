from Automovel import Automovel

class Moto (Automovel):
    def __init__ (self, marca, qtdRodas, modelo, velocidade, potenciaMotor, partidaEletrica):
        
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaMotor)
        
        self.partidaEletrica = partidaEletrica

    def imprimir (self):
        print (f" Marca: {self.marca}      Quantidade de rodas: {self.qtdRodas}  Modelo: {self.modelo} Velocidade Inicial: {self.velocidade} km/h Potência Motor: {self.potenciaMotor} Partida Elétrica: {self.partidaEletrica}")
