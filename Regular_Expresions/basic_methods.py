# Regular Expresions

import re

cadena = "Vamos aprender expresiones regulares en python. python es un lenguaje de sintaxis sencilla"

# Search Method
print(re.search("aprender", cadena)) # <re.Match object; span(6,14), match = "aprender"
print(re.search("aprendeeerrr", cadena)) # None

if re.search("aprendeeer", cadena) is not None:
    print("Encontre el texto")
else:
    print("No he encontrado el texto")

textEcontrado = re.search("aprender", cadena)
print(textEcontrado) # <re.Match object; span(6,14), match = "aprender"

# Start Method
print(textEcontrado.start()) # 6
# End Method
print(textEcontrado.end()) # 14
# span Method
print(textEcontrado.span()) # (6,14)


# Texto a buscar
text_buscar = "python"
print(re.findall(text_buscar, cadena)) # ['python','python']