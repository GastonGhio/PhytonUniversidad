# EJERCICIO 1
"""
a. Se carga A con 10 números pares y B con 10 números múltiplos de 5.   X
b. Cargar el arreglo C con la suma de cada elemento de A con cada elemento
de B.X
c. Cargar el arreglo D con los todos los elementos de A y a continuación todos
los elementos de B.X
d. Invertir el arreglo A sobre sí mismo.
e. Buscar la posición del máximo de B. Mostrar la posición del máximo y el valor
del máximo. Poner en cero los valores a la derecha del máximo.
f. Encontrar el promedio de C. Contar cuántos valores hay en C por encima de
ese promedio
"""
"""
def charge(a,b,c):
    while (len(a)<10 or len(b)<10):
        num=int(input("agus ingresa un numeragus par o multiplo de 5"))
        if (num%2==0 and len(a)<10):
            a.append(num)
        if (num%5==0 and len(b)<10):
            b.append(num)
    for i in range(len(a)):
        sumatory = a[i] + b [i]
        c.append(sumatory)

    return a, b, c
def combitrant(a,b):
    d = a + b
    return d

def maximo(a):
    pos=0
    max =0
    for i in range(len(a)):
        if a[i] > a[pos]:
            pos = i
            max= a[i]

    for j in range(pos+1,len(a)):
        a[j] = 0

    print("el arreglo con los ceros es", a)
    return pos, max

def average(a):
    total=0
    cont = 0
    for i in range(len(a)):
        total += a[i]

    prom= total/len(a)

    for i in range(len(a)):
        if a[i] > prom :
            cont += 1
    return prom, cont


arraiPar= []
arraiMulti=[]
arraiMix=[]



charge(arraiPar,arraiMulti,arraiMix)
arraiTwo=combitrant(arraiPar,arraiMulti)
print("el arreeglo de numeros pares es ", arraiPar)
print(" este es el arreglo de numeros multiplos de 5 ",arraiMulti)
print("este es el arreglo de la suma de los dos arreglos " ,arraiMix)
print("este es el arreglo  d ",arraiTwo)
arraiPar.reverse()
print("este es el arreglo invertido ",arraiPar)
posMax, max= maximo(arraiMulti)
print("la posicion del maximo del arreglo B es ", posMax+1, " y el vaslor es ", max)
avg ,mayoresAvg = average(arraiMix)
print (" el promedio del arreglo C es ", avg, " y los numeros mayores al promedio son ", mayoresAvg)
"""

#EJERCICIO 2
"""
 Leer 15 números y generar un arreglo con los primeros 8 números mayores que 20.
Si no hay 8 números que cumplan la condición, repetir el primero hasta completar
el arreglo. Si ningún número era mayor que 20, mostrar mensaje y salir.
a. Calcular el promedio de los números que no entraron en el arreglo.
b. Buscar el máximo elemento y mostrar el elemento que esté en la posición
anterior.
c. Mostrar el factorial de los elementos de posición par del arreglo."""

"""
def chargeAndComplete (a, b):
    for i in range(15):
        num = int(input("ingrese numeragus mayor a 20agus"))
        if num > 20 and len(a) < 8:
            a.append(num)
        else:
            b.append(num)

    if len(a) > 0:
        while len(a) < 8:
            a.append(a[0])
    else :
        print("no hay numeros mayores a 20")

    return a, b

def average(a):
    total= 0
    for i in range (len(a)):
        total += a[i]

    avg = total/ len(a)

    return  avg

def max(a):
    pos=0
    vmax=0
    for i in range(len(a)):
        if a[i] > vmax:
            vmax = a[i]
            posAnt = i

    return vmax, posAnt

def fact (a):

    for i in range (len(a)):
        sum = 0
        factor=1
        if a[i]%2==0:
            sum += a[i]
    for i in range(1, sum+1):
        factor *= i
    return sum ,factor



arraiMayor=[]
arraiNoMayor=[]
mayores, otros = chargeAndComplete(arraiMayor, arraiNoMayor)
print ("arreglo mayor a 20", mayores, "menores o mayores a 20 lleno ", otros)

print("el promedio es de los numeros no mayores a  20 eso con arreglo 1 completo es ", average(otros))
maximo, posicion = max(mayores)
print("el numero anterior al maximo es ",mayores[posicion], " y el maximo es ", maximo)
sumatoria , factorial= fact(mayores)
print ("la sumatoria de los numeros pares es ", sumatoria, " y el factorial de los numeros pares del arreglo de mayores a 20 es ", factorial)

"""
"""nombre = input("ingrese nombre").upper()
while nombre.isspace() or nombre == "":
    nombre=input("dene inghresar un nopmbre correcto").upper()
"""


