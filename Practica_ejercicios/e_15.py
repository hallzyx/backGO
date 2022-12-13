frase=input("Escriba la oracion deseada: ")
vec=frase.split()
vec2=[]
print(vec)
i=1
for palabra in vec:
    vec2.append(vec[len(vec)-i])
    i+=1

print(vec2)