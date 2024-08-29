A = [0]*8
B = []

def generar(a ,b):
    contador=0
    acumulador = 0
    while contador < 15:
        try:

            num = int(input("ingrese numer"))
            contador = contador +1
            if num > 20 and acumulador < 8:
                a[acumulador]= num
                acumulador =acumulador + 1
            if num < 20:
                b.append(num)
            if len(a) ==0 :
                print("no hay numeros superiopres a 20")
        except ValueError:
            print("debe ingresar un numero")



    #si no alcanza q repita
    while acumulador < 8:
        a[acumulador]= a[acumulador - 1] #posicion ultima
        acumulador = acumulador + 1

def promedio (a):
    total=0
    prom = 0
    if len(a) != 0:
        for i in range (len(a)):
            total= total + a[i]
        prom = total / len(a)
    return prom
def maxN(a):
    maximo= a[0]
    anterior = a[0]
    for i in range(1, len(a)):
        if a[i] > maximo:
            maximo = a[i]
            anterior = a[i - 1]
    print("el elemento maximo es", maximo, "y el anterior es ", anterior)


generar(A, B)
prom = promedio(B)
maximo = maxN(A)
print("el promedio es" , prom)
print("Lista A:", A)
print("Lista B:", B)