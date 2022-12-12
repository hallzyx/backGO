


def redondeo(n):

    if n%2!=0:
        n=int(n/2+0.5)
    else:
        n=int(n/2)
    return n




palin=input("Introdusca la palabra: ")
token=redondeo(len(palin))
cont=0
i=0

while i<token:
    if palin[i]==palin[len(palin)-(i+1)]:
            cont+=1
    
    i+=1

# print(token)
# print(cont)
if(cont==token):
    print("Esta palabra es palindroma.")
else:
    print("Esta palabra NO es palindroma.")