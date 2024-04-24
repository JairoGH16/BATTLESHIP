import logica.vidas as vidas
import var_imagenes as im
import turnos as tur

def damage(pos_x:int,pos_y:int,mar:list,num_mar:int):
    """si hay un barco en el botón que es atacado, daña su respectiva pieza y lo inmobiliza por completo

    Args:
        pos_x (int): posición x
        pos_y (int): posición y
        mar (list): mar
        num_mar (int): número del mar, para saber de qué jugador es
    """
    #Primero se revisa si no le pego a nada
    if mar[pos_y][pos_x]["pieza"]==".":
        print("no se ha golpeado nada")
        return
    
    #quitar avances a la pieza que se golpeó
    mar[pos_y][pos_x]["danado"]=True
    mar[pos_y][pos_x]["caminando"]=False

    #Si le pega a algún barco se quita el avance a las demás piezas del barco para que no se muevan más
    
    #barco pequeno no es necesario
    
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

    #barco pequeno
    if mar[pos_y][pos_x]["pieza"]=="A":
        if tur.nj == False:
            im.ptsj1+=1
        elif tur.nj == True:
            im.ptsj2+=1
        mar[pos_y][pos_x]["pieza"]="."
        vidas.quitar_vidas(num_mar,"barcos_pequenos")
        mar[pos_y][pos_x]["danado"]=False
        mar[pos_y][pos_x]["caminando"]=True

    #barco mediano
    #barco mediano desde parte 1
    if mar[pos_y][pos_x]["pieza"]=="B1":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            if mar[pos_y][pos_x]["danado"]==True and mar[pos_y][pos_x-1]["danado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y][pos_x-1]["pieza"]="."
                mar[pos_y][pos_x]["danado"]=False
                mar[pos_y][pos_x]["caminando"]=True
                mar[pos_y][pos_x-1]["danado"]=False
                mar[pos_y][pos_x-1]["caminando"]=True
                vidas.quitar_vidas(num_mar,"barcos_medianos")
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            if mar[pos_y+1][pos_x]["danado"]==True and mar[pos_y][pos_x]["danado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y+1][pos_x]["pieza"]="."
                mar[pos_y][pos_x]["danado"]=False
                mar[pos_y][pos_x]["caminando"]=True
                mar[pos_y+1][pos_x]["danado"]=False
                mar[pos_y+1][pos_x]["caminando"]=True
                vidas.quitar_vidas(num_mar,"barcos_medianos")
    #barco mediano desde parte 2
    if mar[pos_y][pos_x]["pieza"]=="B2":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            if mar[pos_y][pos_x]["danado"]==True and mar[pos_y][pos_x+1]["danado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y][pos_x+1]["pieza"]="."
                mar[pos_y][pos_x]["danado"]=False
                mar[pos_y][pos_x]["caminando"]=True
                mar[pos_y][pos_x+1]["danado"]=False
                mar[pos_y][pos_x+1]["caminando"]=True
                vidas.quitar_vidas(num_mar,"barcos_medianos")
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            if mar[pos_y-1][pos_x]["danado"]==True and mar[pos_y][pos_x]["danado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y-1][pos_x]["pieza"]="."
                mar[pos_y][pos_x]["danado"]=False
                mar[pos_y][pos_x]["caminando"]=True
                mar[pos_y-1][pos_x-1]["danado"]=False
                mar[pos_y-1][pos_x-1]["caminando"]=True
                vidas.quitar_vidas(num_mar,"barcos_medianos")

#barco grande
    #barco grande desde parte 1
    if mar[pos_y][pos_x]["pieza"]=="C1":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            if mar[pos_y][pos_x]["danado"]==True and mar[pos_y][pos_x-1]["danado"]==True and mar[pos_y][pos_x-2]["danado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y][pos_x-1]["pieza"]="."
                mar[pos_y][pos_x-2]["pieza"]="."
                mar[pos_y][pos_x]["danado"]=False
                mar[pos_y][pos_x]["caminando"]=True
                mar[pos_y][pos_x-1]["danado"]=False
                mar[pos_y][pos_x-1]["caminando"]=True
                mar[pos_y][pos_x-2]["danado"]=False
                mar[pos_y][pos_x-2]["caminando"]=True
                vidas.quitar_vidas(num_mar,"barcos_grandes")
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            if mar[pos_y][pos_x]["danado"]==True and mar[pos_y+1][pos_x]["danado"]==True and mar[pos_y+2][pos_x]["danado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y+1][pos_x]["pieza"]="."
                mar[pos_y+2][pos_x]["pieza"]="."
                mar[pos_y][pos_x]["danado"]=False
                mar[pos_y][pos_x]["caminando"]=True
                mar[pos_y+1][pos_x]["danado"]=False
                mar[pos_y+1][pos_x]["caminando"]=True
                mar[pos_y+2][pos_x]["danado"]=False
                mar[pos_y+2][pos_x]["caminando"]=True
                vidas.quitar_vidas(num_mar,"barcos_grandes")
    #barco grande desde parte 2
    if mar[pos_y][pos_x]["pieza"]=="C2":
        #si barco va para la izquierda o derecha
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            if mar[pos_y][pos_x]["danado"]==True and mar[pos_y][pos_x-1]["danado"]==True and mar[pos_y][pos_x+1]["danado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y][pos_x-1]["pieza"]="."
                mar[pos_y][pos_x+1]["pieza"]="."
                mar[pos_y][pos_x]["danado"]=False
                mar[pos_y][pos_x]["caminando"]=True
                mar[pos_y][pos_x-1]["danado"]=False
                mar[pos_y][pos_x-1]["caminando"]=True
                mar[pos_y][pos_x+1]["danado"]=False
                mar[pos_y][pos_x+1]["caminando"]=True
                vidas.quitar_vidas(num_mar,"barcos_grandes")
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            if mar[pos_y][pos_x]["danado"]==True and mar[pos_y-1][pos_x]["danado"]==True and mar[pos_y+1][pos_x]["danado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y-1][pos_x]["pieza"]="."
                mar[pos_y+1][pos_x]["pieza"]="."
                mar[pos_y][pos_x]["danado"]=False
                mar[pos_y][pos_x]["caminando"]=True
                mar[pos_y-1][pos_x]["danado"]=False
                mar[pos_y-1][pos_x]["caminando"]=True
                mar[pos_y+1][pos_x]["danado"]=False
                mar[pos_y+1][pos_x]["caminando"]=True
                vidas.quitar_vidas(num_mar,"barcos_grandes")
    #barco grande desde parte 3
    if mar[pos_y][pos_x]["pieza"]=="C3":
        #si barco va para la izquierda o abajo
        if mar[pos_y][pos_x]["direccion"]=="izquierda" or mar[pos_y][pos_x]["direccion"]=="derecha":
            if mar[pos_y][pos_x]["danado"]==True and mar[pos_y][pos_x+1]["danado"]==True and mar[pos_y][pos_x+2]["danado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y][pos_x+1]["pieza"]="."
                mar[pos_y][pos_x+2]["pieza"]="."
                mar[pos_y][pos_x]["danado"]=False
                mar[pos_y][pos_x]["caminando"]=True
                mar[pos_y][pos_x+1]["danado"]=False
                mar[pos_y][pos_x+1]["caminando"]=True
                mar[pos_y][pos_x+2]["danado"]=False
                mar[pos_y][pos_x+2]["caminando"]=True
                vidas.quitar_vidas(num_mar,"barcos_grandes")
        #si barco va para arriba o abajo
        if mar[pos_y][pos_x]["direccion"]=="arriba" or mar[pos_y][pos_x]["direccion"]=="abajo":
            if mar[pos_y][pos_x]["danado"]==True and mar[pos_y-1][pos_x]["danado"]==True and mar[pos_y-2][pos_x]["danado"]==True:
                mar[pos_y][pos_x]["pieza"]="."
                mar[pos_y-1][pos_x]["pieza"]="."
                mar[pos_y-2][pos_x]["pieza"]="."
                mar[pos_y][pos_x]["danado"]=False
                mar[pos_y][pos_x]["caminando"]=True
                mar[pos_y-1][pos_x]["danado"]=False
                mar[pos_y-1][pos_x]["caminando"]=True
                mar[pos_y-2][pos_x]["danado"]=False
                mar[pos_y-2][pos_x]["caminando"]=True
                vidas.quitar_vidas(num_mar,"barcos_grandes")
    
"""
piezas
pieza A: barco pequeno
pieza B1: parte 1 de barco mediano
pieza B2: parte 2 de barco mediano
pieza C1: parte 1 de barco grande
pieza C2: parte media de barco grande
pieza C3: parte 3 de barco grande
pieza X: pieza rota
"""