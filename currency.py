#coding: utf-8
import json, requests

# bloco para realizar o GET online

#req = requests.get("https://economia.awesomeapi.com.br/json/all")
#resposta = json.loads(req.text)

# Fim bloco para realizar o GET online

resposta = json.loads(open('currency.json').read())
colecttime = (resposta['USD']['create_date'])

realtime = (colecttime[8:10]+"/"+colecttime[5:7]+"/"+colecttime[0:4]+"-"+colecttime[11:19]) # Este campo formata da no padrao brasileiro formato original:2018-09-03 10:40:09

print ('Dólar R${}\nEuro R${}\nLibra R${}\nBitcoin R${}\nGenerate by economia.awesomeapi.com.br at {}(USD)'.format(str(resposta['USD']['high']),str(resposta['EUR']['high']),str(resposta['GBP']['high']),str(resposta['BTC']['high']),realtime))