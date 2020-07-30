# "odd even" -> Separar la imagen en pares y nones

from PIL import Image

im = Image.open('cave.jpg')
(w, h) = im.size

even = Image.new('RGB', (w // 2, h // 2))
odd = Image.new('RGB', (w // 2, h // 2))

for i in range(w):
    for j in range(h):
        p = im.getpixel((i, j))
        if (j + 1) % 2 == 1:
            odd.putpixel((i // 2, j // 2), p)
        else:
            even.putpixel((i // 2, j // 2), p)

even.save('even.jpg')                                                          # Abrir 'even.jpg' -> "evil" -> Cambiar URL por http://www.pythonchallenge.com/pc/return/evil.html
odd.save('odd.jpg')