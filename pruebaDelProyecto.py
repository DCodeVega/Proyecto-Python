import msvcrt as m


a=[]
def suma():
    if len(a)>0:
        return True
    else:
        return False
def respuesta():
    if suma==True:
        print("es true")
    else:
        print("false")
m.getch()
a=int(input("ingrese un numero: "))
respuesta()