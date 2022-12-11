n=int(input("Dijite el numero que quiere dividir: "))
div=int(input("Digite el numero que quiere verificar que sea multiplo: "))

if n%div==0:
    print("El numero {} si es multiplo de {}".format(n,div))
else:
    print("El numero {} NO es multiplo de {}". format(n,div))
