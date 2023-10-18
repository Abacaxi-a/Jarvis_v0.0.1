from funções.voz import *
import os
import time

class funções:
    def pergunta(self):
        return pergunta(self)
        

    def funcao1(self):
        os.remove('frase.mp3')
        time.sleep(5)
        resposta(self,0)
        self.escanear()

    def funcao2(self):
        os.remove('frase.mp3')
        time.sleep(5)
        resposta(self,1)
    
    def funcao3(self):
        os.remove('frase.mp3')
        time.sleep(5)
        resposta(self,2)
    
    def erro(self):
        time.sleep(2)
        return resposta_errada(self)