"""una empresa se dedica a encuestar personas y para ello necesita ingresar los datos de sus encuestados mediante un programa os datos de entrada que se solicitan cargar son:
 HELP CENTER
Tipo de encuesta realizada (1- Telefónica, 2-Presencial). Documento de la persona encuestada • Sexo de la persona encuestada (M/ P Cantidad de hijos de la persona encuestada
y edades de los mismos
 a carga de datos finaliza cuando en el tipo de la encuesta se lee "FIN"

 1 Al finalizar el proceso. el programa debe mostrar por pantalla: Porcentaje de encuestados por cada tipo de encuesta 
 2 Si el sexo es "M" y tiene mas de 2:hijos.
   promediar las edades de los mismos 
 3 cual tue el grupo personas que mas se encuesto segun su sexo 
 4 El documento de la persona encuestada que tiene el hijo de mayor edad 
"""

"""def cargar(a, b, c):

    tipoEncuesta= input(" ingrese tipo de encuesta , 1-telefonica , 2 - presencial")

    while tipoEncuesta.isspace()  or (tipoEncuesta != "1" and tipoEncuesta != "2") :
        tipoEncuesta = input(" ERROR! debe ingresar un correcto tipo de encuesta 1 , 2")

    a.append(tipoEncuesta)




    while tipoEncuesta.upper() != "FIN":

        #DOCUMENTO
        documento = input("ingrese numero de documento")
        while documento.isspace() or documento=="":
            documento = input("ERROR debe ingrese numero de documento")

        #GENERO
        genero = input("ingrese su genero, 1- masculino  , 2 - femenino")

        while genero.isspace() or (genero != "1" and genero != "2"):
            genero = input(" ERROR! debe ingresar un correcto tipo de genero 1 , 2")

        b.append(genero)

        #HIJOS
        question= input("tiene hijos?")

        while question.isspace() or (question.upper() != "SI" and question.upper() != "NO"):
            question = input(" ERROR! debe ingresar si tiene hijos si o no")

        if question.upper() == "SI":
            edadMax = 0
            totalEdad=0
            cantHijos=int(input("ingrese cantidad de hijos"))
            while cantHijos <= 0:
                cantHijos = int(input("error ingrese cantidad de hijos"))

            for i in range (cantHijos):
                edad= int(input("ingrese edad de su hijo"))
                while edad <= 0:
                    edad = int(input("ERROR ingrese edad de su hijo"))
                totalEdad += edad
                if edadMax < edad:
                    edadMax = edad
                    doc = documento



        else:
            print("no tiene hijos")


        if genero == "1" and cantHijos >= 2:
            avgEdad = totalEdad/cantHijos
            c.append (avgEdad)


        tipoEncuesta = input(" ingrese tipo de encuesta , 1-telefonica , 2 - presencial o fin para salir")
        while tipoEncuesta.isspace() or (tipoEncuesta != "1" and tipoEncuesta != "2" and tipoEncuesta.upper() != "FIN"):
            tipoEncuesta = input(" ERROR! debe ingresar un correcto tipo de encuesta 1 , 2 o fin para salir definitivamente ")
        if tipoEncuesta.upper() != "FIN":
            a.append(tipoEncuesta)

    return doc

#PROMEDIOD E ENCUESTADOS DE CADA TIPO
def porcentaje (a):
    encuestados =0
    telefonica= 0
    presencial=0

    for i in range (len(a)):
        if a[i] == "1":
            telefonica +=1
        elif a[i] == "2":
            presencial += 1
        encuestados +=1

    print( "la cantidad de encuestados por telefono es de %", (telefonica/encuestados * 100), " la cantidad de encuestados presencial es de % ", (presencial/encuestados*100))

#PORCENTAJE DE CADA GENERO
def porcentajeGenero (a):
    encuestados = 0
    masculino = 0
    femenino = 0

    for i in range(len(a)):
        if a[i] == "1":
            masculino += 1
        elif a[i] == "2":
            femenino += 1
        encuestados += 1

    if masculino > femenino :
        print (" el grupo masculino fue el mas encuestado")
    elif femenino > masculino :
        print("el grupo femenino fue el mas encuestado")


consultaTipo = []
sexo = []
masDosHijos =[]

docMayor = cargar(consultaTipo, sexo, masDosHijos)
porcentaje(consultaTipo)
porcentajeGenero(sexo)
print(" el promedio de las edades de los masculinos que poseen mas de dos hijos son ", masDosHijos)
print (" el documento del padre con el hijo de mayor edad es ", docMayor)

"""
"""
Una empresa de comidas rápidas, precisa que se desarrolle un sistema en que los empleados puedan tomar Ios pedidos de los clientes,
calcular el precio y el vuelto que deben entregar en caso de que los mismos abonen en efectivo. 

El empleado deberá poder ejecutar las siguientes acciones: 
1) Cargar pedido: (La carga contnua mientras producto sea distinto de FLAN) 
Los datos para cargar en cada pedido serán los siguientes: Producto: Hamburguesa 0 Nuggets. ($ 500 o $300) 
Papas Fritas, debe informar el tamano (G ->$300, M-> $200, C-> $100) .
• Bebida (Cola, Agua, Lima) -> $600 
Total (El total debe ser calculado segun lo pedido por cada cliente y guardado en una lista/arreglo) 
La informacion debera ser guardada utilizando arreglos paralelos.

2) determinar funcion producto menor vendido hambug o nuggets

3) porcentaje de ventas de LIMA

4) calcular el total 


"""

