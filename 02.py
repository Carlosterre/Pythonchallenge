# Recognize the characters. maybe they are in the book, but MAYBE they are in the page source

# Cargar datos del txt (texto extraido del codigo fuente)
data = open('02.txt').read()

# Extraer el texto directamente de HTML
import urllib.request                                                          # Modulo HTML
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

import re
comments = re.findall("<!--(.*?)-->", html, re.DOTALL)                         # Extraer el bloque de comentarios. Por defecto, '.' no cuadra con '\n' (nueva linea), por lo que hay que usar 're.DOTALL'
                                                                               # '<!--(.*?)-->' captura todos los bloques entre <!-- y -->

data = comments[-1]                                                            # Solo interesa la ultima parte

count = {}                                                                     # Encontrar los caracteres "raros"
for i in data:
    count[i] = count.get(i, 0) + 1
        
print(count)                                                                   # Los caracteres "raros" son los que aparecen 1 vez: letras del alfabeto

result = "".join(re.findall("[A-Za-z]", data))
print(result)                                                                  # Cambiar la URL por http://www.pythonchallenge.com/pc/def/result.html
