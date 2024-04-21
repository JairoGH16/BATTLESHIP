def imprimir_mar(mar):
    """imprimir_mar imprime la matriz correspondiente al mar para hacer pruebas en la terminal.
    """
    for fila in mar:
        for columna in fila:
            print(columna["pieza"],"",sep="\t",end="")
        print("")
    print("")

def mover_izquierda(columna:dict,pos_x:int,pos_y:int,mar):
    """mover_izquierda mueve las piezas hacia la izquierda, un paso para todos los barcos, a excepción de los destructores que se mueven
    dos pasos en caso de ser posible.

    Args:
        columna (dict): la pieza que se va a mover.
        pos_x (int): posición x de la pieza.
        pos_y (int): posición y de la pieza.
    """
    if pos_x>0 and mar[pos_y][pos_x-1]["pieza"]==".":
        if mar[pos_y][pos_x]["pieza"]=="A" and pos_x>1 and mar[pos_y][pos_x-2]["pieza"]==".":
            mar[pos_y][pos_x-2]["pieza"]=columna["pieza"]
            mar[pos_y][pos_x-2]["direccion"]=columna["direccion"]
        else:
            mar[pos_y][pos_x-1]["pieza"]=columna["pieza"]
            mar[pos_y][pos_x-1]["direccion"]=columna["direccion"]
        mar[pos_y][pos_x]["pieza"]="."
        mar[pos_y][pos_x]["direccion"]=""
    else:
        columna["direccion"]="derecha"

def mover_arriba(columna:dict,pos_x:int,pos_y:int,mar):
    """mover_arriba mueve las piezas hacia arriba, un paso para todos los barcos, a excepción de los destructores que se mueven
    dos pasos en caso de ser posible.

    Args:
        columna (dict): la pieza que se va a mover.
        pos_x (int): posición x de la pieza.
        pos_y (int): posición y de la pieza.
    """
    if pos_y>0 and mar[pos_y-1][pos_x]["pieza"]==".":
        if mar[pos_y][pos_x]["pieza"]=="A" and pos_y>1 and mar[pos_y-2][pos_x]["pieza"]==".":
                mar[pos_y-2][pos_x]["pieza"]=columna["pieza"]
                mar[pos_y-2][pos_x]["direccion"]=columna["direccion"]
        else:
            mar[pos_y-1][pos_x]["pieza"]=columna["pieza"]
            mar[pos_y-1][pos_x]["direccion"]=columna["direccion"]
        mar[pos_y][pos_x]["pieza"]="."
        mar[pos_y][pos_x]["direccion"]=""
    else:
        columna["direccion"]="abajo"

def mover_abajo(columna:dict,pos_x:int,pos_y:int,mar):
    """mover_abajo mueve las piezas hacia abajo, un paso para todos los barcos, a excepción de los destructores que se mueven
    dos pasos en caso de ser posible.

    Args:
        columna (dict): la pieza que se va a mover.
        pos_x (int): posición x de la pieza.
        pos_y (int): posición y de la pieza.
    """
    if pos_y<len(mar)-1 and mar[pos_y+1][pos_x]["pieza"]==".":
            if mar[pos_y][pos_x]["pieza"]=="A" and pos_y<len(mar)-2 and mar[pos_y+2][pos_x]["pieza"]==".":
                mar[pos_y+2][pos_x]["pieza"]=columna["pieza"]
                mar[pos_y+2][pos_x]["direccion"]=columna["direccion"]
            else:
                mar[pos_y+1][pos_x]["pieza"]=columna["pieza"]
                mar[pos_y+1][pos_x]["direccion"]=columna["direccion"]
            mar[pos_y][pos_x]["pieza"]="."
            mar[pos_y][pos_x]["direccion"]=""
    else:
        columna["direccion"]="arriba"

def mover_derecha(columna:dict,pos_x:int,pos_y:int,mar):
    """mover_derecha mueve las piezas hacia la derecha, un paso para todos los barcos, a excepción de los destructores que se mueven
    dos pasos en caso de ser posible.

    Args:
        columna (dict): la pieza que se va a mover.
        pos_x (int): posición x de la pieza.
        pos_y (int): posición y de la pieza.
    """
    if pos_x<len(mar[0])-1 and mar[pos_y][pos_x+1]["pieza"]==".":
        if mar[pos_y][pos_x]["pieza"]=="A" and pos_x<len(mar[0])-2 and mar[pos_y][pos_x+2]["pieza"]==".":
            mar[pos_y][pos_x+2]["pieza"]=columna["pieza"]
            mar[pos_y][pos_x+2]["direccion"]=columna["direccion"]
        else:
            mar[pos_y][pos_x+1]["pieza"]=columna["pieza"]
            mar[pos_y][pos_x+1]["direccion"]=columna["direccion"]
        mar[pos_y][pos_x]["pieza"]="."
        mar[pos_y][pos_x]["direccion"]=""
    else:
        columna["direccion"]="izquierda"

def mover_barcos(mar):
    #hacia arriba e izquierda
    pos_y=0
    for fila in mar:
        pos_x=0
        for columna in fila:
            if columna["direccion"]=="arriba" and columna["caminando"]==True:
                    mover_arriba(columna,pos_x,pos_y,mar)
            if columna["direccion"]=="izquierda" and columna["caminando"]==True:
                mover_izquierda(columna,pos_x,pos_y,mar)
            pos_x+=1
        pos_y+=1
    #hacia abajo y derecha
    pos_y=len(mar)-1
    for fila in mar[::-1]:
        pos_x=len(mar[0])-1
        for columna in fila[::-1]:
            if columna["direccion"]=="abajo" and columna["caminando"]==True:
                mover_abajo(columna,pos_x,pos_y,mar)
            if columna["direccion"]=="derecha" and columna["caminando"]==True:
                mover_derecha(columna,pos_x,pos_y,mar)
            pos_x-=1
        pos_y-=1
