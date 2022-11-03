from cmath import pi
from ctypes import c_int64
from mailbox import linesep
import os
import msvcrt as m
# ------------------------------------------- VARIABLES GLOBALES ------------------------------------
# ---- CREANDO UNA LISTA VACIA -----
lista_variables = ["","","","","","","","","",""]
lista_lineas_codigo = []
nombre_archivo = []
num_de_apps = 0
nombre = ""
apellido =""
ci=0
datos =[]

# ----(*VARIABLES*) VALIDA EL INGRESO DE DATOS POR TECLADO, OBLIGANDO QUE SEA NUMERICO --------------


def validar_si_numero():
    cantidad_variable = input("Ingrese la cantidad de Aplicaiones a Instalar: ")
    if cantidad_variable.isnumeric() == True:
        return int(cantidad_variable)
    else:
        return 0


def asignar_variables(num_variable):
    for i in range(1, num_variable+1):
        print("1: Fecebook")
        print("2: WhatsApp")
        print("3: TikTok")
        print("4: Instagram")
        print("---Juegos---")
        print("5: Free Fire")
        print("6: Mobile Legends: Bang Bang")
        print("7: Geometry Dash")
        print("8: Minecraft")
        print("9: Pokemon Go")
        print("10: Clash Royale")
        print("PRONTO HABRA MAS APLICACIONES A INSTALAR...")
        num_de_apps=int(input("Ingrese la app Nº "+str(i)+" a Instalar: "))
        if num_de_apps==1:
            #lista_variables.append("Facebook")
            lista_variables [0]="Facebook"
        elif num_de_apps==2:
            #lista_variables.append("WhatsApp")
            lista_variables [1]="WhatsApp"
        elif num_de_apps==3:
            #lista_variables.append("TikTok")
            lista_variables [2]="TikTok"
        elif num_de_apps==4:
            #lista_variables.append("Instagram")
            lista_variables [3]="Instagram"
        elif num_de_apps==5:
            #lista_variables.append("Free Fire")
            lista_variables [4]="Free Fire"
        elif num_de_apps==6:
            #lista_variables.append("Mobile Legends: Bang Bang")
            lista_variables [5]="Mobile Legends: Bang Bang"
        elif num_de_apps==7:
            #lista_variables.append("Geometry Dash")
            lista_variables [6]="Geometry Dash"
        elif num_de_apps==8:
            #lista_variables.append("Minecraft")
            lista_variables [7]="Minecraft"
        elif num_de_apps==9:
            #lista_variables.append("Pokemon Go")
            lista_variables [8]="Pokemon Go"
        elif num_de_apps==10:
            #lista_variables.append("Clash Royale")
            lista_variables [9]="Clash Royale"
        else:
            i=i-1
            print("Eliga una de nuestras Opciones Mostradas")

def variables():
    num_variable = validar_si_numero()
    # ---- MIENTRAS SEA 0 ----
    while num_variable == 0:
        num_variable = validar_si_numero()
    asignar_variables(num_variable)
# -------------------------------------------------- FIN DE CODIGO VARIABLES --------------------------
# ------------------------------- (*CODIFICACION*) REALIZAMOS LA CODIFICACION  -----------------------


def verificar_lista_variables():
    if len(lista_variables) > 0:
        return True
    else:
        return False


def validar_si_numero_codificacion():
    cantidad_fila = input("Ingrese numero de cantidad filas: ")
    if cantidad_fila.isnumeric() == True:
        return int(cantidad_fila)
    else:
        return 0
def datos_del_propietario():
    nombre=input("Ingrese su Nombre: ")
    apellido=input("Ingrese su Apellido: ")
    ci=int(input("Ingrese su ID (Solo Numeros): "))
    lista_lineas_codigo.append("puesto")
    datos.append(nombre)
    datos.append(apellido)
    datos.append(str(ci))
    

def asignar_filas(num_filas):
    for i in range(1, num_filas+1):
        codigo = input("Escriba codigo en la linea "+str(i)+": ")
        lista_lineas_codigo.append(codigo)


def definir_codificacion():
    if verificar_lista_variables() == True:
        datos_del_propietario()
    else:
        print("\n\n\n\n\n\n\n\nDebe seleccion la opcion =>: 1")
        menu_opciones(0)
# ----------------------------------------------- FIN DE CODIGO CODIFICACION --------------------------
# ------------------------------------------(*NOMBRE ARCHIVO*) --------------------------------------------


def asignar_nombre_archivo():
    if len(lista_variables) > 0 and len(lista_lineas_codigo) > 0:
        nombre_archivo .append(str(
            input("Ingrese el nombre de archivo (sin la extension): ")))
    else:
        print("\n\n\n\n\n\n\n\nDebe seleccion la opcion =>: 1")
        menu_opciones(0)
