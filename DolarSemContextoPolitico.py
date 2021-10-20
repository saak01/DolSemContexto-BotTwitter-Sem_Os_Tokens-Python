from Elementos import *
from time import sleep
from tweepy import *
import tweepy
from Elementos import *

# Autenticação do Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
#Criando o Objeto da api
api = tweepy.API(auth)

#Limites de Tweet
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)



def main():
    atual=0
    while True:
        #loop para o bot não parar
        semana,limitehor=pausa()

        if semana != 5 and semana != 6:
            if limitehor > 8 and limitehor < 18:
                try:
                    while True:
                        horario=datas()
                        dol=cotação()
                        dol=float(dol)
                        if dol > atual:
                            #tw é a variavael com nome tweet é a informação que vai ser postada pelo tweet
                            tw=float(dol)
                            #formatação para uma melhor exp
                            tw1= (f'{tw:.2f}')
                            #Mudando os tipos primitivos de float para str"
                            tw1=str(tw1)
                            #tratamento de str para trocar "." por ","
                            tw1=tw1.replace('.',',')
                            #Imprimindo o tweet com as infos recolhidas
                            api.update_status(f'''Dólar subiu: R$ {tw1} / {horario}
                                    :(''')
                            print(f'Tweet Postado as: {horario}')
                            atual=dol
                        
                        if dol < atual:
                            #tw é a variavael com nome tweet é a informação que vai ser postada pelo tweet
                            tw=float(dol)
                            #formatação para uma melhor exp
                            tw1= (f'{tw:.2f}')
                            #Mudando os tipos primitivos de float para str"
                            tw1=str(tw1)
                            #tratamento de str para trocar "." por ","
                            tw1=tw1.replace('.',',')
                            #Imprimindo o tweet com as infos recolhidas
                            api.update_status(f'''Dólar caiu: R$ {tw1} / {horario}
                                    :)''')
                            print(f'Tweet Postado as: {horario}')
                            atual=dol
                        if dol == atual:
                            #pass foi usado para não ocorrer um tipo de flood com o mesmo valor do dolar
                            pass   
                        sleep(60*20)
                except:
                    pass 

#chamada da função main
main()