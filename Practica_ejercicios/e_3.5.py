a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_1=[]
for num in a:
    if num < 5:
        a_1.append(num)
        print(num)

print(a_1)

n=int(input("Digite el numero techo de la lista: "))
for num in a:
    if num < n:
        print(num)