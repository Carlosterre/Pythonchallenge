# "Pronounce it"
# Del codigo fuente: '<!-- peak hell sounds familiar ? -->' suena parecido a 'pickle'. Des-serializacion y compresion

from urllib.request import urlopen
string = urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
string.decode()                                                                # '.decode()' revela el texto codificado como utf-8 o cualquier otra forma

import pickle                                                                  # Des-serializa el texto
data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))  # Lista de tuplas

for line in data:                                                              # Convertir los caracteres repetitivos en tuplas de (caracter, numero de apariciones)
    print("".join([k * v for k, v in line]))                                   # El banner dice "channel" -> Cambiar la URL por http://www.pythonchallenge.com/pc/def/channel.html
    