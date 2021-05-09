# Descargar el codigo de barras 'wire.png'
# Del codigo fuente: <!-- remember: 100*100 = (100+99+99+98) + (...  -->

from PIL import Image

im = Image.open('wire.png')
print(im.size)                                                                 # La imagen no es 100x100, ess 1000x1

delta = [(1,0), (0,1), (-1,0), (0,-1)]                                         # Crear otra imagen de 100x100 rodeando el cuadrado desde fuera hacia dentro (espiral)
out = Image.new('RGB', [100, 100])
x,y,p = -1, 0, 0
d = 200
while d / 2 > 0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            out.putpixel((x, y),im.getpixel((p, 0)))
            p += 1
        d -= 1
out.save('Level_14.jpg')                                                       # La imagen es un gato -> Cambiar URL por http://www.pythonchallenge.com/pc/return/cat.html

# "and its name is uzi. you'll hear from him later" -> Cambiar URL por http://www.pythonchallenge.com/pc/return/uzi.html
