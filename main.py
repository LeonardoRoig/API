import pandas as pd
from flask import Flask, jsonify
from flask import Flask, render_template
app = Flask(__name__)
tabela = pd.read_csv ('Advertising.csv')
#Construir funcionalidaes
@app.route('/')
def homepage():
  return 'Resultado Online da Planilha - API Online - Para obter o resultado para a API use o link: https://minhaapi.leonardoroig.repl.co/vendas'


print(tabela)
  
@app.route('/vendas')
def total_vendas():
  tabela = pd.read_csv ('Advertising.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)#EndPoint(Cada link que dá uma resposta é um EndPoint, onde o usuario requisita e recebe resposta.) 


#Rodar API
app.run(host = '0.0.0.0')

#tabela = pd.read_csv ('Advertising.csv')
#total_vendas = tabela['Vendas'].sum()
#print ('Tabela de Dados')
#print (tabela)
#print ('Total de Vendas')
#print (total_vendas)