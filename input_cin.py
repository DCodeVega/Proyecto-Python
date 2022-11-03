import re
print("buscando palabras")
codigo = input("Ingrese codigo: ")

# dividir separar a partir de la o letra
# print(codigo.split("="))
palabra_dividida = codigo.split("=")

# extraer lo que esta en ""
pattern = '"(.*?)"'
texto = re.findall(pattern, codigo)
print(texto)

# rstrip() : devuelve una nueva cadena con los espacios en blanco finales eliminados. Es más fácil de recordar eliminando los espacios en blanco del lado "derecho" de la cadena.
# Verificar si existe input
if len(re.findall("input", codigo)) == 1:
    nuevo_texto = 'cout<<"'+texto[0]+'"<<endl;'
    variable = "cin>>"+palabra_dividida[0].rstrip()+";"
    print(nuevo_texto)
    print(variable)
