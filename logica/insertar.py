import logica.movimiento as mov
import turnos as tur
import rotar_imagenes as rot
import var_imagenes as im

def insertar_piezas(pieza:str,direccion:str,pos_x:int,pos_y:int,mar):
    """insertar es una función que permite insertar una pieza de un barco en las matrices donde funciona la lógica del movimiento.

    Args:
        pieza (str): corresponde a la parte del barco, trasera, media o delantera, si es un destructor (barco de una sola pieza) entonces se representa
        con una A.
        direccion (str): dirección que tiene el barco (derecha, izquierda, arriba o abajo).
        pos_x (int): posición x de la pieza.
        pos_y (int): posición y de la pieza.
    """
    if mar[pos_y][pos_x]["pieza"]==".":
        mar[pos_y][pos_x]["pieza"]=pieza
        mar[pos_y][pos_x]["direccion"]=direccion

def insertar_barcos(posx:int, posy:int,config:int,columns:int,rows:int,matriz_visual:list,mar:int,mar1:list,mar2:list):
    """insertar_barcos es una función que permite insertar los barcos, insertando cada una de sus piezas por separado.

    Args:
        posx (int): posición x
        posy (int): posición y
        config (int): configuración
        columns (int): columnas_
        rows (int): filas_
        matriz_visual (list): matriz de interfaz
        mar (int): número de mar
        mar1 (list): mar de jugador 1
        mar2 (list): mar de jugador 2
    """
    global verif

    #Jugador 1
    if tur.nj == False and tur.fase_barcos_1 == True:
        if mar==2:
            return
        verif = 1
        if config == 1:
                var = 0
                for x in im.imagenes1_1:
                    var+=1
                if var < 6:
                    if ((posy, posx)) not in im.verif_pos_1 and im.barcos1_1 < 6:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen(verif, im.angulo_rotacion, im.imagenes1_1, im.imagenes1_2))
                        im.verif_pos_1.append((posy, posx))
                        im.barcos1_1+=1
                        if im.angulo_rotacion == 0:
                            direccion = "derecha"
                        elif im.angulo_rotacion == 180:
                            direccion = "izquierda"
                        elif im.angulo_rotacion == 90:
                            direccion = "arriba"
                        elif im.angulo_rotacion == 270:
                            direccion = "abajo"
                        insertar_piezas("A",direccion,posx,posy,mar1)

        elif config == 2:
            var = 0
            for x in im.imagenes2_1:
                var+=1
            if var < 8:
                if im.angulo_rotacion == 0 and ((posy, posx)) not in im.verif_pos_1 and ((posy, posx-1)) not in im.verif_pos_1 and im.barcos2_1 < 4:
                    if posy < rows and posx > 0 and posx < columns-1:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b2(1, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        matriz_visual[posy][posx-1].configure(image=rot.rotar_imagen_b2(2, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        im.verif_pos_1.append((posy, posx))
                        im.verif_pos_1.append((posy, posx-1))
                        im.barcos2_1+=1
                        insertar_piezas("B1","derecha",posx,posy,mar1)
                        insertar_piezas("B2","derecha",posx-1,posy,mar1)

                elif im.angulo_rotacion == 180 and ((posy, posx)) not in im.verif_pos_1 and ((posy, posx+1)) not in im.verif_pos_1 and im.barcos2_1 < 4:
                    if posx < columns-1:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b2(1, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        matriz_visual[posy][posx+1].configure(image=rot.rotar_imagen_b2(2, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        im.verif_pos_1.append((posy, posx))
                        im.verif_pos_1.append((posy, posx+1))
                        im.barcos2_1+=1
                        insertar_piezas("B1","izquierda",posx+1,posy,mar1)
                        insertar_piezas("B2","izquierda",posx,posy,mar1)

                elif im.angulo_rotacion == 90 and ((posy, posx)) not in im.verif_pos_1 and ((posy+1, posx)) not in im.verif_pos_1 and im.barcos2_1 < 4:
                    if posy < rows-1:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b2(1, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        matriz_visual[posy+1][posx].configure(image=rot.rotar_imagen_b2(2, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        im.verif_pos_1.append((posy, posx))
                        im.verif_pos_1.append((posy+1, posx))
                        im.barcos2_1+=1
                        insertar_piezas("B1","arriba",posx,posy,mar1)
                        insertar_piezas("B2","arriba",posx,posy+1,mar1)

                elif im.angulo_rotacion == 270 and ((posy, posx)) not in im.verif_pos_1 and ((posy-1, posx)) not in im.verif_pos_1 and im.barcos2_1 < 4:
                    if posy < rows:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b2(1, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        matriz_visual[posy-1][posx].configure(image=rot.rotar_imagen_b2(2, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        im.verif_pos_1.append((posy, posx))
                        im.verif_pos_1.append((posy-1, posx))
                        im.barcos2_1+=1
                        insertar_piezas("B1","abajo",posx,posy-1,mar1)
                        insertar_piezas("B2","abajo",posx,posy,mar1)

        elif config == 3:
            var = 0
            for x in im.imagenes3_1:
                var+=1
            if var < 6:
                if im.angulo_rotacion == 0 and ((posy, posx)) not in im.verif_pos_1 and ((posy, posx-1)) not in im.verif_pos_1 and ((posy, posx-2)) not in im.verif_pos_1 and im.barcos3_1 < 2:
                    if posx > 1:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b3(1, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy][posx-1].configure(image=rot.rotar_imagen_b3(2, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy][posx-2].configure(image=rot.rotar_imagen_b3(3, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        im.verif_pos_1.append((posy, posx))
                        im.verif_pos_1.append((posy, posx-1))
                        im.verif_pos_1.append((posy, posx-2))
                        im.barcos3_1+=1
                        insertar_piezas("C1","derecha",posx,posy,mar1)
                        insertar_piezas("C2","derecha",posx-1,posy,mar1)
                        insertar_piezas("C3","derecha",posx-2,posy,mar1)

                elif im.angulo_rotacion == 180 and ((posy, posx)) not in im.verif_pos_1 and ((posy, posx+1)) not in im.verif_pos_1 and ((posy, posx+2)) not in im.verif_pos_1 and im.barcos3_1 < 2:
                    if posx < columns-2:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b3(1, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy][posx+1].configure(image=rot.rotar_imagen_b3(2, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy][posx+2].configure(image=rot.rotar_imagen_b3(3, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        im.verif_pos_1.append((posy, posx))
                        im.verif_pos_1.append((posy, posx+1))
                        im.verif_pos_1.append((posy, posx+2))
                        im.barcos3_1+=1
                        insertar_piezas("C1","izquierda",posx+2,posy,mar1)
                        insertar_piezas("C2","izquierda",posx+1,posy,mar1)
                        insertar_piezas("C3","izquierda",posx,posy,mar1)

                elif im.angulo_rotacion == 90 and ((posy, posx)) not in im.verif_pos_1 and ((posy+1, posx)) not in im.verif_pos_1 and ((posy+2, posx)) not in im.verif_pos_1 and im.barcos3_1 < 2:
                    if posy < rows-2:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b3(1, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy+1][posx].configure(image=rot.rotar_imagen_b3(2, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy+2][posx].configure(image=rot.rotar_imagen_b3(3, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        im.verif_pos_1.append((posy, posx))
                        im.verif_pos_1.append((posy+1, posx))
                        im.verif_pos_1.append((posy+2, posx))
                        im.barcos3_1+=1
                        insertar_piezas("C1","arriba",posx,posy,mar1)
                        insertar_piezas("C2","arriba",posx,posy+1,mar1)
                        insertar_piezas("C3","arriba",posx,posy+2,mar1)

                elif im.angulo_rotacion == 270 and ((posy, posx)) not in im.verif_pos_1 and ((posy-1, posx)) not in im.verif_pos_1 and ((posy-2, posx)) not in im.verif_pos_1 and im.barcos3_1 < 2:
                    if posy > 1:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b3(1, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy-1][posx].configure(image=rot.rotar_imagen_b3(2, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy-2][posx].configure(image=rot.rotar_imagen_b3(3, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        im.verif_pos_1.append((posy, posx))
                        im.verif_pos_1.append((posy-1, posx))
                        im.verif_pos_1.append((posy-2, posx))
                        im.barcos3_1+=1
                        insertar_piezas("C1","abajo",posx,posy-2,mar1)
                        insertar_piezas("C2","abajo",posx,posy-1,mar1)
                        insertar_piezas("C3","abajo",posx,posy,mar1)

    #Jugador 2
    elif tur.nj == True and tur.fase_barcos_2 == True:
        if mar==1:
            return
        verif = 2
        if config == 1:
                var = 0
                for x in im.imagenes1_2:
                    var+=1
                if var < 6:
                    if ((posy, posx)) not in im.verif_pos_2 and im.barcos1_2 < 6:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen(verif, im.angulo_rotacion, im.imagenes1_1, im.imagenes1_2))
                        im.verif_pos_2.append((posy, posx))
                        im.barcos1_2+=1
                        if im.angulo_rotacion == 0:
                            direccion = "derecha"
                        elif im.angulo_rotacion == 180:
                            direccion = "izquierda"
                        elif im.angulo_rotacion == 90:
                            direccion = "arriba"
                        elif im.angulo_rotacion == 270:
                            direccion = "abajo"
                        insertar_piezas("A",direccion,posx,posy,mar2)
                        
        elif config == 2:
            var = 0
            for x in im.imagenes2_2:
                var+=1
            if var < 8:
                if im.angulo_rotacion == 0 and ((posy, posx)) not in im.verif_pos_2 and ((posy, posx-1)) not in im.verif_pos_2 and im.barcos2_2 < 4:
                    if posy < rows and posx > 0 and posx < columns-1:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b2(1, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        matriz_visual[posy][posx-1].configure(image=rot.rotar_imagen_b2(2, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        im.verif_pos_2.append((posy, posx))
                        im.verif_pos_2.append((posy, posx-1))
                        im.barcos2_2+=1
                        insertar_piezas("B1","derecha",posx,posy,mar2)
                        insertar_piezas("B2","derecha",posx-1,posy,mar2)

                elif im.angulo_rotacion == 180 and ((posy, posx)) not in im.verif_pos_2 and ((posy, posx+1)) not in im.verif_pos_2 and im.barcos2_2 < 4:
                    if posx < columns-1:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b2(1, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        matriz_visual[posy][posx+1].configure(image=rot.rotar_imagen_b2(2, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        im.verif_pos_2.append((posy, posx))
                        im.verif_pos_2.append((posy, posx+1))
                        im.barcos2_2+=1
                        insertar_piezas("B1","izquierda",posx+1,posy,mar2)
                        insertar_piezas("B2","izquierda",posx,posy,mar2)
                        
                elif im.angulo_rotacion == 90 and ((posy, posx)) not in im.verif_pos_2 and ((posy+1, posx)) not in im.verif_pos_2 and im.barcos2_2 < 4:
                    if posy < rows-1:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b2(1, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        matriz_visual[posy+1][posx].configure(image=rot.rotar_imagen_b2(2, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        im.verif_pos_2.append((posy, posx))
                        im.verif_pos_2.append((posy+1, posx))
                        im.barcos2_2+=1
                        insertar_piezas("B1","arriba",posx,posy,mar2)
                        insertar_piezas("B2","arriba",posx,posy+1,mar2)

                elif im.angulo_rotacion == 270 and ((posy, posx)) not in im.verif_pos_2 and ((posy-1, posx)) not in im.verif_pos_2 and im.barcos2_2 < 4:
                    if posy < rows:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b2(1, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        matriz_visual[posy-1][posx].configure(image=rot.rotar_imagen_b2(2, verif, im.angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                        im.verif_pos_2.append((posy, posx))
                        im.verif_pos_2.append((posy-1, posx))
                        im.barcos2_2+=1
                        insertar_piezas("B1","abajo",posx,posy-1,mar2)
                        insertar_piezas("B2","abajo",posx,posy,mar2)

        elif config == 3:
            var = 0
            for x in im.imagenes3_2:
                var+=1
            if var < 6:
                if im.angulo_rotacion == 0 and ((posy, posx)) not in im.verif_pos_2 and ((posy, posx-1)) not in im.verif_pos_2 and ((posy, posx-2)) not in im.verif_pos_2 and im.barcos3_2 < 2:
                    if posx > 1:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b3(1, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy][posx-1].configure(image=rot.rotar_imagen_b3(2, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy][posx-2].configure(image=rot.rotar_imagen_b3(3, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        im.verif_pos_2.append((posy, posx))
                        im.verif_pos_2.append((posy, posx-1))
                        im.verif_pos_2.append((posy, posx-2))
                        im.barcos3_2+=1
                        insertar_piezas("C1","derecha",posx,posy,mar2)
                        insertar_piezas("C2","derecha",posx-1,posy,mar2)
                        insertar_piezas("C3","derecha",posx-2,posy,mar2)

                elif im.angulo_rotacion == 180 and ((posy, posx)) not in im.verif_pos_2 and ((posy, posx+1)) not in im.verif_pos_2 and ((posy, posx+2)) not in im.verif_pos_2 and im.barcos3_2 < 2:
                    if posx < columns-2:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b3(1, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy][posx+1].configure(image=rot.rotar_imagen_b3(2, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy][posx+2].configure(image=rot.rotar_imagen_b3(3, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        im.verif_pos_2.append((posy, posx))
                        im.verif_pos_2.append((posy, posx+1))
                        im.verif_pos_2.append((posy, posx+2))
                        im.barcos3_2+=1
                        insertar_piezas("C1","izquierda",posx+2,posy,mar2)
                        insertar_piezas("C2","izquierda",posx+1,posy,mar2)
                        insertar_piezas("C3","izquierda",posx,posy,mar2)

                elif im.angulo_rotacion == 90 and ((posy, posx)) not in im.verif_pos_2 and ((posy+1, posx)) not in im.verif_pos_2 and ((posy+2, posx)) not in im.verif_pos_2 and im.barcos3_2 < 2:
                    if posy < rows-2:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b3(1, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy+1][posx].configure(image=rot.rotar_imagen_b3(2, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy+2][posx].configure(image=rot.rotar_imagen_b3(3, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        im.verif_pos_2.append((posy, posx))
                        im.verif_pos_2.append((posy+1, posx))
                        im.verif_pos_2.append((posy+2, posx))
                        im.barcos3_2+=1
                        insertar_piezas("C1","arriba",posx,posy,mar2)
                        insertar_piezas("C2","arriba",posx,posy+1,mar2)
                        insertar_piezas("C3","arriba",posx,posy+2,mar2)

                elif im.angulo_rotacion == 270 and ((posy, posx)) not in im.verif_pos_2 and ((posy-1, posx)) not in im.verif_pos_2 and ((posy-2, posx)) not in im.verif_pos_2 and im.barcos3_2 < 2:
                    if posy > 1:
                        matriz_visual[posy][posx].configure(image=rot.rotar_imagen_b3(1, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy-1][posx].configure(image=rot.rotar_imagen_b3(2, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        matriz_visual[posy-2][posx].configure(image=rot.rotar_imagen_b3(3, verif, im.angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                        im.verif_pos_2.append((posy, posx))
                        im.verif_pos_2.append((posy-1, posx))
                        im.verif_pos_2.append((posy-2, posx))
                        im.barcos3_2+=1
                        insertar_piezas("C1","abajo",posx,posy-2,mar2)
                        insertar_piezas("C2","abajo",posx,posy-1,mar2)
                        insertar_piezas("C3","abajo",posx,posy,mar2)