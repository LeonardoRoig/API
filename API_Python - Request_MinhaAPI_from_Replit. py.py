import requests

link = 'https://minhaapi.leonardoroig.repl.co/vendas'

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()

print(dicionario['total_vendas'])
