def extremos(x,y):
    y.append(x[0])
    y.append(x[len(x)-1])

a = [5, 10, 15, 20, 25, 33, 23, 120]

b=[]

extremos(a,b)
print(b)