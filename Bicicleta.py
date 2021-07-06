from Veiculo import Veiculo

class Bicicleta (Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro):
        
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimir (self):
        print (f" Marca: {self.marca}     Quantidade de rodas: {self.qtdRodas} Modelo: {self.modelo}    Velocidade Inicial: {self.velocidade} km/h Marchas: {self.numMarchas}  Bagageiro: {self.bagageiro}")
