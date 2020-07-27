# Del codigo fuente: '<!-- <-- zip -->' -> cambiar la URL por http://www.pythonchallenge.com/pc/def/channel.zip
# Descomprimiendo y abriendo 'readme.txt':
# "welcome to my zipped list."
# "hint1: start from 90052"
# "hint2: answer is inside the zip"

import zipfile, re

f = zipfile.ZipFile("channel.zip")
num = '90052'

while True:                                                                    # Todos los . txt dicen "Next nothing is..." a primera vista, pero puede ser que alguno no 
    content = f.read(num + ".txt").decode("utf-8")
    print(content)
    match = re.search("Next nothing is (\d+)", content)                        # search en vez de match
    if match == None:
        break
    num = match.group(1)                                                       # En efecto, termina con: "Collect the comments."

num = '90052'
comments = []
while True:                                                                    # Se añaden las lineas necesarias para ver los comentarios del zip
    content = f.read(num + ".txt").decode("utf-8")
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    content
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))                                                       # El comentario dice hockey -> cambiar la URL por  http://www.pythonchallenge.com/pc/def/hockey.html

# it's in the air. look at the letters.
# Las letras que componen la palabra hockey son O, X, Y, G, E, N -> cambiar la URL por  http://www.pythonchallenge.com/pc/def/oxygen.html
