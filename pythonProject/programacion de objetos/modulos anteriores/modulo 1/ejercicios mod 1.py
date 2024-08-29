#num = int(input("ingrese numero de 3 cifras"))

#primero = num//10

#print(primero%10)


#EJERCICIO 2

#pais = input("ingrese pais")
#apital = input("ingrese capital de dicho pais")

#print(capital + " es capital de " + pais)

#EJERCICIO 3

#precioheladera = float(input("ingrese precio de modelo de heladera: "))

#descuento = precioheladera - precioheladera*10/100

#print("aplicando el 10% su precio final es de " + str(descuento))

#EJERCICIO 6

#x = float(input("Ingrese un número decimal: "))

#x1 = round(x, 2)
#x2 = round(x, 3)

# Usar cadenas de formato f para mostrar números con ceros adicionales si es necesario
#print(f"Número con 2 decimales: {x1:.2f}")
#print(f"Número con 3 decimales: {x2:.3f}")

#EJERCICIO 7

#distancia = float(input("ingrese distancia en millas"))

#km = distancia * 1.60935

#plgada = distancia * 2.534

#print("en kilometrs ", km, "km en pulgadas ", plgada," pulgadas")

#EJERCICIOS 8

# Ingresar numeros enteros positivos hasta que ingrese un -1
# calcular y mostrar el promedio al finalizar


# Ingresar numeros enteros positivos hasta que ingrese un -1
# sumarlos y mostrar el total al finalizar

sumador = 0
contador = 0
a = int(input("Ingrese un numero: "))

while a != -1: # MIENTRAS sea DISTINTO, si es igual no entra
    if a > 0:
        sumador += a
        contador += 1
    a = int(input("Ingrese otro numero: "))

if contador > 0: # para evitar error de div x 0
    promedio = sumador / contador
    print("El promedio es:", promedio)
else:
    print("No hay valores para calcular")


