import logica.vidas as vidas

def damage(pos_x:int,pos_y:int,mar:list,num_mar:int):
    #Primero se revisa si no le pego a nada
    if mar[pos_y][pos_x]["pieza"]==".":
        print("no se ha golpeado nada")
        return
    
    #quitar avances a la pieza que se golpeó
    mar[pos_y][pos_x]["dañado"]=True
    mar[pos_y][pos_x]["caminando"]=False

    #Si le pega a algún barco se quita el avance a las demás piezas del barco para que no se muevan más
    
    #barco pequeño no es necesario
    
    #barco mediano
    #barco mediano desde parte 1
    if mar[pos_y][pos_x]["pieza"]=="B1":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            mar[pos_y][pos_x-1]["caminando"]=False
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            mar[pos_y+1][pos_x]["caminando"]=False
    #barco mediano desde parte 2
    if mar[pos_y][pos_x]["pieza"]=="B2":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            mar[pos_y][pos_x+1]["caminando"]=False
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            mar[pos_y-1][pos_x]["caminando"]=False
    
    #barco grande
    #barco grande desde parte 1
    if mar[pos_y][pos_x]["pieza"]=="C1":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            mar[pos_y][pos_x-1]["caminando"]=False
            mar[pos_y][pos_x-2]["caminando"]=False
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            mar[pos_y+1][pos_x]["caminando"]=False
            mar[pos_y+2][pos_x]["caminando"]=False
    #barco grande desde parte 2
    if mar[pos_y][pos_x]["pieza"]=="C2":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            mar[pos_y][pos_x-1]["caminando"]=False
            mar[pos_y][pos_x+1]["caminando"]=False
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            mar[pos_y-1][pos_x]["caminando"]=False
            mar[pos_y+1][pos_x]["caminando"]=False
    #barco grande desde parte 3
    if mar[pos_y][pos_x]["pieza"]=="C3":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            mar[pos_y][pos_x+1]["caminando"]=False
            mar[pos_y][pos_x+2]["caminando"]=False
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            mar[pos_y-1][pos_x]["caminando"]=False
            mar[pos_y-2][pos_x]["caminando"]=False

    #si todas las piezas de un barco están dañadas, se desaparece

    #barco pequeño
    if mar[pos_y][pos_x]["pieza"]=="A":
        mar[pos_y][pos_x]["pieza"]="."
        vidas.quitar_vidas(num_mar,"barcos_pequeños")

    #barco mediano
    #barco mediano desde parte 1
    if mar[pos_y][pos_x]["pieza"]=="B1":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            if mar[pos_y][pos_x]["dañado"]==True and mar[pos_y][pos_x-1]["dañado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y][pos_x-1]["pieza"]="."
                vidas.quitar_vidas(num_mar,"barcos_medianos")
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            if mar[pos_y+1][pos_x]["dañado"]==True and mar[pos_y][pos_x]["dañado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y+1][pos_x]["pieza"]="."
                vidas.quitar_vidas(num_mar,"barcos_medianos")
    #barco mediano desde parte 2
    if mar[pos_y][pos_x]["pieza"]=="B2":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            if mar[pos_y][pos_x]["dañado"]==True and mar[pos_y][pos_x+1]["dañado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y][pos_x+1]["pieza"]="."
                vidas.quitar_vidas(num_mar,"barcos_medianos")
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            if mar[pos_y-1][pos_x]["dañado"]==True and mar[pos_y][pos_x]["dañado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y-1][pos_x]["pieza"]="."
                vidas.quitar_vidas(num_mar,"barcos_medianos")

#barco grande
    #barco grande desde parte 1
    if mar[pos_y][pos_x]["pieza"]=="C1":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            if mar[pos_y][pos_x]["dañado"]==True and mar[pos_y][pos_x-1]["dañado"]==True and mar[pos_y][pos_x-2]["dañado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y][pos_x-1]["pieza"]="."
                mar[pos_y][pos_x-2]["pieza"]="."
                vidas.quitar_vidas(num_mar,"barcos_grandes")
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            if mar[pos_y][pos_x]["dañado"]==True and mar[pos_y+1][pos_x]["dañado"]==True and mar[pos_y+2][pos_x]["dañado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y+1][pos_x]["pieza"]="."
                mar[pos_y+2][pos_x]["pieza"]="."
                vidas.quitar_vidas(num_mar,"barcos_grandes")
    #barco grande desde parte 2
    if mar[pos_y][pos_x]["pieza"]=="C2":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            if mar[pos_y][pos_x]["dañado"]==True and mar[pos_y][pos_x-1]["dañado"]==True and mar[pos_y][pos_x+1]["dañado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y][pos_x-1]["pieza"]="."
                mar[pos_y][pos_x+1]["pieza"]="."
                vidas.quitar_vidas(num_mar,"barcos_grandes")
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            if mar[pos_y][pos_x]["dañado"]==True and mar[pos_y-1][pos_x]["dañado"]==True and mar[pos_y+1][pos_x]["dañado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y-1][pos_x]["pieza"]="."
                mar[pos_y+1][pos_x]["pieza"]="."
                vidas.quitar_vidas(num_mar,"barcos_grandes")
    #barco grande desde parte 3
    if mar[pos_y][pos_x]["pieza"]=="C3":
        #si barco va para la izquierda o abajo
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            if mar[pos_y][pos_x]["dañado"]==True and mar[pos_y][pos_x+1]["dañado"]==True and mar[pos_y][pos_x+2]["dañado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y][pos_x+1]["pieza"]="."
                mar[pos_y][pos_x+2]["pieza"]="."
                vidas.quitar_vidas(num_mar,"barcos_grandes")
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            if mar[pos_y][pos_x]["dañado"]==True and mar[pos_y-1][pos_x]["dañado"]==True and mar[pos_y-2][pos_x]["dañado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y-1][pos_x]["pieza"]="."
                mar[pos_y-2][pos_x]["pieza"]="."
                vidas.quitar_vidas(num_mar,"barcos_grandes")
    
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