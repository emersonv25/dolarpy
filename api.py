import requests
def getUSD():
    dolar = requests.get('https://economia.awesomeapi.com.br/json/usd').json()
    return float(dolar[0]['bid'])

def realParaDolar(real):
    return real / getUSD()

def dolarParaReal(dolar):
    return dolar * getUSD()







