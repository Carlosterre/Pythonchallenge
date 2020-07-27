# "One small letter, surrounded by EXACTLY three big bodyguards on each of its sides"

# Cargar datos del txt (texto extraido del codigo fuente)
data = open('03.txt').read()

# Extraer el texto directamente de HTML
import urllib.request
import re
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()

data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]

# Encontrar todos los segmentos del string con el patron 'AAAbCCC'
# Patron:
# '[a-z]' 1 letra minuscula
# '[A-Z]' 1 letra mayuscula
# '[A-Z]{3}' 3 letras mayusculas consecutivas
# '[A-Z]{3}[a-z][A-Z]{3}' 3 letras mayusculas consecutivas + 1 letra minuscula + 3 letras mayusculas consecutivas
# '[^A-Z]' cualquier letra excepto mayuscula
# '[^A-Z]+' al menos una letra
# '[^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+' algo antes y algo despues del patron (AAAbCCC) de manera que no haya mas de 3 mayusculas consecutivas en cada lado
# '[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+' solo interesa la minuscula

print(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data))

result = "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data))    # Juntando las letras
print(result)                                                                  # Cambiar la URL por http://www.pythonchallenge.com/pc/def/result.html
                                                                               # Cambiar la URL por http://www.pythonchallenge.com/pc/def/result.php
                                                                               