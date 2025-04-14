# Trabalhando com enumerate
with open('frasesFamosas.txt', 'r') as f:
    for linhas in enumerate(f.readlines()):
        if linhas[0] % 2 == 0:
            print(linhas[1], end = '')
        else:
            print(' ' + linhas[1])


    