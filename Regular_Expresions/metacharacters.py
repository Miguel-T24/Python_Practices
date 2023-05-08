# Methacharacters

import re

lista_nombres = ["Ana Gomez", "Maria Martin", "Sandra Lopez", "Santiago Martin"]

# Todos los que comienzan con...
for element in lista_nombres:
    if (re.findall('^Sandra',element)):
        print(element)

#Todos los que terminan con...
for el in lista_nombres:
    if (re.findall("Martin$", el)):
        print(el)

lista_web = [
    'http://pildorasinformaticas.es',
    'ftp://pildorasinformaticas.es',
    'http://pildorasinformaticas.com',
    'ftp://pildorasinformaticas.com',
]

# Example with domain
for i in lista_web:
    if(re.search("es$", i)):
        print(i)

# example with protocol
for i in lista_web:
    if(re.search("^http", i)):
        print(i)


# differentes char
random_list = [
    'hombres',
    'mujeres',
    'mascotas',
    'camion',
    'camión'
]

for i in random_list:
    if (re.search("cami[oó]n", i)):
        print(i)