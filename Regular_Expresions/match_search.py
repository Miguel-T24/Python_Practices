# Match Search

import re

nombre1="Sandra Lopez"
nombre2 = "Antonio Gomez"
nombre3 = "Maria Lopez"
nombre4 = 'sandra Lopez'

# Match si hay coincidencia al COMIENZO de una cadena de texto
if(re.match("Sandra", nombre4, re.IGNORECASE)):
    print("Lo hemos encontrado")
else:
    print("NOO lo hemos encontrado")


# Search Para buscar una coincidencia en CUALQUIER PUNTO de la cadena
if(re.search("Lopez", nombre3, re.IGNORECASE)):
    print("Lo hemos encontrado")
else:
    print("NOO lo hemos encontrado")