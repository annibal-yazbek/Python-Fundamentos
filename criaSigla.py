# Criar Siglas
def criaSigla(mensagem):
    result = ""
    words = mensagem.split()
    for word in words:
        result += word[0].upper()
    return result

print(criaSigla("Universal Serial Bus"))
print(criaSigla("Central Processing Unit"))
print(criaSigla("Graphics Interchange Format"))
print(criaSigla("World wide web"))
print(criaSigla("local area network"))
