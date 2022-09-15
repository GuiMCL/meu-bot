


from cProfile import label
from cgitb import text
from distutils.cmd import Command
from imaplib import Commands
from posixpath import split
from sqlite3 import Row
import tkinter
from ast import Import, Num, Return
from cgi import print_arguments
from tkinter.tix import COLUMN
from tracemalloc import start
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from tkinter import*
 



def BOT ():


            chrome_options = Options()
            chrome_options.add_argument("-headless")
            nav = webdriver.Chrome(options = chrome_options)
            nav.get('https://blaze.com/pt/games/double')

            pegardados = nav.find_element(By.XPATH, '//*[@id="roulette-recent"]').text

            tfg = pegardados.split()
            def qualnum(x):
                if x == '1':
                    return 1

                if x == '2':
                    return 2

                if x == '3':
                    return 3

                if x == '4':
                    return 4

                if x == '5':
                    return 5

                if x == '6':
                    return 6

                if x == '7':
                    return 7

                if x == '8':
                    return 8

                if x == '9':
                    return 9

                if x == '10':
                    return 10

                if x == '11':
                    return 11

                if x == '12':
                    return 12

                if x == '13':
                    return 13

                if x == '14':
                    return 14

            def qualcor(x):
                if x == '1':
                    return 'Vermelho'

                if x == '2':
                    return 'Vermelho'

                if x == '3':
                    return 'Vermelho'

                if x == '4':
                    return 'Vermelho'

                if x == '5':
                    return 'Vermelho'

                if x == '6':
                    return 'Vermelho'

                if x == '7':
                    return 'Vermelho'

                if x == '8':
                    return 'Preto'

                if x == '9':
                    return 'Preto'

                if x == '10':
                    return 'Preto'

                if x == '11':
                    return 'Preto'

                if x == '12':
                    return 'Preto'

                if x == '13':
                    return 'Preto'

                if x == '14':
                    return 'Preto'

            pd = tfg[0:3]

            mapeando = map(qualnum, pd)
            mapeando2 = map(qualcor, pd)

            finalnum = list(mapeando)
            finalcor = list(mapeando2)

            def verificarsaida(num):
                if num == [ 'Vermelho', 'Vermelho', 'Vermelho' ]:
                    return '''
                    Estrategia x entrar no Preto 
                    Apoiar no Branco 
                    '''
                if num == [ 'Preto', 'Preto', 'Vermelho' ]:
                    return '''
                    Estrategia x entrar no preto
                    Apoiar no Branco 
                    '''

                if num == [ 'Preto', 'Preto', 'Preto' ]:
                    return  '''
                    Estrategia x entrar no ver
                    Apoiar no Branco 
                    '''
                if num == [ 'Vermelho', 'Preto', 'Vermelho' ]:
                    return '''
                    Estrategia x entrar no 
                    Apoiar no Branco 
                    '''    
                if num == [ 'Vermelho', 'Vermelho', 'Preto' ]:
                    return '''
                    Estrategia x entrar no 
                    Apoiar no Branco 
                    '''    
                if num == [ 'Preto', 'Vermelho', 'Vermelho' ]:
                    return '''
                    Estrategia x entrar no 
                    Apoiar no Branco 
                    '''    
            
            testando = verificarsaida(finalcor)

            print(finalcor)
            print (testando)


           
            textocotacao ["text"] = testando




          
        



janela = Tk()

janela.title("BOT")
janela.geometry("400x200")

texto2 = Label(janela, text= "Gerar entrada com o BOT")
texto2.grid(column=0 , row= 1, padx=10, pady= 10 )


botao = Button(janela ,text= "Gerar entrada" , command= BOT )
botao.grid (column=0,row= 2, padx=10, pady= 10)


textocotacao = Label(janela , text= "" )
textocotacao.grid(column= 0 , row= 4, padx=10, pady= 10 )


janela.mainloop()





       


    
        

