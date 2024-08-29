#EJERCICIO 3 MODULO 6
"""
cat1=45
cat2=50
cat3=55
cat4=60
totalSalary = 0
c1= 0
c2=0
c3=0
c4=0


employer= int(input("uingrese cantidad de empleados"))

for i in range (employer):

    catEmployer= int(input("ingrese categoriA DE 1 A 4"))
    hourJob= int(input("ingrese horas ttrabajadas mensuales"))
    if catEmployer == 1:
        salaryBruto = cat1 * hourJob
        salaryNet = salaryBruto - (salaryBruto * 0.17)
        c1= c1 +1

    if catEmployer == 2:
        salaryBruto = cat2 * hourJob
        salaryNet = salaryBruto - (salaryBruto * 0.17)
        c2 = c2 + 1

    if catEmployer == 3:
        salaryBruto = cat3 * hourJob
        salaryNet = salaryBruto - (salaryBruto * 0.17)
        c3 = c3 + 1

    if catEmployer == 4:
        salaryBruto = cat4 * hourJob
        salaryNet = salaryBruto - (salaryBruto * 0.17)
        c4 = c4 + 1

    totalSalary = totalSalary + salaryBruto
    print("el empleado ", i+1 , " su salario bruto es ", salaryBruto, " y el salario neto ", salaryNet)

print("la cantidad de empleados de cat 1 cat 2 cat 3 y cat 4 es ", c1, " ", c2, " ", c3,"",c4)
print("la cantidad de sueldos pagados en usd", totalSalary)
"""

#  A