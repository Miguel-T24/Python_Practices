# Introduction

"""
Se hacen dos preguntas importantes

1. Coincide esta cadena con este patron?
2. Hay alguna coincidencia con el patron en alguna parte de esta cadena?

Se puede utilizar pra modificar la cadena de carcateres o dividirla en varias formas


"""
import re

# 1. Compilando expresiones regulares
p = re.compile('ab*')
print(p)

# 2. Tambien se puede usar un argumento opcional flags (bandera), usando para habilitar varias catacteristicas y varioaciones de sintaxis.
p = re.compile("ab*",re.IGNORECASE)
print(p)

# 3. Realizando coincidencias
"""
- Match(): Determinasi la RE coincide con el cominezo de la cadena de caratreres
- Search(): Escanea una cadena, buscando cualquier ubicacion donde coincida este re
- findall(): Encuentra tosdas las subcadenas de caracteres donde coincide la re y las retorna como un lista
- finditer(): Encuentra todas las subcadenas donde la RE coincide y la retorna como un termino iterado

"""

# Match y search() retornan None si la coincidencia no puede serr encontrada. Si tienen exito, se retorna una instancia match object, que contiene informaicon sobre la coincidencia: donde comienza y termina

# Usando match
print("Usando Match:")
print("Primera forma:")
p = re.compile('[a-z]+')
print(p)
print(p.match(""))
print(p.match("tempo"))

# Other way
print("Segunda forma:")
print(re.match('[a-z]+',"tempo"))

# Two ways
print("\nUtilizando los metodos de match de las dos formas:")
print("Primera forma:")
p = re.compile('[a-z]+')
m = p.match("tempo")
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

print("Segunda forma:")
m = re.match("[a-z]+","tempo")
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())


# Usando search
print("\nUsando Seach:")
# Search evalua toda la cadena por lo que no necesariamento empezara en 0
m = re.search("[a-z]+", "::: message")
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# Utilizando findall()
print("\nUtilizando Findall()")
print("Puedo usarlo de cualquiera d elas ods formas pero lo utilizare con la quecra mas facil")

texto = '12 drummers drumming, 11 pipers piping, 10 lords a-leaping'
m = re.findall("\d+",texto)
print(m)
m = re.findall(r"\d+",texto)
print(m)

# Utilizando finditer()
print("\nUtilizando finditer()")
iterador = re.finditer("\d+", texto)
print(iterador) # Devuelve un objeto iterador

for i in iterador:
    print(i.span())

"""
Flags o banderas

- ASCII , A : Hace que varios escapes como \w, \b, \s ,\d coincidan solo en caracteres ASCII con la propiedad respectiva

- DOTALL, S  : Hcae que . coincida con cualquier caracter, incluidas las nuevas lineas

- IGNORECASE, I : Hca ecoincidencias que no distingan entre mayusculas y minusculas

- LOCALE , L : Hace una coincidencia con reconocimiento de configuracion regional

- MULTILINE, M : Coincidencia de varias lineas, que afecta a ^ y $

- VERBOSE, X(for "extended") : Habilite RE detallados, que se pueden organizar de manera mas limpia y comprensible

"""