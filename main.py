# Loop através de um arquivo

with open('arquivoPessoas.txt', 'r') as f:
    # Ler o arquivo de uma vez só
    for linha in f.readlines():
        print(linha)
    f.close()
        
with open("arquivoPessoas.txt", "r") as meuArquivo:
    conteudo = meuArquivo.readlines()
    print(conteudo)  # Imprime o conteúdo do arquivo como uma lista de strings
    # Ler o arquivo linha por linha
    
    conteudo = meuArquivo.readline()
    print(conteudo)  # Imprime a primeira linha do arquivo


