# trabalhando com arquivos
# meuArquivo = open('meuArquivo.txt, 'r')

with open('meuArquivo.txt') as meuArquivo:
    conteudo = meuArquivo.read()
    print(conteudo)

with open('meuArquivo.txt', 'r') as meuArquivo:
    conteudo = meuArquivo.readlines()
    print(conteudo)

with open('meuArquivo.txt', 'r') as meuArquivo:
    conteudo = meuArquivo.readline()
    print(conteudo)
    