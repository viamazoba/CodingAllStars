
from bs4 import BeautifulSoup
import openai
import os
import time

counter = 0
openai.api_key = 'Put here your Key'

def translation(text):
    translate = openai.Completion.create(engine = "text-davinci-003", prompt = text, max_tokens = 4000)
    wordHindi = translate.choices[0].text

    return wordHindi

directorio = './' # reemplazar con el directorio que deseas revisar
archivos_html = []

# Busca todos los archivos HTML en el directorio especificado y en sus subdirectorios y agrega sus nombres a la lista 'archivos_html'
for raiz, directorios, archivos in os.walk(directorio):
    for archivo in archivos:
        if archivo.endswith('.html'):
            archivos_html.append(os.path.join(raiz, archivo))


listWords = []
listTranslatedWords = []

selectedWords = []

with open('specialWords.txt', 'r') as archivo:
   for i in archivo:
        word = i.rstrip()
        listWords.append(word)
    


for i in listWords:
    print('Traducción: ', counter)
    try:
        wordToTranslate = f"Traduce al Hindi (sin explicaciones): '{i}'"
        wordInHindi = translation(wordToTranslate)
        listTranslatedWords.append(wordInHindi)
        selectedWords.append(i)
        time.sleep(10)
        counter += 1
    except:
        continue

dictionary = dict(zip(selectedWords,listTranslatedWords))


for i in dictionary.keys():
    dictionary[i] = dictionary[i].replace('\n\n', '')






# # Imprime los nombres de los archivos encontrados
for html in archivos_html:

    print('\n','Traducción en proceso del documento:', html, '\n')

    # Abra el archivo HTML y cárguelo en BeautifulSoup
    with open(html) as archivo:
        soup = BeautifulSoup(archivo, "html.parser")


    # Encuentre todas las etiquetas HTML que contienen texto
    etiquetas_con_texto = soup.find_all(text=True)

    # Para cada etiqueta con texto, traduzca el texto y reemplace el texto original
    for texto in etiquetas_con_texto:
        # Si el texto es el contenido de un atributo, como href, no lo traduzca
        if texto.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            continue
        
        if texto.strip() != '':
            if texto.strip() in selectedWords:
                try:
                    texto_traducido = dictionary[texto.strip()]
                    texto.replace_with(texto_traducido)

                except:
                    continue

    # Guarde los cambios en el archivo HTML
    with open(html, "w") as archivo:
        archivo.write(str(soup))
    
    print('Se tradujo el documento: ', html)