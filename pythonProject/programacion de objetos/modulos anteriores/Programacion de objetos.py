#funcion class crea un objeto y se le puede anexar funciones diversas y caracteristicas

#class Cuadrado:
#    def __init__(self, ancho, alto):
 #       self.ancho = ancho
  #      self.alto = alto

   # def CalculoArea(self):
    #    area = self.ancho * self.alto
     #   return area

#figura = Cuadrado(10, 12)

#print(figura.CalculoArea())


#VAMOS A CREAR EL ARRAY BIEN HECHO

#TENEMOS Q IMPORTAR EMPLEADO Y CLIENTE


from cliente import cliente
from empleado import empleado



emp = empleado('jorge', 'guiller', '31211233', '115515532', '1000')
cli = cliente('lautaro', 'casillo', '215145', '151425624', 'vip')



def cargar():
    respuesta = input('nuevo empleado?')
    nombre = input('ingrese su nombre')
    apellido = input('ingrese su apellido')
    dni = input('ingrese su dni')
    telefono = input('ingrese su tel')

    if respuesta == 'si':
        salario = input('ingrese salario del empleado')
        emp = empleado(nombre, apellido, dni, telefono, int(salario))
        personas.append(emp)
    else:
        categoria = input('ingrese categoria del cliente nuevo')
        cli = cliente(nombre, apellido, dni, telefono, categoria)
        personas.append(cli)


personas = []
cargar()

for persona in personas:
    print(persona)