# "Everybody thinks twice before solving this"

string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(chr(65))                                                                 # ord(): letra a entero
print(ord('A'))                                                                # chr(): entero a letra

step = 2                                                                       # Cambiar una letra. Step: cuanto se desplaza en el alfabeto
print(ord('k'))                                                               
print(ord('k') + step)
print(chr(ord('k') + step))
print(chr(ord('z') + step))                                                    # No funciona para la 'z'

# Para hacerlo circular
dist = (ord('z') + step - ord('a'))                                            # Distancia entre la 'z' y la 'a'
print(dist)
print((ord('z') + step - ord('a')) % (dist - 1))                               # Si es mayor que (dist-1), 'z', debe volver al principio.
print(chr((ord('z') + step - ord('a')) % (dist - 1) + ord('a')))               # Y añadir la diferencia a 'a'

# Traduccion del string. Loop al estilo Java o C
result = ""
for i in string:
    if i >= 'a' and i <= 'z':
        result += chr((ord(i) + step - ord('a')) % (dist - 1) + ord('a'))
    else:
        result += i

print(result)

# Traduccion del string con comprension de lista: Python
print(''.join([chr(((ord(i) + 2) - ord('a')) % (dist - 1) + ord('a')) if i >= 'a' and i <= 'z' else i for i in string]))

# Usando str.maketrans() con Paso=2
table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
result = string.translate(table)

print(result)

# Traduccion creando un diccionario. Paso=2
a = "abcdefghijklmnopqrstuvwxyz,. '()"                                         # Crear 2 listas
b = "cdefghijklmnopqrstuvwxyzab,. '()"

list(zip(a, b))                                                                # Crear un zip: [('a', 'c'), ('b', 'd'), ('c', 'e'), ('d', 'f'), ...]
dict(zip(a, b))                                                                # Crear un diccionario: {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', ...}

print(dict(zip(a, b))['z'])                                                    # Mapeo

print("".join([dict(zip(a,b))[i] for i in string]))                            # Traduccion del string

# URL http://www.pythonchallenge.com/pc/def/map.html -> map
string_2 = 'map'

result = ''.join([chr(((ord(i) + 2) - ord('a')) % (dist - 1) + ord('a')) if i >= 'a' and i <= 'z' else i for i in string_2])
print(result)                                                                  # Cambiar la URL por http://www.pythonchallenge.com/pc/def/result.html
