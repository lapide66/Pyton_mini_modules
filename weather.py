#coding: utf-8
import json, requests

# bloco para realizar o GET online
#req = requests.get("https://api.hgbrasil.com/weather/?format=json&woeid=455821")
#resposta = json.loads(req.text)
# fim bloco para realizar o GET online

resposta = json.loads(open('bh.json').read())

resposta2 = ('Cidade:{}\nTemperatura:{}Cº\nCondição Tempo:{}\nPeriodo:{}\nUmidade do ar:{}%\nAmanhecer:{}\nAnoitecer:{}\nGenerate by api.hgbrasil.com/weather at {}-{}'.format(str(resposta['results']['city_name']),str(resposta['results']['temp']),str(resposta['results']['description']),str(resposta['results']['currently']),str(resposta['results']['humidity']),str(resposta['results']['sunrise']),str(resposta['results']['sunset']),str(resposta['results']['date']),str(resposta['results']['time']))) 

print resposta2