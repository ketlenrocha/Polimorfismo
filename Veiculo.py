class Veiculo ():
    def __init__ (self, marca = None, qtdRodas = 0, modelo = None, velocidade = 0):
        
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade
    
    def imprimir (self):
        print (f" Marca: {self.marca}       Quantidade de rodas: {self.qtdRodas} Modelo: {self.modelo}    Velocidade: {self.velocidade}km/h")
        
   
    def acelerar (self, velocidadeAtual):
        self.velocidade += velocidadeAtual

    def frear (self, velocidadeAtual):
        self.velocidade -= velocidadeAtual
        