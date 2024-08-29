A = [2,3,5,6]
i = 2

def generar(a):
    cont = 0
    for i in range (0, 8):
        num = int(input("ingrese numero"))
        if num %2 ==0 and cont < 6:
            a.append(num)
            cont = cont + 1





#generar(A)

print(i,A[i])