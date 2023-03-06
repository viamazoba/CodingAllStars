import os
from bs4 import BeautifulSoup

directorio = './' # reemplazar con el directorio que deseas revisar
archivos_html = []

# Busca todos los archivos HTML en el directorio especificado y en sus subdirectorios y agrega sus nombres a la lista 'archivos_html'
for raiz, directorios, archivos in os.walk(directorio):
    for archivo in archivos:
        if archivo.endswith('.html'):
            archivos_html.append(os.path.join(raiz, archivo))

# Imprime la lista de archivos HTML

dictionary= {
'What do you want to learn?': 'मुझे क्या सीखना है?',
'Search 100,000 courses…': '100,000 कोर्स खोजें...',
'Search courses and more…': 'कोर्स और अधिक खोजें...'
}

for i in archivos_html:
    with open(i, "r") as archivo:
        contenido = archivo.read()

    soup = BeautifulSoup(contenido, "html.parser")
    inputs = soup.find_all("input", {"placeholder": True})
 
    for input in inputs:
        valor_anterior = input.get("placeholder")
        if(valor_anterior in dictionary.keys()):
            input["placeholder"] = dictionary[valor_anterior]


    try:
        nueva_etiqueta = soup.new_tag("script", src="./menu.js", defer=True)
        soup.head.append(nueva_etiqueta)
    except:
        print('Este archivo no tenia head: ', i)

    with open(i, "w") as archivo:
        archivo.write(str(soup))

print('El proceso ha finalizado')