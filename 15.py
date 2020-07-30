# "whom?"
# Del codigo fuente: <!-- he ain't the youngest, he is the second -->
#                    <!-- todo: buy flowers for tomorrow -->

# Hay un agujero quemado en el año del calendario -> 1XX6
# El 1 de enero es jueves
# En pequeño se ve que hay 29 de febrero -> Año bisiesto
# El 26 de enero esta rodeado

# 1.- Filtrar todos los años desde 1006 hasta 1996
print(1006 / 4)                                                                # 251.5 -> 1006 no fue bisiesto
print(1016 / 4)                                                                # Primer año bisiesto

print(list(range(1016, 1996, 20)))                                             # De 20 en 20

import datetime

# Buscar años cuyo 26 de enero fue lunes
print([year for year in range(1016, 1996, 20) if datetime.date(year, 1, 26).isoweekday() == 1])

# 1176 es el mas joven, 1356 es el segundo mas joven -> 26/01/1356

# 2.- Utilizando datetime y 'calendar.isleap()'
import calendar

for year in range(1006,1996,10):
    d = datetime.date(year, 1, 26)
    if d.isoweekday() == 1 & calendar.isleap(year):
        print(d)
        
# Comprar flores para mañana -> 27/01/1356 fecha de nacimiento de Mozart -> Cambiar URL por http://www.pythonchallenge.com/pc/return/mozart.html
