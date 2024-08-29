A = []
B = []
C = []

def cargar():
    cont_A = 0
    cont_B = 0
    while cont_A < 10 or cont_B < 10:
        if cont_A < 10:
            num = int(input("Ingrese un número par para A: "))
            if num % 2 == 0:
                A.append(num)
                cont_A += 1
            else:
                print("El número ingresado no es par.")
        if cont_B < 10:
            num1 = int(input("Ingrese un número divisible por 5 para B: "))
            if num1 % 5 == 0:
                B.append(num1)
                cont_B += 1
            else:
                print("El número ingresado no es divisible por 5.")
def combinar(a,b):
    C = a + b
    return C

def maxB (a):
    max = 0
    for i in range (a, len(a)):
        if a[i] > max:
            max = a[i]
            pos = i
    print("el maximo es ", max)
    print("la posicio del maximo es ", pos)
    for i in range(pos+1, len(a)):
        a[i]=0
    return
def prom(a):
    total= 0
    contador = 0
    for i in range (a, len(a)):
        total = total + a(i)
    promedio=total/len(a)
    for i in range (a, len(a)):
        if prom>a[i]:
            contador = contador + 1
    print("la cantidad por encima del promedio es", contador)
    return promedio

cargar()
C= combinar(A,B)
A.reverse ()
maximo_B = maxB(B)
promedio = prom(C)
print("el promedioes ", promedio)
print("Lista A:", A)
print("Lista B:", B)
print("la compbinacion es ", C)