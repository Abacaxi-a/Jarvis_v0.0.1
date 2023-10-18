from playsound import playsound
import gtts
import pandas as pd
from funções.função import *
from funções.voz import pergunta
import time

doc = pd.read_csv('frases.csv')
doc = doc['teste']

class jarvis(funções):
    def __init__(self): 
        self.doc = doc
        print(self.pergunta())
        
        if "função um" in self.texto:
            self.funcao1()
        elif "teste" in self.texto:
            self.funcao2()
        elif "teste" in self.texto:
            self.funcao3()
        else:
            time.sleep(2)
            self.erro()
        

if '__main__' == __name__:
    jarvis()
    