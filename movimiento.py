#Este código corresponde a una versión inicial de prueba y requiere de modificaciones importantes
import time

mar=[["." for y in range(5)]for x in range(5)]

def imprimir_mar():
    """imprimir_mar imprime la matriz correspondiente al mar para hacer pruebas en la terminal.
    """
    for fila in mar:
        for columna in fila:
            print(columna,"",sep="\t",end="")
        print("")
    print("")
    
imprimir_mar()
time.sleep(2)

barco1={
    "pos_y":0,
    "pos_x":0,
    "direccion":"derecha",
    "apariencia":"D"
}
    
barco2={
    "pos_y":2,
    "pos_x":3,
    "direccion":"arriba",
    "apariencia":"A"
}

barco3={
    "pos_y":4,
    "pos_x":4,
    "direccion":"izquierda",
    "apariencia":"I"
}

barco4={
    "pos_y":2,
    "pos_x":1,
    "direccion":"abajo",
    "apariencia":"E"
}
    
def mover(barco):
    """mover mueve un barco una casilla según la dirección en la que esté, o en caso de chocar con pared o con otro barco hace que cambie
    hacia la dirección opuesta.

    Args:
        barco (_dict_): corresponde al barco que se va a mover
    """
    if barco["direccion"]=="abajo":
        if barco["pos_y"]<len(mar)-1 and mar[barco["pos_y"]+1][barco["pos_x"]]==".":
            mar[barco["pos_y"]][barco["pos_x"]]="."
            barco["pos_y"] += 1
            mar[barco["pos_y"]][barco["pos_x"]]=barco["apariencia"]
        else:
            barco["direccion"]="arriba"
            return
    if barco["direccion"]=="arriba":
        if barco["pos_y"]>0 and mar[barco["pos_y"]-1][barco["pos_x"]]==".":
            mar[barco["pos_y"]][barco["pos_x"]]="."
            barco["pos_y"] -= 1
            mar[barco["pos_y"]][barco["pos_x"]]=barco["apariencia"]
        else:
            barco["direccion"]="abajo"
            return
    if barco["direccion"]=="derecha":
        if barco["pos_x"]<len(mar[0])-1 and mar[barco["pos_y"]][barco["pos_x"]+1]==".":
            mar[barco["pos_y"]][barco["pos_x"]]="."
            barco["pos_x"] += 1
            mar[barco["pos_y"]][barco["pos_x"]]=barco["apariencia"]
        else:
            barco["direccion"]="izquierda"
            return
    if barco["direccion"]=="izquierda":
        if barco["pos_x"]>0 and mar[barco["pos_y"]][barco["pos_x"]-1]==".":
            mar[barco["pos_y"]][barco["pos_x"]]="."
            barco["pos_x"] -= 1
            mar[barco["pos_y"]][barco["pos_x"]]=barco["apariencia"]
        else:
            barco["direccion"]="derecha"

while True:
    mover(barco1)
    mover(barco2)
    mover(barco3)
    mover(barco4)
    imprimir_mar()
    time.sleep(2)