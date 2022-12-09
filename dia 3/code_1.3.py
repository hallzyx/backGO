notas=[10,20,16,8,6,1]


for nota in notas:
    print(nota)


print("----------")

print(notas[0:3])  

print("----------")

for indice in range(3):
    print(notas[indice])



series=[]
def new_series(nombre, tipo, genero ):
    series.append({
            'Nombre':nombre,
            'Tipo': tipo,
            'Genero': genero,
        })

new_series("PLAYER","manhwa","shonen")
print(series)


nom=[]
nom.append("numeroxd")
print(nom)
nom.append({"numero":1})
print(nom)
