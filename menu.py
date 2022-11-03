import os
def menu():
    print("-------------------------------------------------------------------------------")
    print("------------- PROYECTO: CONVERSOR DE CODIGO Y CREADOR DE ARCHIVOS --------------")
    print(" MENU:")
    print(" 1: Inicializar variable")
    print(" 2: Realizar la codificacion")
    print(" 3: Nombre de archivo")
    print(" 4: Crear script")
    print(" 5: Finalizar")

def menu_opciones(opcion):
    if opcion == 1:
        print("Inicializar variable ")
    elif  opcion == 1:
        print("Realizar la codificacion: ")
    elif  opcion == 2:
        print("Nombre de archivo: ")
    elif  opcion == 3:
        print("Nombre de archivo: ")
    elif  opcion == 4:
        print("Crear script: ")


selecion_opcion = 0
while selecion_opcion < 5:
    menu()
    selecion_opcion = int(input("Ingrese Opcion: "))
    menu_opciones(selecion_opcion)
    os.system("cls")
