#https://decodigo.com/python-crear-archivos-de-texto
import os
file = open("C:/Users/USUARIO/Desktop/proyecto Python/prueba3.txt", "w")
file.write('print("INGRES UN VALOR")' + os.linesep)
file.write("#include<iostream>\n scout <<''hola mundo del grupo'';\n")
file.write("siguiente parrafo")
file.close()

#https://decodigo.com/python-leer-un-archivo-de-texto#:~:text=Para%20leer%20un%20archivo%20de,referenciado%20por%20la%20variable%20archivo.
# with open("C:/Users/santy/Desktop/Curso python/Archivos/prueba.py","r") as archivo:
#     for linea in archivo:
#         print(linea)