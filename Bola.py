class Bola:
    def __init__(self, cor, tamanho, direcao):
        self.cor = cor
        self.tamanho = tamanho
        self.direcao = direcao
    
    def __str__(self):
        msg = "Ola, eu sou uma " + self.tamanho + " bola da cor " + self.cor
        return msg

    def quicar(self):
        if self.direcao == "Para Baixo":
            self.direcao = "Para cima"

minhaBola = Bola("verde", "pequena", "Para baixo")
print(minhaBola)



