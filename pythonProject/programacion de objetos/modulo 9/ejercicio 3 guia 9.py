def calculacion (a):
    suma = 0
    for i in a:
        suma += i
    promedio = suma / len(a)  if len(a) > 0 else 0
    return suma, promedio

numPosi = []
numNega = []


for i in range(10):
    n =int(input('ingrese numero'))

    if n != 0:    #hace q solo se agrege el numero a los arreglos si son distints de  0, moy bueno
        if n > 0:
            numPosi.append(n)
        if n < 0:
            numNega.append(n)

sumaPosi, promPosi= calculacion(numPosi)
print("la sumatoria de positivos es ", sumaPosi, " y el promedio es ", promPosi)

sumaNega, promNega = calculacion(numNega)
print("la sumatoria de negativos es ", sumaNega, " y el promedio es ", promNega)