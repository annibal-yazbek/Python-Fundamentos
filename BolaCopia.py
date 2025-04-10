class Bola:

    def quicar(self):
        if self.direcao == "Para Baixo":
            self.direcao = "Para cima"

minhaBola = Bola()

minhaBola.direcao = "Para Baixo"
minhaBola.cor = "verde"
minhaBola.tamanho = "pequena"

print("Nos criamos uma bola")
print("O tamanho da bola e: ", minhaBola.tamanho)
print("A cor da bola e: ", minhaBola.cor)
print("A direção da bola e: ", minhaBola.direcao)
print("Agora vamos quicar a bola. \n")
minhaBola.quicar()
print("Agora a direcao da bola e: ", minhaBola.direcao)
