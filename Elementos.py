from datetime import *
from requests import *
from bs4 import *
import requests
from requests.models import parse_url
from time import *

def cotação():
    '''
    -A função que retorna a cotação atual do dólar e muda o tipo de dado de string para float. 
    -Request faz a requisão para a url definida que entrega um json.
    
    return: Retorna o valor da atua cotação do dólar formatado em float.
    '''
    while True:
        res=requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
        resc=res.json()
        cotação_dolar = resc["USDBRL"]["bid"]
        cotação_dolar=float(cotação_dolar)
        cotação_dolar=f'{cotação_dolar:.2f}'
        return cotação_dolar

def variação():
    while True:
        res=requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
        resc=res.json()
        cotação_dolarv = resc["USDBRL"]["varBid"]
        return cotação_dolarv

def datas():
    from datetime import datetime
    
    hor=datetime.now().strftime('%H:%M')
    return hor

def pausa():
    from datetime import datetime
    
    hor=datetime.now().strftime('%H')
    hor=int(hor)
    semana=datetime.today().weekday()
    semana= int(semana)
    return semana,hor

