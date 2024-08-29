"""print("hola")


print(type(9))
print(type(1.2))
print(type(True))

"""

my_other_set = {"cintia", "natala", 35 }
list = [1, 2, 3, "morena"]

print (type(my_other_set))
print (type(list))
print(list)

#TEST DE EXISTENCIA EN LISTA  - in -

print("morena" in list)
print(35 in my_other_set)
print("intia" in my_other_set)
my_new = {"rojas" , "roro"}

my_new = my_other_set.union(my_new)
print(my_other_set)
print(my_new)

diccionario =  dict()
print(type(diccionario))

diccionario = {"nombre" : "perro",
               "raza":  "boxer",
               "edad" : 3}

otro_dic = {"lenguajes": {"phyton", "javascript" }}


new_dict = dict.fromkeys(diccionario)
print(new_dict)