nombre=input("Introdusca su nombre: ")
edad=int(input("Introdusca su edad: "))
anio=int(input("Cual es el año actual: "))
dif=100-edad

anio_2=anio+dif

print("El usuario {} cumplirá 100 años en {} años, es decir en el año {}".format(nombre,dif,anio_2))

