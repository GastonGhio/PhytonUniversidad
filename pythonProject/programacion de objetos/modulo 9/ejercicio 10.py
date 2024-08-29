def primo(num):
    divisores =0
    for i in range(1,num):
        if num % i==0:
            divisores = divisores+1 # este es el valor q toma divs al retorse ya q esta llamndo a la funcion
    return divisores

vec = []
cont =0
num = 1

while cont<15:
    divs=primo(num)
    if (divs==0 or divs==1) and num != 1:
        vec.append(num)
        cont =cont +1
    num =num+1

print(vec)