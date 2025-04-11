# polimorfismo e herança

class Carro:
    def __init__(self, marca, modelo, ano): 
        self.marca = marca      
        self.modelo = modelo
        self.ano = ano
        self.km = 0


    def geraNomeCarro  (self):
        fullName = f"{self.marca} {self.modelo} {self.ano}"
        return fullName

    def getKm(self, km):
        print(f"Este carro já rodou {self.km} km.")

    def atualizaKm(self, kmrodado):
        if kmrodado >= self.km:
            self.km = kmrodado
        else:
            print("Nao pode resetar kilometragem") 

    def addKm(self, kmrodado):
        self.km = self.km + kmrodado


class carroEletrico(Carro):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.ah = 75

    def descricaoBateria(self):
        print(f"Este carro tem {self.ah} Ah de bateria.")


    

meuCarro = Carro("Ford", "Fusion", 2021)
meuCarroEletrico = carroEletrico("Tesla", "Model S", 2022)
print(meuCarroEletrico.geraNomeCarro())
meuCarroEletrico.descricaoBateria()



    