def pedido(a):
    totalProd=0
    sesion=input("quiere ingresar pedido 1 - SI ,   2- NO")
    while sesion != "1" and sesion != "2":
        sesion = input("quiere ingresar pedido 1 - SI ,   2- NO")

    if sesion == "1":

        producto = input("ingrese pedido  1 - BURGER , 2- NUGGETS O FLAN para continuar")
        while producto.lower() != "flan":

            while producto.lower() != "burger" and producto.lower() != "nuggets" and producto.lower() != "flan":
                producto = input(" error debe ingresar pedido -BURGER ,  NUGGETS O FLAN")

            if producto.lower() == "burger":
                totalProd += 600
            if producto.lower() == "nuggets":
                totalProd += 300
            if producto.lower() != "flan":
                a.append(producto)
                producto = input("CARGADO , INGREasar nuevo pedido O flan?")

        print(totalProd)

        if totalProd != 0:
             for i in range (len(a)):

                guarnicion = input("seleccione tamaño de papas fritas , G- GRANDE M-MEDIANO C-CHICO")
                while guarnicion.upper() != "G" and guarnicion.upper() != "M" and guarnicion.upper() != "C":
                    guarnicion = input("ERROR ---- ingrese tamaño de papas fritas , G- GRANDE M-MEDIANO C-CHICO")

                if guarnicion.upper() == "G":
                    totalProd += 300
                if guarnicion.upper() == "M":
                    totalProd += 200
                if guarnicion.upper() == "C":
                    totalProd += 100
        print(totalProd)















    else:
        print("gracias, vuelva a iniciar el programa para encargar")










principal = []


pedido(principal)
print(principal)