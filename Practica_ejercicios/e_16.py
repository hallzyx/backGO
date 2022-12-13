##Generador de contraseñas
import random

dif=input("¿Desea una contraseña debil o fuerte?=> ").lower()

debil=["casa", "perro", "carro", "mosquito", "basura", "padres", "dinero", "ex"]

contra=[]

if(dif=="debil"):
    ran1=random.randint(0,len(debil)-1)
    ran2=random.randint(0,len(debil)-1)
    print(ran1)
    print(ran2)

    print("Tu contrasenia es : {} {}".format(debil[ran1],debil[ran2]))
if(dif=="fuerte"):
    n_caract=random.randint(8,12)
    i=0
    while i<n_caract:
        caract=chr(random.randint(33,126))
        contra.append(caract)
        i+=1 
    print("Tu contraseña es: {}".format("".join(contra)))
    
else:
   print("Has escrito una opcion desconocida, intente de nuevo.")
