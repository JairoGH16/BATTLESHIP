import movimiento as mov
import rotar_imagenes as rot
import var_imagenes as im

mi = True
nj = False
fnl = False
fase_barcos_1 = True
fase_barcos_2 = True

def next_pj(matriz1, matriz2):
    global mi, nj, fnl, fase_barcos_1, fase_barcos_2
    if fnl == True:
        mov.mover_barcos()
        rest_barcos_1(matriz1)
        nj = False
        mi = True
        fnl = False
        return(nj, mi, fnl)
    elif nj == False and fnl == False:
        for fila in matriz1:
            for boton in fila:
                boton.configure(image="")
        nj = None
        mi = None
        fase_barcos_1 = False
        return(nj, mi, fnl)
    elif nj == None and fnl == False:
        nj = True
        mi = False
        #llamar a rest_barcos_2
        return(nj, mi, fnl)
    elif nj == True and fnl == False:
        for fila in matriz2:
            for boton in fila:
                boton.configure(image="")
        nj = False
        fnl = True
        mi = None
        fase_barcos_2 = False
        return(nj, mi, fnl)

def rest_barcos_1(matriz_botones):
    global angulo_rotacion
    posy=0
    for fila in mov.mar:
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
                posx += 1
            posy += 1
    return(matriz_botones)