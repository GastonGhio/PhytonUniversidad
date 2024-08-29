def encriptar(mensaje):
    mensaje_encriptado = ""
    for char in mensaje:
        if char.isalpha():
            if char.isupper():
                mensaje_encriptado += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            else:
                mensaje_encriptado += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:
            mensaje_encriptado += char
    return mensaje_encriptado

def desencriptar(mensaje_encriptado):
    mensaje_desencriptado = ""
    for char in mensaje_encriptado:
        if char.isalpha():
            if char.isupper():
                mensaje_desencriptado += chr((ord(char) - ord('A') - 1) % 26 + ord('A'))
            else:
                mensaje_desencriptado += chr((ord(char) - ord('a') - 1) % 26 + ord('a'))
        else:
            mensaje_desencriptado += char
    return mensaje_desencriptado


mensaje_original = "una IA q pueda buscar gente por una foto, a taves de perfiles de facebook o intagram, tiktok."


mensaje_encriptado = encriptar(mensaje_original)
print("Mensaje encriptado:", mensaje_encriptado)


mensaje_desencriptado = desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)