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


#calcular el factorial de cualquier numero [n!]



def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
    

num=factorial(3)
print(num) 
n1=2
n2=4
nombre="Brayan"

def saludar(n1,n2):
    n1+=1
    rpta= n2+n1
    print(rpta)
saludar(n1,n2)

print(n1)


class manga:

    def __init__(self,nombre,genero,_capitulos,tipo):
        self.nombre=nombre
        self.genero=genero
        self.capitulos=_capitulos
        self.tipo=tipo

    def saludar(self):
        print("Holap")

    def getCapitulos(self):
        return self.capitulos


serie1=manga("Player","Shounen",0.0099999999,"Manhwa")
serie2=manga("Mercenario","Shounen",114,"Manhwa")

print("{:.2f}".format(serie1.capitulos))





