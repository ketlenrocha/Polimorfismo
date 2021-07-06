from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Moto import Moto
from Carro import Carro

veiculo = Veiculo("Ford", 4, "Logan", 40)
veiculo.imprimir ()
veiculo.acelerar(20)
veiculo.imprimir()
veiculo.frear(5)
veiculo.imprimir()

bicicleta = Bicicleta("Aro 26", 2, "Aro26", 5, 22, 2)
bicicleta.imprimir()

automovel = Automovel("Citroen" , 4, "C3", 15, "1.0 turbo")
automovel.imprimir()

moto = Moto("Honda",2,"160 Fan",75, "19,8 CV", "contem" )
moto.imprimir()
carro = Carro("Chevrolet" , 4, "Cruze", 40, "1.2 turbo", "5")
carro.imprimir()




