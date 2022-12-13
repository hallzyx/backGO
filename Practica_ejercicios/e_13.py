val=int(input("Cuantas numeros de fibonachi desea generar: "))

i=1

while i<=val:
    if(i==1 or i==2):
        n_1=1
        n_2=1
        print("1 ")
    if(i>2):
        temp=n_1+n_2
        print("{} ".format(temp))
        n_1=n_2
        n_2=temp
        

    i+=1