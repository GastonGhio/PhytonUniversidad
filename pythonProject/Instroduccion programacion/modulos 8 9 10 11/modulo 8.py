 # 1 EJERCICIO

"""
arrai = []

n =int(input("ingrese cantidad de numeros de la lista"))

for i in range (0,n):
    arrai.append(int(input("ingrese numero codigo")))
    print("posicion ", i, arrai[i])
print(arrai)

"""

# 2 EJERCICIO
"""
newComp=[]
comp=[]
impar=[]
total=  0
multi = 1
n = int(input("ingrese numero de ciclos"))
for i in range (0, n):
    comp.append(int(input("ingrese n de componente")))
    if i % 2 == 0 and i != 0:
        impar.append(comp[i])
        multi = multi * comp[i]
    else:
        total = total + comp[i]

print("elarreglo es ", comp)
print("el arreglo posicion 4 es ", comp[3])


comp.reverse()
print("Invertida:", comp)
comp.reverse()

print("multiplicado", comp[0]*comp[-1])
print("impares", impar)
print("el total de los impar3es es ", total)
print("el multiplicado de los pares es ", multi)

compA = comp[0]
comp[0] = comp[-1]
comp [-1] = compA

print(comp)
"""

#EJERCICIO 3
"""
a= [11,22,33,44,2,3,4,5,6,7,8,9,1,33,32]
b= [11, 22, 33, 44, 55, 66, 77, 88, 99, 100,101,102,103,104,993]
c= []

for i in range (0,len(a)):
    c.append (a[i])
for i in range (0,len(b)):
    c[i] += b[i]

print(len(c))
print(c)
"""
#EJERCICIO 4
"""
arrai= [22, 44, 66, 88,66, 69, 81, 5, 105, 1829, 109, 111, 8, 137, 1025]
max= 0
min= arrai[0]

for i in range (0, len(arrai)):
    if arrai[i] > max:
        max = arrai[i]
    elif arrai[i] < min:
        min = arrai[i]

print("el maximo es ", max , " y el minimo es ", min)
"""
#EJERCICIO 5

