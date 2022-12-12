def felicitaciones(x,m):
    if x==m:
        print("Felicitaciones al jugador 1, es el ganador.")
    else:
        print("Felicitaciones al jugador 2, es el ganador.")
    
controlador=0

while controlador!=1:
    while True:
        j_1=input("Elija jugador 1: ").lower()
        if(j_1=="piedra" or j_1=="tijera" or j_1=="papel"):
            break

    while True:           
        j_2=input("Elija jugador 2: ").lower()    
        if(j_2=="piedra" or j_2=="tijera" or j_2=="papel"):
            break
        
        

    mov=["piedra", "papel", "tijera"]



    for n in mov:
        if n==j_1:
            for m in mov:
                if m==j_2:
                    if(n==m):
                        print("Ambos jugadores an sacado lo mismo.")
                    
                    else:
                        if n=="piedra" and m=="papel" or m=="piedra" and n=="papel":
                            print("Papel gana a piedra")
                            felicitaciones(n,"papel")
                            controlador=1
                            break

                        elif n=="piedra" and m=="tijera" or m=="piedra" and n=="tijera":
                            print("Piedra gana a tijera")
                            felicitaciones(n,"piedra")
                            controlador=1
                            break

                        elif n=="papel" and m=="tijera" or m=="papel" and n=="tijera":
                            print("Tijera gana a papel")
                            felicitaciones(n,"tijera")
                            controlador=1
                            break

    



