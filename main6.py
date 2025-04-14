# Loop através de um arquivo

with open('arquivoPessoas.txt', 'r') as f:
    # Ler o arquivo de uma vez só
    for linha in f.readlines():
        print(linha)
    f.close()
        
with open("arquivoPessoas.txt", "r") as meuArquivo:
    conteudo1 = meuArquivo.readlines()
    print(conteudo1)
    
    for linha in conteudo1:
        print(linha, end = '')
        

    conteudo2 = meuArquivo.readline()
    print(conteudo2)  # Imprime a primeira linha do arquivo


