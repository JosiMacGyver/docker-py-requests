import requests
print ("Teste do Docker com o requests como dependência")
print("digite o cep:")

cep=input()
print (cep)
url = "https://viacep.com.br/ws/" + cep +"/json"

r = requests.get(url)
print (r.text) 