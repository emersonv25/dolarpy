import requests
def getUSD():
    #retorna o valor do dolar
    dolar = requests.get('https://economia.awesomeapi.com.br/json/usd').json()
    return float(dolar[0]['bid'])

def formulario(pergunta , func, resposta):
    #:) uma brincadeirinha para gerar o formulario sem poluir o codigo
    num = float(input(pergunta))
    #numero de saida     #numero de entrada
    num2 = func(num)
    resposta = resposta.replace('FUNCnum1', f'{num:.2f}')
    resposta = resposta.replace('FUNCnum2', f'{num2:.2f}')
    print(resposta)
    
def testeUnidade_valorNumerico(num):
    #teste de unidade
    try:        
        return float(num)
    except:
        return ValueError(f'Valor {num} não é um número.')


def realParaDolar(real):
    #converte de real para dolar
    return testeUnidade_valorNumerico(real) / getUSD()

def dolarParaReal(dolar):
    #converte de dolar para real
    return testeUnidade_valorNumerico(dolar) * getUSD()


def pingpong(num):
    return testeUnidade_valorNumerico(num)

print(pingpong('a'))


        
