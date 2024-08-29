#nombre = input('what is your name?')
#print('hola ' + nombre)

#edad = int(input('how age?'))

#if edad > 18:
#    print('Acesso permitido')
#else:
#    print('No acesso es menor de edad')

#def mostrarPrecioFinal(producto, precio, descuento):
#    precioFinal = precio - descuento*precio/100
#    print("el precio del " + producto + " es: $" + str(precioFinal))

#mostrarPrecioFinal("pantalon", 40 , 20)





#def calcularimc(peso, alturaM):
 #   imc = peso / (alturaM * alturaM)
  #  return imc

#def pedirDatos():
 #   peso = float(input('ingrese su peso'))
  #  altura = int(input('ingrese su altura'))
   # alturaM = altura/100
    #imc = calcularimc(peso, alturaM)

  #  if imc < 19:
    #    print ('esta muy flaco')

   # if imc > 19 and imc < 25:
     #   print (' esta saludable')

   # if imc >= 26 and imc < 30:
    #   print (' gordito como leito ')

   # if imc > 30:
    #    print ('obesidad')

#pedirDatos()


contador=0
while contador < 10:
    contador += 1
    if contador == 4:
        continue
    print('elvalor de contador es ' + str(contador))

