# "len(a[30]) = ?"
# Clickando la vaca: "a = [1, 11, 21, 1211, 111221, ". Es la "Look-and-say sequence"

# 1.- Solucion simple
a = '1'
b = ''
for i in range(0, 30):
    j = 0
    k = 0
    while j < len(a):
        while k < len(a) and a[k] == a[j]: k += 1
        b += str(k - j) + a[j]
        j = k
    print(b)
    a = b
    b = ''
    
print(len(a))

# 2.- Usando Python
import re       
                                                               
print(re.findall(r"(\d)(\1*)", "111221"))                                      # Expresion regular para encontrar las parejas de (numeros, length). El patron es un string  fila (r"..."), lo que significa que no necesita '\'
                                                                               # Equivalente a 're.findall("(\\d)(\\1*)", "111221")'
                                                                               # Tuplas: (Primera aparicion, siguiente aparicion) -> de la primera se extrae el numero, de la segunda la length-1 -> length+1

x = '1'
print("".join([str(len(i+j))+i for i,j in re.findall(r"(\d)(\1*)", x)]))
print("".join([str(len(i+j))+i for i,j in re.findall(r"(\d)(\1*)", "1")]))
print("".join([str(len(i+j))+i for i,j in re.findall(r"(\d)(\1*)", "11")]))
print( "".join([str(len(i+j))+i for i,j in re.findall(r"(\d)(\1*)", "21")]))
print("".join([str(len(i+j))+i for i,j in re.findall(r"(\d)(\1*)", "1211")]))

for n in range(30):                                                            # Corriendo el bucle 30 veces
    x="".join([str(len(j) + 1)+i for i, j in re.findall(r"(\d)(\1*)", x)])

print(len(x))

# 3.- Utilizando 'itertools.groupby()' en vez de expresiones regulares para encontrar las parejas (numeros, length)
import itertools

print("".join([str(len(list(j))) + i for i,j in itertools.groupby("1211")]))

print([(i, list(j)) for i,j in itertools.groupby("1211")])                     # No es necesario el '+1'

x = "1"
for n in range(30):
    x = "".join([str(len(list(j))) + i for i,j in itertools.groupby(x)])

print(len(x))

# 4.- En una sola linea
# 2 'reduce()'anidados. El exterior simplemente corre 30 veces, y establece el valor inicial 1 para la x. El interior hace lo mismo que la solucion 3.-

from itertools import groupby
from functools import reduce
print(len(reduce(lambda x, n:reduce(lambda a, b: a + str(len(list(b[1]))) + b[0], groupby(x), ""), range(30), "1")))

solution = len(x)
print(solution)                                                                # cambiar la URL por  http://www.pythonchallenge.com/pc/return/5808.html
