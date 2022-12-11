
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 40,85, 85,90,91,90,87,87,87,87,87,87]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,40,85,87,87,87,87,87,87,93,94,96,4,6,6,322,45,43]
c=[]
#Primera manera
d=list(set(a).intersection(set(b)))

e=[]

i=0
#Segunda manera 
while True:
    if(i==len(a)):
        break
    
    for num in b:
        if(num==a[i]):
            c.append(num)
            break
    i+=1

i=0
print(c)
while i<20:
    
    token=0
    if(i==len(c)):
        break
    for num in c:
        
        if(c[i]==num):
            
            token=token+1
            
            
        if token==2:
            c[i]=0
            break
    i+=1     
print(c)

i=0
while i<len(c):
     
    for num in c:
        if num==0:
            c.remove(0)
            

    i+=1
#Tercera manera
for num in a:
    if num in b and num not in e:
        e.append(num)



print(c)

print(d)

print(e)


