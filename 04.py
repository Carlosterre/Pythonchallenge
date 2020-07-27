# "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# "And the next nothing is 44827" -> Cambiar la URL por http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827
# "And the next nothing is 45439"
# ...

from urllib.request import urlopen
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"        # Codigo que simula el proceso manual
num = "12345"
content = urlopen(uri % num).read().decode()
print(content)

match = re.search("and the next nothing is (\d+)", content)                    # Extraer el numero con una expresion regular
print(match)

print(match.group(0))                                                          # '.group(0)' devuelve el texto entero que cumpla el patron
print(match.group(1))                                                          # Los segmentos capturados empiezan en '.group(1)'

pattern = re.compile("and the next nothing is (\d+)")
while True:
    content = urlopen(uri % num).read().decode('utf-8')
    print(content)
    match = pattern.match(content)                                             # 'pattern.match' falla porque hay una linea de texto diferente: "Your hands are getting tired". Hay que usar 'pattern.search'
    if match == None:
        break
    num = match.group(1)

pattern = re.compile("and the next nothing is (\d+)")
while True:
    content = urlopen(uri % num).read().decode('utf-8')
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)

# "Yes. Divide by two and keep going"
num = str(16044/2)

pattern = re.compile("and the next nothing is (\d+)")
while True:
    content = urlopen(uri % num).read().decode('utf-8')
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)                                                       # "peak.html" es el ultimo -> Cambiar la URL por http://www.pythonchallenge.com/pc/def/peak.html
