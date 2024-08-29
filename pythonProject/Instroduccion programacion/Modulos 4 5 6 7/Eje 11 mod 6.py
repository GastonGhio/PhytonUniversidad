
cont = 0

while cont < 1:
    llamada = int(input("ingrese tipo llamada 1. local 2. limitorfe 3. interplanetario "))
    if llamada == 1 or llamada == 2 or llamada ==3:
        duracion = float(input("ingrese cantidad de minutios"))
        if llamada == 1:
            monto = duracion * 0.25
        elif llamada == 2:
            monto = duracion * 0.5
        elif llamada == 3:
            monto = duracion * 1.5
        cont = 1
print("el monto de la llamda es", monto)




