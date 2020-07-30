# "phone that evil"
# Pulsar tecla '5' del telefono de la imagen -> http://www.pythonchallenge.com/pc/phonebook.php

import xmlrpc.client

conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(conn)

print(conn.system.listMethods())
print(conn.system.methodHelp("phone"))
print(conn.system.methodSignature("phone"))                                    # El input deberia ser un nombre y el output un numero

print(conn.phone("Bert"))                                                      # 555 significa numero falso -> Cambiar URL por http://www.pythonchallenge.com/pc/return/italy.html
