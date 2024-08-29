def mostrar(a,b):
    for i in range(0,b):
        print(a[i])
    return

def cargar(a):
    i=0
    j=5
    cont=0
    num=int(input("ingrese numero"))
    while cont < 10:
        if num >0 and i<5:
            a[i]=numi=i+1
            cont=cont+1
        if num <0 and j<10:
            a[j]=numj=j+1
            cont=cont+1
        num=int(input("ingrese numero"))
    return

def promedio(a):
    cont=0
    acum=0
    for i in range(5,len(a)):
        acum=acum+a[i]
    prom=acum/5
    print("el promedio es", prom)
    return

def generar (a,b):
    j=0
    for i in range(0,lent(a)):
        if a[i]%4 ==0:
            b[j]=a[i]
            j=j+1
    return j

def cantidad(a,b):
    cont=0
    cont3=0
    for i in range(0,b):
        if a[i]%2==0:
            cont=cont+1
        if a[i]%3==0:
            cont3=cont3+1
    print("cantidad de pares", cont)
    print("cantidad de multiplos de 3", cont3)
    return




vec = [0]*10
vec1=[0]*10

cargar(vec)
print("arreglo")
mostrar(vec,10)
promedio(vec)
vec.sort()
mostrar(vec,10)
m=generar(vec,vec1)
if==m:
    print("no hay multiplos de  14")
else:
    mostrar(vec1,m)