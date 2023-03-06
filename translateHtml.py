from bs4 import BeautifulSoup
from easynmt import EasyNMT
import os

directorio = './' # reemplazar con el directorio que deseas revisar
archivos_html = []

palabras = set()

# Busca todos los archivos HTML en el directorio especificado y en sus subdirectorios y agrega sus nombres a la lista 'archivos_html'
for raiz, directorios, archivos in os.walk(directorio):
    for archivo in archivos:
        if archivo.endswith('.html'):
            archivos_html.append(os.path.join(raiz, archivo))

# Imprime los nombres de los archivos encontrados
for html in archivos_html:
    print(html)
    #print('\n','Documento:', html, '\n')

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
            palabras.add(texto.strip())


listWords = list(palabras)
selectedWords = []
translateWords = []
wordsNoTranslate = []

model = EasyNMT('opus-mt')

for i in listWords:
 try:
  variable = model.translate(i, target_lang='hi')
  translateWords.append(variable)
  selectedWords.append(i)

 except:
  wordsNoTranslate.append(i)

# Creando diccionario 
dictionary = dict(zip(selectedWords, translateWords))


print('Cantidad de palabras especiales encontradas:', len(wordsNoTranslate))

# Se guardan las palabras que no se pudieron traducir
with open('specialWords.txt', 'w') as archivo:
    for word in wordsNoTranslate:
        archivo.write(word + '\n')





# Imprime los nombres de los archivos encontrados
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


#with open("words.txt", "w") as archivo:
    #for palabra in palabras:
        #archivo.write(palabra + "\n")
