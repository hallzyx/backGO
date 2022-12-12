import random

n=random.randint(1,9)
controlador=0

while True:
    print("El numero secreto es: {}".format(n))
    user=int(input("Adivine el numero: "))

    if(n==user):
        print("¡Has adivinado el numero!")
        controlador+=1
        break
    elif(n>user):
        print("El numero que elegiste es menor al numero secreto")
        controlador+=1
    elif(n<user):
        print("El numero que has elegido es mayor al numero secreto")
        controlador+=1

print("Total de intentos : {}".format(controlador))