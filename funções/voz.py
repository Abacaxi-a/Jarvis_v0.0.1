from playsound import playsound
import gtts
import pandas as pd
import speech_recognition  as sr

def pergunta(self):
    rec = sr.Recognizer()
    #print(sr.Microphone().list_microphone_names())
    with sr.Microphone(1) as mic:
        rec.adjust_for_ambient_noise(mic)
        frase = gtts.gTTS('Qual seria o pedido',lang='pt-br')
        frase.save('frase_pergunta.mp3')
        playsound('frase_pergunta.mp3')
        audio = rec.listen(mic)
        self.texto = rec.recognize_google(audio,language='pt-BR')  
        return self.texto

def resposta(self,i):
    self.frase = gtts.gTTS(self.doc[i],lang='pt-br')
    self.frase.save('frase.mp3')
    return playsound('frase.mp3')

def resposta_errada(self):
    self.frase = gtts.gTTS('função não encontrada',lang='pt-br')
    self.frase.save('erro.mp3')
    return playsound('erro.mp3')