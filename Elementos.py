from datetime import *
from requests import *
from bs4 import *
import requests
from requests.models import parse_url
from time import *

def dolar():
    """-A função dolar, obtem por meio de um request em uma api a cotação atual do dólar e mantem o valor da cotação sempre atual por meio de um loop infinito.A obtenção deste dado é feita pelo método get, o atributo é trabalhado(formatação) e é retornado cotação do dólar para uso. """
    while True:
        res=requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
        resc=res.json()
        dolar = resc["USDBRL"]["bid"]
        dolar = round(float(dolar),2)
        dolar = f'{dolar:.2f}'
        return dolar
        

def variacao():
    """-De uma forma semelhante a função dolar(), é feito request, mas ao inves de obter a cotação é obtido a variação """
    while True:
        res=requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
        resc=res.json()
        vari = resc["USDBRL"]["varBid"]
        vari = round(float(vari),2)
        return vari


def datas():
    """A função datas(), tem com objetivo obtenção do horário(horas/minutos) local por meio da biblioteca datetime e é retornado para uso."""   
    from datetime import datetime
    hor=datetime.now().strftime('%H:%M')
    return hor


def pausa():
    """A função pausa() usa a biblioteca datetime para obter o dia da semana e o hórario, sua finalidade no código é pausar o script quando for final de semana e após o horário das 19."""
    from datetime import datetime    
    hor=datetime.now().strftime('%H')
    hor=int(hor)
    semana=datetime.today().weekday()
    semana= int(semana)
    return semana,hor

