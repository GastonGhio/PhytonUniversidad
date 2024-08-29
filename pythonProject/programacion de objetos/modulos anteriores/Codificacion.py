
#GENERA UN ARCHIVO Y PONE LO ESCRITO AHI
#archivo = open('texto.txt', 'a')
#archivo.write('es una prueba')
#archivo.close()

#PERMITE ACCEDER AL ARCHIVO GUARDADO
#archivo = open('texto.txt', 'r')
#print(archivo.read())

#VAMOS A GENERAR UN FUNCION PARA ENCRIPTAR Y DESENCRIPTAR UN TEXTO


def encriptar(texto):
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textoFinal += chr(ascii)
    print('el texto a sido encriptado correctamente en ' + textoFinal)
    return textoFinal

def desencriptar(texto):
    textoFinal = ''
    contador = 0
    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        textoFinal += chr(ascii)
    print('texto desencriptado correctamente en ' + textoFinal )
    return textoFinal


def encriptarDoc(rutaArchivo):
        archivo = open(rutaArchivo, 'r')
        texto = archivo.read()
        archivo.close()
        textoEncriptado = encriptar(texto)

        archivo = open(rutaArchivo, 'w')
        archivo.write(textoEncriptado)
        archivo.close()


def desencriptarDoc(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()

#encriptarDoc()

#desencriptarDoc()

respuestaEoD = input('precione E para encriptar o D para desencriptar')

rutaArchivo = input('ingrese ruta del archivo')

#ACA CREAMOS UN CONDICIONAL CON IF , ELIF Y ELSE, PARA QUE SE ENCIPTE O NO EL TEXTO

if respuestaEoD == 'e':
    encriptarDoc(rutaArchivo)
elif respuestaEoD == 'd':
    desencriptarDoc(rutaArchivo)
else:
    input('no se logro la encriptacion')

# UTILIZACION DE ORD Y CHR

