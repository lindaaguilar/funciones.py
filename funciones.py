def suma (a,b):
    z= a+b
    print(z)
    resta(a,b)
def resta (a,b):
    z=a-b
    print (z)
    multiplicacion(a,b)
def multiplicacion(a,b):
    z=a*b
    print (z)
    division(a,b)
def division (a,b):
    z=a/b
    print(z)
def ingreso():
    a=int(input("ingrese una cantidad"))
    b=int(input("ingerse una cantidad"))
    suma(a,b)
ingreso()
