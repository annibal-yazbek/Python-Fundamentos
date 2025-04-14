import json

meuArquivo = 'pessoas.json'
with open(meuArquivo, 'r', encoding='utf-8', newline='') as f:
 pessoas = json.load(f)
print(pessoas)