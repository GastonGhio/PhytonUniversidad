
#cont = 0
#while cont < 100:

 #   num = int(input("ingrese numero"))
  #  cont += 1

   # operacion = int(input("seleccion opracion 1.factorial del numero , 2. potencia, otro numero. recibira si su numero es par o impar "))

    #if operacion == 1:

    ##EJERCICIO 4

#acum = 0
#mayor = 0

#for i in range (1,6):
 #   curso=int(input("ingrese curso"))
  #  presentes = int(input("ingrese numero de presentes del dia"))
   # ausentes = int(input("ingrese numero de ausentes"))
 #   total = presentes + ausentes
  #  porcentaje = presentes*100/total
   # print("del curso ", i , " el procentaje de presentes es ", porcentaje)
  #  acum = acum+ausentes

#print("el total de ausentes del dia fue de ", acum)

"""
EJERCICIO 6

totalSalary = 0
mayorSueldo = 0
acum = 0
totalA1 = 0
totalA2 = 0
totalA3 = 0
while acum <= 4:
    name = input("ingrese nombre del chango")
    category = int(input("ingrese categorioa 1 , 2, 3"))
    if category == 1 :
        salary = 150000
        acum = acum + 1
        totalA1 = totalA1 + salary
    elif category == 2 :
        salary = 400000
        acum = acum + 1
        totalA2 = totalA2 + salary
    elif category == 3:
        salary = 700000
        acum = acum+1
        totalA3 = totalA3 + salary
    else:
        print("debe ingresar numero del 1 al 3")
    totalSalary = totalSalary + salary
print("el total de salarios de la categoria 1 es ", totalA1,  "el total a2 ", totalA2, "el total a3 ", totalA3)
print("el total de salarios es ", totalSalary)
"""

"""EJERCICIO 6 MOD COMO DICE LKA PROFE """


"""counter = 0
mayor200 = 0
men500A1 = 0
mayorSalary = 0
totalSalary = 0
salaryA1 = 0
salaryA2 = 0
salaryA3 = 0

while counter < 100:
    name = input("employer name")
    salary = int(input("put salary employer"))
    category = int(input("pone la category compa"))
    if category == 1 or category == 2 or category == 3:

        if category == 1:
            salaryA1 = salaryA1 + salary
        elif category == 2:
            salaryA2 = salaryA2 + salary
        elif category == 3:
            salaryA3 = salaryA3 + salary


 2       if salary > 200000:
            mayor200 = mayor200 + 1
        if salary < 500000 and category == 1:
            men500A1 = men500A1 + 1
        if salary > mayorSalary :
            mayorSalary = salary
            employerExp = name
        counter = counter + 1
        totalSalary = totalSalary + salary
    else:
        print("entre 1 y 3 la concha de tu madre")
print (" el total de salarios que paga la empresa es ", totalSalary)
print (" empleados q cobran mas de 200 ", mayor200)
print(" catn empleados cobran menos de 500 cat a 1", men500A1)
print("empleado q mas gana ", employerExp)
print("el total de sueldos de  A1 A2 Y A3 ES ", salaryA1, salaryA2, salaryA3)
"""

"""class celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

celular1= celular("Samsung", "S23 ultra")
celular2 = celular("iphone", "15 Pro Max")

print(celular1.marca)
"""

"""class estudiante:
    def __init__(self, nombre,edad,grado):
        self.nombre = nombre
        self.edad= edad
        self.grado= grado

    def estudiar(self):
        print(f"el estudiante {estudiante.nombre} esta estudiando")

estudiante = estudiante("jorge",23,3)

while True:
    estudiar= input("ingrese paslabra estudiar")
    if (estudiar.lower() == "estudiar"):#es parab q si escriben en mayuscula o minuscula lo tome igual al llamado a la funcion
        estudiante.estudiar()"""


# HERENCIA DE CLASES DE PERSONA SE HEREEDA A EMPLEADO Y ROBERTO AGARRA LAS HERENCIASA DE PERSONA A APWESAR DE SER EMPLEADO

"""class empleado(persona):
    def __init__(self,nombre,edad,nacionalidad,chamba,salario):
        super().__init__(nombre,edad,nacionalidad) #hereda de la classe pldre
        self.trabajo = chamba
        self.salario = salario
"""
"""class estudiante(persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad) #hereda de la classe pldre
        self.notas = notas
        self.universidad = universidad"""
class persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad= edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("hola estoy hablando")
class artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrarHabilidad(self):
        print(f"mi habilidad es {self.habilidad}")

class empleadoArtista(persona,artista):  ## ejemplo de herencia multiple
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        persona.__init__(self,nombre,edad,nacionalidad)
        artista.__init__(self,habilidad)
        self.salario=salario
        self.empresa=empresa

    def presentarse(self):
        print( f"hola mi nombre es {self.nombre}, trabajo en {self.empresa}, tengo un salario de {self.salario}")



roberto = empleadoArtista("roberto",33,"bolita","programador",1500, "ibm")

roberto.presentarse()

herencia = issubclass(empleadoArtista,persona)
print(herencia )



