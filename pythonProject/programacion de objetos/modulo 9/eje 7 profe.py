def generar(arreglo, n):
    for i in range(0,n):
        arreglo.append(int(input("ingres elemento del arreglo)")))

def inter(arreglo1, arreglo2, comunes):
    for i in range(0,len(arreglo1)):
        for j in range (0,len(arreglo2)):
            if(arreglo1[i]==arreglo2[j]): # esto es por si dos cosas en el areglo son iguales, que los sume a comunes
                comunes.append(arreglo1[i])
            else:
                comunes.append ("no hay numero repetidos")

def mostrar(arreglo):
    for i in range(0, len(arreglo)):
        print(arreglo[i])

a=[]
b=[]
c=[]
n=int(input("ingresar numero de elemtnos del primr arreglo"))
generar (a,n)
m=int(input("ingresar elementos del segundo arreglo"))
generar(b,m)
inter (a, b, c)
print("los siguientes arreglos pertecen a ambas listas y estan repetidos, ")
mostrar(c)
