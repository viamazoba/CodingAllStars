from bs4 import BeautifulSoup, Comment
import os

directorio = './' # reemplazar con el directorio que deseas revisar
archivos_html = []

# Busca todos los archivos HTML en el directorio especificado y en sus subdirectorios y agrega sus nombres a la lista 'archivos_html'
for raiz, directorios, archivos in os.walk(directorio):
    for archivo in archivos:
        if archivo.endswith('.html'):
            archivos_html.append(os.path.join(raiz, archivo))




for html in archivos_html:

        # Abra el archivo HTML y cárguelo en BeautifulSoup
    with open(html) as archivo:
        soup = BeautifulSoup(archivo, "html.parser")

    # Encuentre todas las etiquetas <img> con el atributo data-source
    img_etiquetas = soup.find_all("img", {"data-src": True})

    # Para cada etiqueta img, cambie el valor de src a data-source y elimine data-source
    for img in img_etiquetas:
        img["src"] = img["data-src"]
        del img["data-src"]

    # Encontrar todos los comentarios y eliminarlos
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    # Guarde los cambios en el archivo HTML
    with open(html, "w") as archivo:
        archivo.write(str(soup))
    
    print(html)