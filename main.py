# carregando arquivos JSON
import json
meuArquivo = 'pessoas.json'
with open(meuArquivo, 'r', encoding = 'utf-8', newline = '') as f:
     pessoas = json.load(f)
     print (pessoas)

     for p in pessoas:
         print(type(p))

     for p in pessoas:
         print(p['nome'], p['altura'])

