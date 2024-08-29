def cargar(a):
    cont=0
    i=0
    j=1
    while(cont<12):
        num=int(input("ingrese numero"))
        if num%2==0 and i<12:
            a[i]=num
            i=i+2
            cont +=1
        if num<0 and j<12:
            a[j]=num
            j=j+2
            cont +=1
    return

def mostrar(a):
    for i in range(0,len(a)):
        print(a[i])

def generar(a, b):
    for i in range(0,len(a)//2):
        b[i]=a[i]/2
    for i in range (5, len(a)):
        b[i]=-a[i]
    return

def eliminar(a):
    cont=0
    for i in range (0,len(a)):
        if a[i] %4==0:
            a.remove(a[i])
            cont=cont+1
    return cont

vec = [0]*12
vec1=[0]*12
cargar(vec)
mostrar(vec)
vec.reverse()
mostrar(vec)
vec.reverse()
generar(vec, vec1)
mostrar(vec1)
vec.sort()
mostrar(vec)
dim=eliminar(vec)
for i in range(0,dim):
    print(vec[i])
