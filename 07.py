# Aparece una escala de grises. Se necesita una libreria para procesar imagenes

# 1.- Utilizando PIL(Pillow)
# Abrir Anaconda Prompt e instalar Pillow con 'conda install -c anaconda pillow'

from PIL import Image                                                          # Cargar la imagen previamente descargada
img = Image.open("oxygen.png")

import requests                                                                # Cargar la imagen desde la URL
from io import BytesIO
from PIL import Image
img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))

print(img.width, 'x', img.height)

print(img.getpixel((0,0)))                                                     # Tupla (R, G, B, alpha)

row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]            # Fila cental
print(row)                                                                     # Muchos duplicados, pues la anchura de cada bloque es de 7 pixeles

row = row[::7]
print(row)

order = [r for r, g, b, a in row if r == g == b]                               # Eliminando el ruido del final del array (pixeles que no son grises)
print(order)

# El RGB utiliza un numero positivo entre [0, 255] -> Representa caracteres ASCII
print("".join(map(chr, order)))

# "smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]"
import re
numbers = re.findall("\d+", "".join(map(chr, order)))
print(numbers)

# 2.- Utilizando PyPNG
# Abrir Anaconda Prompt e instalar PyPNG con 'conda install -c conda-forge pypng'
# Los pixeles se guardan como [r, g, b, a, r, g, b, a...]. Si el pixel es gris, el rgb deberia ser equivalente
# La anchura de los bloques es de 7 pixeles, por lo que el paso del rango debe ser 4*7


from urllib.request import urlopen
import png

response = urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")

(w, h, rgba, dummy) = png.Reader(response).read()

it = list(rgba)
mid = int(h / 2)
l = len(it[mid])
res = [chr(it[mid][i]) for i in range(0, l, 4 * 7) if it[mid][i] == it[mid][i + 1] == it[mid][i + 2]]

print("".join(res))

numbers = re.findall("\d+", "".join(map(chr, order)))
print(numbers)

# Solucion, extrayendo y mapeando los enteros letras
solution = "".join(map(chr, map(int, re.findall("\d+", "".join(res)))))
print(solution)                                                                # Cambiar la URL por http://www.pythonchallenge.com/pc/def/solution.html
