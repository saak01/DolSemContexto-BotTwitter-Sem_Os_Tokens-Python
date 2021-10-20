from datetime import *
from requests import *
from bs4 import *
import requests
from requests.models import parse_url
from time import *

def cotação():
    '''
    -A função cotação é responsavel por request da cotação atual do dolar, que está em json
    -Após formatado para float é retornado "cotação_dolar" para uso.
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

