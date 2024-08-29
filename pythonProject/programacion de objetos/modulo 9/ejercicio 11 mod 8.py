def mostrar(arreglo):
    for i in range(0, len(arreglo)):
        print(arreglo[i], i + 1)

def calculoMaximo(arreglo):
    max=0
    for i in range (0,len(arreglo)):
        if arreglo[i] > max:
            max = arreglo[i]
            posicion = i  # en caso de seer la mayor gurarda i como posicion
    return posicion


cursoA = []
cursoB = []


for i in range (0, 2):
    alturaA = (float(input("agrege altura de alumno curso A")))
    cursoA.append(alturaA)
for i in range(0, 2):
    alturaB = (float(input("agrege altura de alumno curso b")))
    cursoB.append(alturaB)

mostrar(cursoA)
mostrar(cursoB)
maxA = calculoMaximo(cursoA)
print("la altura maxima dl curso A y su lugar es ", cursoA[maxA], maxA+1)

maxB = calculoMaximo(cursoB)
print("la altura maxima dl curso b y su lugar es ", cursoB[maxB], maxB+1)

if cursoA[maxA]> cursoB[maxB]:
    print ("la altura mayor es la del curso A")
elif cursoA[maxA] <cursoB[maxB]:
    print("la altura mayor es la del curso B")
else:
    print("los curson coinciden en altura maxima")