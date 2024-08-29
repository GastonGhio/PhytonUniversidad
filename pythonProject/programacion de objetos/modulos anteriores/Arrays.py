# son variables que pueden guardar datos o caracteristicas asociadas al objeto creado


#generar una especie de diccionario

numeros = {
     "0": "cero",
     "1": "uno",
     "2": "dos",
     "3": "tres",
     "4": "cuatro",
     "5": "cinco",
     "6": "seis",
     "7": "siete",
     "8": "ocho",
     "9": "nueve"
}

texto = input('ingrese su numero')

textoFinal = ''

#RECORRER UN ARREGLO ES CON FOR XX IN XXX
for letra in texto:
    textoFinal += numeros[letra] + ' '

print(textoFinal)
