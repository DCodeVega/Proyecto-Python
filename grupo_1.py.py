
import os
import msvcrt as m

# ------------------------------------------- VARIABLES GLOBALES ------------------------------------
# ---- CREANDO UNA LISTA VACIA -----
lista_variables = []
lista_lineas_codigo = []
nombre_archivo = []

# ----(*VARIABLES*) VALIDA EL INGRESO DE DATOS POR TECLADO, OBLIGANDO QUE SEA NUMERICO --------------


def validar_si_numero():
    cantidad_variable = input("Ingrese la cantidad de variables a usar: ")
    if cantidad_variable.isnumeric() == True:
        return int(cantidad_variable)
    else:
        return 0


def asignar_variables(num_variable):
    for i in range(1, num_variable+1):
        variable = input("Ingrese el "+str(i)+" Variable: ")
        lista_variables.append(variable)


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


def asignar_filas(num_filas):
    for i in range(1, num_filas+1):
        codigo = input("Escriba codigo en la linea "+str(i)+": ")
        lista_lineas_codigo.append(codigo)


def definir_codificacion():
    if verificar_lista_variables() == True:
        cantidad_fila = validar_si_numero_codificacion()
        # ---- MIENTRAS SEA 0 ----
        while cantidad_fila == 0:
            cantidad_fila = validar_si_numero()
        asignar_filas(cantidad_fila)
    else:
        print("Debe seleccion la opcion =>: 1")
        menu_opciones(0)
# ----------------------------------------------- FIN DE CODIGO CODIFICACION --------------------------
# ------------------------------------------(*NOMBRE ARCHIVO*) --------------------------------------------


def asignar_nombre_archivo():
    if len(lista_variables) > 0 and len(lista_lineas_codigo) > 0:
        nombre_archivo .append(str(
            input("Ingrese el nombre de archivo (sin la extension): ")))
    else:
        print("Debe seleccion la opcion =>: 1")
        menu_opciones(0)
# ------------------------------------------(*FIN ARCHIVO*) --------------------------------------------
# ------------------------------------------(*CREAR SCRIPT*) --------------------------------------------


def crear_script():
    print(lista_variables)
    print(lista_lineas_codigo)
    print(nombre_archivo[0])
    # esperar hasta que se haga enter
    print(lista_variables[0])
    print("este es el elemento")
    m.getch()

    file = open("C:/Users/LAB-INTER 2/Desktop/proyecto/proytcsuma.cpp", "w")
    file.write("#include<iostream>\n#include<conio.h>\n"+ os.linesep)
    file.write("using namespace std;\n int main()\n{\n")
    file.write("int "+lista_variables[0]+","+lista_variables[1]+";\n")
    file.write("int suma;\n")
    file.write('cout<<"introdusca elemento '+lista_variables[0]+'"<< endl;\ncin>>'+lista_variables[0]+';')
    file.write('cout<<"introdusca elemento '+lista_variables[1]+'"<< endl;\ncin>>'+lista_variables[1]+';')
    file.write("suma="+lista_variables[0]+"+"+lista_variables[1]+";")
    file.write('cout <<"resultado de la suma es = " <<suma ;\n}')
    file.write('retunr 0;')
    file.close()


# ------------------------------------------(*FIN SCRIPT*) --------------------------------------------


def menu():
    print("-------------------------------------------------------------------------------")
    print("------------- PROYECTO: CONVERSOR DE CODIGO Y CREADOR DE ARCHIVOS --------------")
    print(" MENU:")
    print(" 1: Variable")
    print(" 2: Realizar la codificacion")
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
