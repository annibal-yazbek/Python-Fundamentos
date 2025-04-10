class Bife:
    def __init__(self):
        self.nivel_cozimento = 0
        self.descricao_cozimento = "Cru"
        self.temperos = []
    
    def __str__(self):
        msg = "Seu Bife " + self.descricao_cozimento
        if len(self.temperos) > 0:
            msg = msg + " com "
        for i in self.temperos:
            msg =  msg + i + ", "
        msg = msg.strip(", ")
        msg = msg + "."
        return msg    

    def adicionaTemperos(self, tempero):
        self.temperos.append(tempero)

    def cozinhar(self, tempo):
        self.nivel_cozimento = self.nivel_cozimento + tempo
        if self.nivel_cozimento > 8 :
           self.descricao_cozimento = "Torrado"
        elif self.nivel_cozimento > 5:
            self.descricao_cozimento = "Bem Passado"
        elif self.nivel_cozimento > 3:
            self.descricao_cozimento = "Ao Ponto"
        else:
            self.descricao_cozimento = "Cru"

print("Vamos Cozinhar")

meuBife = Bife()
meuBife.adicionaTemperos("Cebola")
meuBife.adicionaTemperos("Maionese")
meuBife.cozinhar(4)
meuBife.cozinhar(1)
meuBife.cozinhar(1)
meuBife.cozinhar(1)
meuBife.cozinhar(1)
meuBife.cozinhar(1)

print(meuBife)


