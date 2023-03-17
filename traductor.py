from googletrans import Translator
from gtts import gTTS
import os

translator = Translator()
book = open(r"book.txt")
book_text=book.read()
textoSalida = translator.translate(book_text, dest='es')
print("****************\n")
print(textoSalida.text)
textoSalida1=textoSalida.text
lenguaje="es-us"
audio=gTTS(text= textoSalida1, lang=lenguaje, slow=False)
audio.save("texto.mp3")
os.system("start texto.mp3")