# ------------------------------------------(*FIN ARCHIVO*) --------------------------------------------
# ------------------------------------------(*CREAR SCRIPT*) --------------------------------------------


def crear_script():
    print(lista_variables)
    print(datos,sep=",")
    print(nombre_archivo[0],linesep)
    print("PULSE ENTER PARA CREAR EL ARCHIVO")
    # esperar hasta que se haga enter
    m.getch()
    file = open("C:/Users/USUARIO/Desktop/proyecto Python/prueba4.cpp", "w")
    file.write('print("INGRES UN VALOR")' + os.linesep)
    file.write("Armando Celular con las siguientes apps: \n")
    file.write("Lista de Apps: "+lista_variables[0]+"  "+lista_variables[1]+"  "+lista_variables[2]+"  "+lista_variables[3]+"  "+lista_variables[4]+"  "+lista_variables[5]+"  "+lista_variables[6]+"  "+lista_variables[7]+"  "+lista_variables[8]+"  "+lista_variables[9]+"  "+ os.linesep)
    file.write("Propietario: "+ os.linesep)
    file.write("Nombre: "+ datos[0]+ os.linesep)
    file.write("Apellido : "+ datos[1]+ os.linesep)
    file.write("C.I. : "+ datos[2]+ os.linesep)
    file.write("| |")
    file.close()
   


# ------------------------------------------(*FIN SCRIPT*) --------------------------------------------


def menu():
    print("\n\n\n\n\n\n\n\n")
    print("")
    print("██████╗░██████╗░░█████╗░░██████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░  ██╗░░░██╗███╗░░██╗")
    print("██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗████╗░████║██╔══██╗  ██║░░░██║████╗░██║")
    print("██████╔╝██████╔╝██║░░██║██║░░██╗░██████╔╝███████║██╔████╔██║███████║  ██║░░░██║██╔██╗██║")
    print("██╔═══╝░██╔══██╗██║░░██║██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║██╔══██║  ██║░░░██║██║╚████║")
    print("██║░░░░░██║░░██║╚█████╔╝╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║██║░░██║  ╚██████╔╝██║░╚███║")
    print("╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚══╝")
    print("")
    print("░█████╗░███████╗██╗░░░░░██╗░░░██╗██╗░░░░░░█████╗░██████╗░  ███████╗███╗░░██╗")
    print("██╔══██╗██╔════╝██║░░░░░██║░░░██║██║░░░░░██╔══██╗██╔══██╗  ██╔════╝████╗░██║")
    print("██║░░╚═╝█████╗░░██║░░░░░██║░░░██║██║░░░░░███████║██████╔╝  █████╗░░██╔██╗██║")
    print("██║░░██╗██╔══╝░░██║░░░░░██║░░░██║██║░░░░░██╔══██║██╔══██╗  ██╔══╝░░██║╚████║")
    print("╚█████╔╝███████╗███████╗╚██████╔╝███████╗██║░░██║██║░░██║  ███████╗██║░╚███║")
    print("░╚════╝░╚══════╝╚══════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚══════╝╚═╝░░╚══╝")
    print("")
    print("██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗  ██████╗░░█████╗░██████╗░░█████╗░  ░█████╗░░░░░░░░░░░░░░░")
    print("██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗░░██╗░░░░██╗░░")
    print("██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║  ██████╔╝███████║██████╔╝███████║  ██║░░╚═╝██████╗██████╗")
    print("██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║  ██╔═══╝░██╔══██║██╔══██╗██╔══██║  ██║░░██╗╚═██╔═╝╚═██╔═╝")
    print("██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║  ██║░░░░░██║░░██║██║░░██║██║░░██║  ╚█████╔╝░░╚═╝░░░░╚═╝░░")
    print("╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░░░░░░░░░░░░░░░")
    print("")
    print("-------------------------------------------------------------------------------")
    print("------------- PROYECTO: CONVERSOR DE CODIGO Y CREADOR DE ARCHIVOS --------------")
    print(" MENU:")
    print(" 1: Instalar Aplicaciones")
    print(" 2: Firma de Propietario")
    print(" 3: Nombre de archivo")
    print(" 4: Crear script")
    print(" 5: Finalizar")


def menu_opciones(opcion):
    if opcion == 1:
        variables()
    elif opcion == 2:
        definir_codificacion()
    elif opcion == 3:
        asignar_nombre_archivo()
    elif opcion == 4:
        crear_script()  


selecion_opcion = 0
while selecion_opcion < 5:
    menu()
    selecion_opcion = int(input("Ingrese Opcion: "))
    menu_opciones(selecion_opcion)
    #2os.system("cls")
