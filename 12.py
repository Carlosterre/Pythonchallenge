# Click en "evil1.jpg" del codigo fuente -> http://www.pythonchallenge.com/pc/return/evil1.jpg -> Cambiar URL por 'evil2' http://www.pythonchallenge.com/pc/return/evil2.jpg
# Cambiar sufijo jpg por gfx -> Se descarga 'evil2.gfx'
# Cambiar URL por 'evil3' http://www.pythonchallenge.com/pc/return/evil3.jpg
# Cambiar URL por 'evil4' http://www.pythonchallenge.com/pc/return/evil4.jpg
# Cambiar URL por 'evil5' http://www.pythonchallenge.com/pc/return/evil5.jpg -> Error 404

# CMD: curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg -> "Bert is evil! go back!"

data = open("evil2.gfx", "rb").read()
print(data)
print(len(data))

for i in range(5):                                                             # En imagen se reparten las cartas en 5 montones -> Separar los bytes en 5 grupos
    open('%d.jpg' % i, 'wb').write(data[i::5])
    
# Las 5 imagenes generadas: '0.jpg' dis,'1.jpg' pro, '2.jpg' port, '3.jpg' ional, '4.jpg' ~ity~
# Cambiar URL por http://www.pythonchallenge.com/pc/return/disproportional.html
