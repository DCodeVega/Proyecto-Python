
def bienvenida():
    print("Gracias por ingresar")


def muestra():
    d = suma()
    print(f"La suma es: {d}")


def suma():
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    c = a+b
    return c


def gracias():
    print("FIN DE PROCESO")


def main():
    bienvenida()
    muestra()
    gracias()


main()
