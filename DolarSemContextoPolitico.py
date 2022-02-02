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


def main():
    #loop para o bot não parar
    semana,limitehor=pausa()
    atual = 0
    while True:
        if semana != 5 and semana != 6:
            if limitehor > 8 and limitehor < 19:
                
                while True:
                    try:
                        horario=datas()
                        dol=dolar()
                        dol=float(dol)
                        dol = f'{dol:.2f}' 
                        dol_formatado = str(dol)   
                        dol=float(dol)        
                        if dol > atual:                           
                            api.update_status(f'''Dólar subiu: R$ {dol_formatado.replace(".",",")} / {horario}
                                    :(''')
                            print(f'Tweet Postado as: {horario}')
                            atual=dol
                        
                        if dol < atual: 
                            api.update_status(f'''Dólar caiu: R$ {dol_formatado.replace(".",",")} / {horario}
                                    :)''')
                            print(f'Tweet Postado as: {horario}')
                            atual=dol
                        if dol == atual:
                            #pass foi usado para não ocorrer um tipo de flood com o mesmo valor do dolar
                            pass   
                        sleep(60*20)
                    
                    except ValueError as err:
                        print(f'Ocorreu um Value Error:{err} ')
                        break
                    except TypeError as err:
                        print(f'Ocorreu um TypeError: {err}')
                        break


if __name__ == "__main__":
    main()


