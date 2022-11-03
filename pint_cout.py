import re

print("buscando palabras")

codigo = input("Ingrese codigo: ")

# contar coincidencias print
print(len(re.findall("print", codigo)))

# extraer lo que esta en ""
pattern = '"(.*?)"'
x = re.findall(pattern, codigo)
print(x)


# extraer lo que esta en ""
pattern = '{(.*?)}'
x = re.findall(pattern, codigo)
print(x)


# verificar si existe print
if len(re.findall("print", codigo)) == 1:
    # extraer lo que esta en "    "
    pattern = '"(.*?)"'
    x = re.findall(pattern, codigo)
    # print(x)

    # extraer lo que esta en "{}"
    pattern = '{(.*?)}'
    x_valor = re.findall(pattern, codigo)
    print(x_valor)

    # El replace()método reemplaza una frase específica con otra frase específica.
    texto_solo = x[0].replace("{"+x_valor[0]+"}", ": ")
    impresion = 'cout<<"'+texto_solo+'"<<'+x_valor[0]+'<<endl;'
    print(impresion)
