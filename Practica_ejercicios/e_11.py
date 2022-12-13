n=int(input("Ingrese el numero: "))
i=1

token=0
while i<=n:


    if n%i==0:
        token=token+1
        
    i+=1


if token==2:
    print("El numero {} SI es primo".format(n))
else:
    print("El numero {} NO es primo".format(n))

