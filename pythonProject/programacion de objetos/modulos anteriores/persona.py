
#LAS CLASES SON COMO CAJAS

#TE AVISA Q ESA CLASE ESTA SIENDO USADA EN ALGUNOS LUGARES
class persona: #INIT ME PERMITE AGREGARLE ITEMS A LAS CLASES
    def __init__(self, nombre, apellido, dni, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        #PONIENDO EL SELF.XX = XX LO Q HAGO  ES ANEXAR ESE PARAMETRO COMO PROP[IEDAD DEL OBJETO

    def __str__(self): #ACA HAGO Q RETORNE ESTOS DATOS COMO DATOS A MOSTRAR EN CASO DE QUERER HACERLO AL CONFIRMAR
          return self.nombre + " " + self.apellido + " - " + self.dni


#ESTA FUNCION LA VAN A HEREDAR CLIENTE Y EMPLEADO
