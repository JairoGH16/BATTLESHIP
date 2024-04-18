def damage(pos_x:int,pos_y:int):
    #Primero se revisa si no le pego a nada
    if mar[pos_y][pos_x]["pieza"]==".":
        print("no se ha golpeado nada")
        return
    #Si le pega a algún barco se quita la dirección a las demás piezas del barco para que no se muevan más
    
    #barco pequeño no es necesario
    
    #barco mediano
    #barco mediano desde parte 1
    if mar[pos_y][pos_x]["pieza"]=="B1":
        #si barco va para la izquierda
        if mar[pos_y][pos_x]["direccion"]=="izquierda":
            mar[pos_y][pos_x+1]["direccion"]="N"
        #si barco va para la derecha
        if mar[pos_y][pos_x]["direccion"]=="derecha":
            mar[pos_y][pos_x-1]["direccion"]="N"
        #si barco va para arriba
        if mar[pos_y][pos_x]["direccion"]=="arriba":
            mar[pos_y+1][pos_x]["direccion"]="N"
        #si barco va para abajo
        if mar[pos_y][pos_x]["direccion"]=="abajo":
            mar[pos_y-1][pos_x]["direccion"]="N"
    #barco mediano desde parte 2
    if mar[pos_y][pos_x]["pieza"]=="B2":
        #si barco va para la izquierda
        if mar[pos_y][pos_x]["direccion"]=="izquierda":
            mar[pos_y][pos_x-1]["direccion"]="N"
        #si barco va para la derecha
        if mar[pos_y][pos_x]["direccion"]=="derecha":
            mar[pos_y][pos_x+1]["direccion"]="N"
        #si barco va para arriba
        if mar[pos_y][pos_x]["direccion"]=="arriba":
            mar[pos_y-1][pos_x]["direccion"]="N"
        #si barco va para abajo
        if mar[pos_y][pos_x]["direccion"]=="abajo":
             mar[pos_y+1][pos_x]["direccion"]="N"
    
    #barco grande
    #barco grande desde parte 1
    if mar[pos_y][pos_x]["pieza"]=="C1":
        #si barco va para la izquierda
        if mar[pos_y][pos_x]["direccion"]=="izquierda":
            mar[pos_y][pos_x+1]["direccion"]="N"
            mar[pos_y][pos_x+2]["direccion"]="N"
        #si barco va para la derecha
        if mar[pos_y][pos_x]["direccion"]=="derecha":
            mar[pos_y][pos_x-1]["direccion"]="N"
            mar[pos_y][pos_x-2]["direccion"]="N"
        #si barco va para arriba
        if mar[pos_y][pos_x]["direccion"]=="arriba":
            mar[pos_y+1][pos_x]["direccion"]="N"
            mar[pos_y+2][pos_x]["direccion"]="N"
        #si barco va para abajo
        if mar[pos_y][pos_x]["direccion"]=="abajo":
            mar[pos_y-1][pos_x]["direccion"]="N"
            mar[pos_y-2][pos_x]["direccion"]="N"
    #barco grande desde parte 2
    if mar[pos_y][pos_x]["pieza"]=="C2":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            mar[pos_y][pos_x-1]["direccion"]="N"
            mar[pos_y][pos_x+1]["direccion"]="N"
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            mar[pos_y-1][pos_x]["direccion"]="N"
            mar[pos_y+1][pos_x]["direccion"]="N"
    #barco grande desde parte 3
    if mar[pos_y][pos_x]["pieza"]=="C3":
        #si barco va para la izquierda
        if mar[pos_y][pos_x]["direccion"]=="izquierda":
            mar[pos_y][pos_x-1]["direccion"]="N"
            mar[pos_y][pos_x-2]["direccion"]="N"
        #si barco va para la derecha
        if mar[pos_y][pos_x]["direccion"]=="derecha":
            mar[pos_y][pos_x+1]["direccion"]="N"
            mar[pos_y][pos_x+2]["direccion"]="N"
        #si barco va para arriba
        if mar[pos_y][pos_x]["direccion"]=="arriba":
            mar[pos_y-1][pos_x]["direccion"]="N"
            mar[pos_y-2][pos_x]["direccion"]="N"
        #si barco va para abajo
        if mar[pos_y][pos_x]["direccion"]=="abajo":
            mar[pos_y+1][pos_x]["direccion"]="N"
            mar[pos_y+2][pos_x]["direccion"]="N"

    #quitar dirección a la pieza que se golpeó y marcarla con X
    mar[pos_y][pos_x]["pieza"]="X"
    mar[pos_y][pos_x]["direccion"]="N"
    
"""
piezas
pieza A: barco pequeño
pieza B1: parte 1 de barco mediano
pieza B2: parte 2 de barco mediano
pieza C1: parte 1 de barco grande
pieza C2: parte media de barco grande
pieza C3: parte 3 de barco grande
pieza X: pieza rota
"""