import logica.movimiento as mov
import rotar_imagenes as rot
import var_imagenes as im
import tkinter as tk

mi = True
nj = False
fnl = False
fase_barcos_1 = True
fase_barcos_2 = True
turno=1
ataque_posible=False

def next_pj(matriz1,matriz2,mar1,mar2):
    """Esta funcion se encarga de llevar los turnos de los Jugadores, dejando entre cada turno un espacio neutro para el manejo del juego en un solo dispositivo.

    Args:
        matriz1 (_type_): Matriz del Jugador 1
        matriz2 (_type_): Matriz del Jugador 2
        mar1 (_type_): Matriz logica del Jugador 1
        mar2 (_type_): Matriz logica del Jugador 2

    Autor: Rafael Odio
    """
    global mi, nj, fnl, fase_barcos_1, fase_barcos_2, turno, ataque_posible
    if fnl == True:
        ataque_posible=True
        mov.mover_barcos(mar1)
        rest_barcos(matriz1,mar1)
        nj = False
        mi = True
        fnl = False
        return(nj, mi, fnl)
    elif nj == False and fnl == False:
        if (len(im.imagenes1_1) == 6 and len(im.imagenes2_1) == 8 and len(im.imagenes3_1) == 6) or fase_barcos_1 == False:
            for fila in matriz1:
                for boton in fila:
                    boton.configure(image="")
            nj = None
            mi = None
            fase_barcos_1 = False
            turno+=1
            return(nj, mi, fnl)
        else:
            pass
    elif nj == None and fnl == False:
        ataque_posible=True
        mov.mover_barcos(mar2)
        rest_barcos(matriz2,mar2)#llamar rest barcos 2
        nj = True
        mi = False
        return(nj, mi, fnl)
    elif nj == True and fnl == False:
        if (len(im.imagenes1_2) == 6 and len(im.imagenes2_2) == 8 and len(im.imagenes3_2) == 6) or fase_barcos_2 == False:
            for fila in matriz2:
                for boton in fila:
                    boton.configure(image="")
            nj = False
            fnl = True
            mi = None
            fase_barcos_2 = False
            turno+=1
            return(nj, mi, fnl)

def rest_barcos(matriz_botones,mar):
    """Esta funcion se encarga de volver visibles los barcos del jugador actual

    Args:
        matriz_botones (_type_): Matriz en la que se van a revelar los barcos
        mar (_type_): Matriz logica a travez de la cual se tomaran los barcos a reflejar

    Autor: Rafael Odio
    """
    global angulo_rotacion
    posy=0
    for fila in mar:
        posx = 0
        for boton in fila:
            if boton["direccion"] == "arriba":
                angulo_rotacion = 90
            elif boton["direccion"] == "abajo":
                angulo_rotacion = 270
            elif boton["direccion"] == "derecha":
                angulo_rotacion = 0
            elif boton["direccion"] == "izquierda":
                angulo_rotacion = 180
            if boton["pieza"] == "A":
                matriz_botones[posy][posx].configure(image=rot.rotar_imagen(1, angulo_rotacion, im.imagenes1_1, im.imagenes1_2))
            if boton["pieza"] == "B1" and boton["direccion"] == "derecha":
                matriz_botones[posy][posx].configure(image=rot.rotar_imagen_b2(1,1, angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                matriz_botones[posy][posx-1].configure(image=rot.rotar_imagen_b2(2,1, angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
            if boton["pieza"] == "B1" and boton["direccion"] == "izquierda":
                matriz_botones[posy][posx].configure(image=rot.rotar_imagen_b2(2,1, angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                matriz_botones[posy][posx-1].configure(image=rot.rotar_imagen_b2(1,1, angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
            if boton["pieza"] == "B2" and boton["direccion"] == "arriba":
                matriz_botones[posy-1][posx].configure(image=rot.rotar_imagen_b2(1,1, angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                matriz_botones[posy][posx].configure(image=rot.rotar_imagen_b2(2,1, angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
            if boton["pieza"] == "B2" and boton["direccion"] == "abajo":
                matriz_botones[posy-1][posx].configure(image=rot.rotar_imagen_b2(2,1, angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
                matriz_botones[posy][posx].configure(image=rot.rotar_imagen_b2(1,1, angulo_rotacion, im.imagenes2_1, im.imagenes2_2))
            if boton["pieza"] == "C1" and boton["direccion"] == "derecha":
                matriz_botones[posy][posx].configure(image=rot.rotar_imagen_b3(1,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                matriz_botones[posy][posx-1].configure(image=rot.rotar_imagen_b3(2,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                matriz_botones[posy][posx-2].configure(image=rot.rotar_imagen_b3(3,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
            if boton["pieza"] == "C1" and boton["direccion"] == "izquierda":
                matriz_botones[posy][posx].configure(image=rot.rotar_imagen_b3(3,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                matriz_botones[posy][posx-1].configure(image=rot.rotar_imagen_b3(2,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                matriz_botones[posy][posx-2].configure(image=rot.rotar_imagen_b3(1,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
            if boton["pieza"] == "C3" and boton["direccion"] == "arriba":
                matriz_botones[posy-2][posx].configure(image=rot.rotar_imagen_b3(1,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                matriz_botones[posy-1][posx].configure(image=rot.rotar_imagen_b3(2,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                matriz_botones[posy][posx].configure(image=rot.rotar_imagen_b3(3,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
            if boton["pieza"] == "C3" and boton["direccion"] == "abajo":
                matriz_botones[posy][posx].configure(image=rot.rotar_imagen_b3(1,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                matriz_botones[posy-1][posx].configure(image=rot.rotar_imagen_b3(2,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
                matriz_botones[posy-2][posx].configure(image=rot.rotar_imagen_b3(3,1, angulo_rotacion, im.imagenes3_1, im.imagenes3_2))
            if boton["danado"] == True:
                matriz_botones[posy][posx].configure(bg="red")
            posx += 1
        posy += 1
    return(matriz_botones)