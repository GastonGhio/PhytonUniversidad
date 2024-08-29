def calculadorOrden():
    sumaT = A + B
    sumaT.sort(reverse=True)
    return sumaT


A = []
B = []

n = int(input("ingrese numero de componentes de la lista respuesto de 208"))
m = int(input("ingrese numero de componentes de la lista respuesto de Gol trend"))

for i in range(n):
    repuesto = int(input("ingrese precio de las piezas de 208"))

    if repuesto != 0 and repuesto > 0:
        A.append(repuesto)

for i in range(m):
    repuesto = int(input("ingrese precio de las piezas de GOL trend"))

    if repuesto != 0 and repuesto > 0:
        B.append(repuesto)

sumaT = calculadorOrden()
print("el orden de los repuestos odenador es ", sumaT)

