#EJERCICIO 1
"""
x = 1
while x != 0 :
    def absolut (a):
        if a < 0:
            a = a*(-1)
        elif a > 0:
            a = a
        else:

            a = "adios vuelva prontos"
        return a

    x = int(input("ingrese numero para obtener absoluto"))
    abs = absolut(x)

    print(abs)

    """

#EJERCICIO 2 Construir una función que permite devolver la potencia de un número ingresando el número y su potencia.

"""
def pot (a, b):
    r = a**b
    return r

x= int(input("ingrese numero a potenciar"))
y= int(input("ingrese numero potencia"))

response = pot(x,y)

print ("el numero resultado de la protencia es ", response)
"""

#EJERCIO 3 Diseñar una función que calcule el triple de un número y otra función que calcule el
#siguiente de un número. Utilizar las funciones en un programa para que ingresado un
#numero muestre el consecutivo del triple del número y el triple del consecutivo del
#número
"""
number=int(input("ingreseun numero"))

def third(a):
    a = a*3
    return a
def follow(a):
    a+= 1
    return a

print("el triple del numero es" ,third(number))
print("el siguiente del numero es ",follow(number))
"""

#EJERCICIO  5 Se ingresan n números. Diseñar un programa que usando una función, muestre la mitad de aquellos que son pares.

"""
def middle (a):
    for i in range (0, len(a)):
        if a[i]%2 == 0:
            middleNum = a[i]//2
            arrai2.append(middleNum)


n =int(input("ingrese cantidad de numeros"))
arrai = []
arrai2= []
for i in range (0, n):
    number = int(input("ingrese numero"))
    arrai.append (number)

middle(arrai)
print(arrai)
print(arrai2)

"""


# EJERCICIO 6
"""
def sumary(a):
    sumatory = 0
    arrai = []
    for i in range(1, a + 1):
        if a % i == 0:
            arrai.append(i)
            sumatory += i
    print("la sumario de los numeros que son divisores de ", a, " son ", sumatory, " y estos son ", arrai)


x = int(input("ingrese un numero"))
sumary(x)
"""


# ejercicio 7
"""
def sumary(a):
    sumatory = 0
    arrai = []
    perfect = "NO ES PERFECTO"
    for i in range(1, a):
        if a % i == 0:
            arrai.append(i)
            sumatory += i
    if sumatory == a:
        perfect = "ES PERFECTO"
    print("la sumario de los numeros que son divisores de ", a, " son ", sumatory, " y estos son ", arrai,
          " y en cuanto a si es numero perfecto... ", perfect)


x = int(input("ingrese un numero"))
sumary(x)
"""

# EJERCICIO 8 numeros primos
"""
arraiCousin = []
arraiNoCousin = []


def cousin(x):
    cont = 0
    for i in range(1, x):
        if x % i == 0:
            cont += 1
    return cont


m = int(input("ingrese valor inferior"))
n = int(input("ingrese valor superior"))

for i in range(m, n):
    a = cousin(i)
    if a == 0 or a == 1 and n != 1:
        arraiCousin.append(i)

    else:
        arraiNoCousin.append(i)

print(arraiCousin, " son los  primos del 100 al 200")
print(arraiNoCousin, " son los no primos del 100 al 200")
"""

#EJERCICIO DE ENTREGA MODULO 9
"""
cont=0
while cont < 3:
    def friendly(a,b):
        sumatory1=0
        sumatory2=0
        for i in range (1,a):
            if a % i ==0:
                sumatory1 += i
        for i in range (1,b):
            if b % i == 0:
                sumatory2 += i

        if (sumatory1 == b and sumatory2 == a):
            c = "son numeros amigos"
        else:
            c = "no son numeros amigos"

        return c

    number1=int(input("ingrese numero amigo 1"))
    number2=int(input("ingrese numero amigo 2"))
    response=friendly(number1, number2)
    print(response)
    cont +=1
    """