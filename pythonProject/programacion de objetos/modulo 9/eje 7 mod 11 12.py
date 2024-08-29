A = []
B = []

def generar(a, b):
    try:
        num = int(input("ingrese numero principal"))
        if num !=0:

            contador = 0
            while contador < 12:
                num2 = int(input("ingrese numero"))
                b.append(num2)
                contador = contador + 1
                if num2 %num==0:
                    a.append(num2)
                if len(a)==0:
                    print("no hay numeros multiplos del numero principal")
        else:
            print("el numero principal no puede ser 0")
    except ValueError:
        print("debe ingresar numero no caracter")

def formular(a):
    cantidadMultiplos = 0
    producto = 1
    sumatoria = 0
    for i in range(len(a)):
        if a[i] %4== 0:
            cantidadMultiplos = cantidadMultiplos + 1
        if i %2==0:
            producto = producto * a[i]
        if a[i] %3 ==0:
            sumatoria = sumatoria + a[i]
            if sumatoria == 0:
                sumatoria = "no hay numeros multiplos de 3"


    print("la cantidad de multiplos de 4 es ", cantidadMultiplos)
    print("el producto de los numeros en posiciones pares es ", producto)
    print("la sumatoria de los numeros d 3 es ", sumatoria)

def max(a):
    consecutivo = a[0]
    maximo = a[0]
    for i in range (len(a)):
        if a[i] > maximo and i < len(a) -1 :
            maximo = a[i]
            consecutivo = a[i + 1]
            a.append(consecutivo)
    return consecutivo

def mostrar (a):
    for i in range (len(a)):
        print (a[i])


generar (A,B)
print ("el arreglo es ", A)
formular(B)
siguiente = max(B)
print(" el numero consecutivo al maximo es el ", siguiente)

mostrar (B)

B.sort()
mostrar (B)

