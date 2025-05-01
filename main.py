# trabalhando com arquivos no SO

import os
# abir o arquivo no modo write cria o arquivo vazio caso não exista
file = open("teste.txt", "w")
file.close()

# renomeando o arquivo
os.rename("teste.txt", "teste_renomeado.txt")

# verificando se o arquivo existe   
if os.path.exists("teste_renomeado.txt"):
    print("O arquivo existe")
else:
    print("O arquivo não existe")   
    


