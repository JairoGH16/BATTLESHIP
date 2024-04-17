import tkinter as tk
from PIL import ImageTk, Image
import os

angulo_rotacion = 0
config = 1
nj = False
imagenes1_1 = []
imagenes1_2 = []
imagenes2_1 = []
imagenes2_2 = []
imagenes3_1 = []
imagenes3_2 = []
verif_pos_1 = []
verif_pos_2 = []
barcos_jugador1 = []
barcos_jugador2 = []
current_dir = os.path.dirname(os.path.abspath(__file__))

def cambiar_config(num:int):
    global config
    if num == 1:
        config = 1
    if num == 2:
        config = 2
    if num == 3:
        config =3

def salir_juego():
    exit()

def mostrar_imagen(event):
    if nj == False:
        boton = event.widget
        for f in range(len(matriz_botones)):
            for c in range(len(matriz_botones[f])):
                if matriz_botones[f][c] == boton:
                    if config == 1:
                        boton.configure(bg="Green")
                    try:
                        if config == 2 and angulo_rotacion == 0:
                            if c > 0:
                                boton.configure(bg="Green")
                                matriz_botones[f][c-1].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 2 and angulo_rotacion == 270:
                            if f > 0:
                                boton.configure(bg="Green")
                                matriz_botones[f-1][c].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 2 and angulo_rotacion == 180:
                            if c < columns:
                                boton.configure(bg="Green")
                                matriz_botones[f][c+1].configure(bg="Green")
                            if c == columns:
                                boton.configure(bg="Red")
                        elif config == 2 and angulo_rotacion == 90:
                            if f < rows:
                                boton.configure(bg="Green")
                                matriz_botones[f+1][c].configure(bg="Green")
                    except IndexError:
                        boton.configure(bg="Red")
                    try:
                        if config == 3 and angulo_rotacion == 0:
                            if c > 1:
                                boton.configure(bg="Green")
                                matriz_botones[f][c-1].configure(bg="Green")
                                matriz_botones[f][c-2].configure(bg="Green")
                            elif c > 0:
                                boton.configure(bg="Red")
                                matriz_botones[f][c-1].configure(bg="Red")
                            elif c == 0:
                                boton.configure(bg="Red")
                        elif config == 3 and angulo_rotacion == 270:
                            if f > 1:
                                boton.configure(bg="Green")
                                matriz_botones[f-1][c].configure(bg="Green")
                                matriz_botones[f-2][c].configure(bg="Green")
                            elif f == 1:
                                boton.configure(bg="Red")
                                matriz_botones[f-1][c].configure(bg="Red")
                            elif f == 0:
                                boton.configure(bg="Red")
                        elif config == 3 and angulo_rotacion == 180:
                            if c < columns-1:
                                boton.configure(bg="Green")
                                matriz_botones[f][c+1].configure(bg="Green")
                                matriz_botones[f][c+2].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 3 and angulo_rotacion == 90:
                            if f < rows-1:
                                boton.configure(bg="Green")
                                matriz_botones[f+1][c].configure(bg="Green")
                                matriz_botones[f+2][c].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                                matriz_botones[f+1][c].configure(bg="Red")
                    except IndexError:
                        boton.configure(bg="Red")
                        if angulo_rotacion == 180:
                            boton.configure(bg="Red")
                            matriz_botones[f][c+1].configure(bg="Red")
                        if angulo_rotacion == 270:
                            boton.configure(bg="Red")
                            matriz_botones[f+1][c].configure(bg="Red")
                        if angulo_rotacion == 90:
                            boton.configure(bg="Red")
                            matriz_botones[f+1][c].configure(bg="Red")
                        break

def mostrar_imagen_2(event):
    if nj == True:
        boton = event.widget
        for f in range(len(matriz_botones_2)):
            for c in range(len(matriz_botones_2[f])):
                if matriz_botones_2[f][c] == boton:
                    if config == 1:
                        boton.configure(bg="Green")
                    try:
                        if config == 2 and angulo_rotacion == 0:
                            if c > 0:
                                boton.configure(bg="Green")
                                matriz_botones_2[f][c-1].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 2 and angulo_rotacion == 270:
                            if f > 0:
                                boton.configure(bg="Green")
                                matriz_botones_2[f-1][c].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 2 and angulo_rotacion == 180:
                            if c < columns:
                                boton.configure(bg="Green")
                                matriz_botones_2[f][c+1].configure(bg="Green")
                            if c == columns:
                                boton.configure(bg="Red")
                        elif config == 2 and angulo_rotacion == 90:
                            if f < rows:
                                boton.configure(bg="Green")
                                matriz_botones_2[f+1][c].configure(bg="Green")
                    except IndexError:
                        boton.configure(bg="Red")
                    try:
                        if config == 3 and angulo_rotacion == 0:
                            if c > 1:
                                boton.configure(bg="Green")
                                matriz_botones_2[f][c-1].configure(bg="Green")
                                matriz_botones_2[f][c-2].configure(bg="Green")
                            elif c > 0:
                                boton.configure(bg="Red")
                                matriz_botones_2[f][c-1].configure(bg="Red")
                            elif c == 0:
                                boton.configure(bg="Red")
                        elif config == 3 and angulo_rotacion == 270:
                            if f > 1:
                                boton.configure(bg="Green")
                                matriz_botones_2[f-1][c].configure(bg="Green")
                                matriz_botones_2[f-2][c].configure(bg="Green")
                            elif f == 1:
                                boton.configure(bg="Red")
                                matriz_botones_2[f-1][c].configure(bg="Red")
                            elif f == 0:
                                boton.configure(bg="Red")
                        elif config == 3 and angulo_rotacion == 180:
                            if c < columns-1:
                                boton.configure(bg="Green")
                                matriz_botones_2[f][c+1].configure(bg="Green")
                                matriz_botones_2[f][c+2].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 3 and angulo_rotacion == 90:
                            if f < rows-1:
                                boton.configure(bg="Green")
                                matriz_botones_2[f+1][c].configure(bg="Green")
                                matriz_botones_2[f+2][c].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                                matriz_botones_2[f+1][c].configure(bg="Red")
                    except IndexError:
                        boton.configure(bg="Red")
                        if angulo_rotacion == 180:
                            boton.configure(bg="Red")
                            matriz_botones_2[f][c+1].configure(bg="Red")
                        if angulo_rotacion == 270:
                            boton.configure(bg="Red")
                            matriz_botones_2[f+1][c].configure(bg="Red")
                        if angulo_rotacion == 90:
                            boton.configure(bg="Red")
                            matriz_botones_2[f+1][c].configure(bg="Red")
                        break

def ocultar_imagen(event):
    if nj == False:
        boton = event.widget
        for f in range(len(matriz_botones)):
            for c in range(len(matriz_botones[f])):
                if matriz_botones[f][c] == boton:
                    boton.configure(bg="Blue")
                    if config == 2 and angulo_rotacion == 0:
                        if c > 0:
                            matriz_botones[f][c-1].configure(bg="Blue")
                    elif config == 2 and angulo_rotacion == 270:
                        matriz_botones[f-1][c].configure(bg="Blue")
                    elif config == 2 and angulo_rotacion == 180:
                        matriz_botones[f][c+1].configure(bg="Blue")
                    elif config == 2 and angulo_rotacion == 90:
                        matriz_botones[f+1][c].configure(bg="Blue")
                    if config == 3 and angulo_rotacion == 0:
                        matriz_botones[f][c-1].configure(bg="Blue")
                        matriz_botones[f][c-2].configure(bg="Blue")
                    elif config == 3 and angulo_rotacion == 270:
                        matriz_botones[f-1][c].configure(bg="Blue")
                        matriz_botones[f-2][c].configure(bg="Blue")
                    elif config == 3 and angulo_rotacion == 180:
                        matriz_botones[f][c+1].configure(bg="Blue")
                        matriz_botones[f][c+2].configure(bg="Blue")
                    elif config == 3 and angulo_rotacion == 90:
                        matriz_botones[f+1][c].configure(bg="Blue")
                        matriz_botones[f+2][c].configure(bg="Blue")
                    break

def ocultar_imagen_2(event):
    if nj == True:
        boton = event.widget
        for f in range(len(matriz_botones_2)):
            for c in range(len(matriz_botones_2[f])):
                if matriz_botones_2[f][c] == boton:
                    boton.configure(bg="Blue")
                    if config == 2 and angulo_rotacion == 0:
                        if c > 0:
                            matriz_botones_2[f][c-1].configure(bg="Blue")
                    elif config == 2 and angulo_rotacion == 270:
                        matriz_botones_2[f-1][c].configure(bg="Blue")
                    elif config == 2 and angulo_rotacion == 180:
                        matriz_botones_2[f][c+1].configure(bg="Blue")
                    elif config == 2 and angulo_rotacion == 90:
                        matriz_botones_2[f+1][c].configure(bg="Blue")
                    if config == 3 and angulo_rotacion == 0:
                        matriz_botones_2[f][c-1].configure(bg="Blue")
                        matriz_botones_2[f][c-2].configure(bg="Blue")
                    elif config == 3 and angulo_rotacion == 270:
                        matriz_botones_2[f-1][c].configure(bg="Blue")
                        matriz_botones_2[f-2][c].configure(bg="Blue")
                    elif config == 3 and angulo_rotacion == 180:
                        matriz_botones_2[f][c+1].configure(bg="Blue")
                        matriz_botones_2[f][c+2].configure(bg="Blue")
                    elif config == 3 and angulo_rotacion == 90:
                        matriz_botones_2[f+1][c].configure(bg="Blue")
                        matriz_botones_2[f+2][c].configure(bg="Blue")
                    break

def extra_barcos(posx, posy):
    global verif
    if nj == False:
        verif = 1
        if config == 1:
                var = 0
                for x in imagenes1_1:
                    var+=1
                if var < 6:
                    if ((posy, posx)) not in verif_pos_1:
                        matriz_botones[posy][posx].configure(image=rotar_imagen(verif))
                        verif_pos_1.append((posy, posx))
                        barcos_jugador1.append([1, [posy, posx], angulo_rotacion, [posy, posx], [posy, posx]])
        elif config == 2:
            var = 0
            for x in imagenes2_1:
                var+=1
            if var < 8:
                if angulo_rotacion == 0 and ((posy, posx)) not in verif_pos_1 and ((posy, posx-1)) not in verif_pos_1:
                    if posy < rows and posx > 0 and posx < columns-1:
                        matriz_botones[posy][posx].configure(image=rotar_imagen_b2(1, verif))
                        matriz_botones[posy][posx-1].configure(image=rotar_imagen_b2(2, verif))
                        verif_pos_1.append((posy, posx))
                        verif_pos_1.append((posy, posx-1))
                        barcos_jugador1.append((2, (posy, posx), angulo_rotacion, (posy, posx-1), (posy, posx)))

                elif angulo_rotacion == 180 and ((posy, posx)) not in verif_pos_1 and ((posy, posx+1)) not in verif_pos_1:
                    if posx < columns-1:
                        matriz_botones[posy][posx].configure(image=rotar_imagen_b2(1, verif))
                        matriz_botones[posy][posx+1].configure(image=rotar_imagen_b2(2, verif))
                        verif_pos_1.append((posy, posx))
                        verif_pos_1.append((posy, posx+1))
                        barcos_jugador1.append((2, (posy, posx), angulo_rotacion, (posy, posx+1), (posy, posx)))

                elif angulo_rotacion == 90 and ((posy, posx)) not in verif_pos_1 and ((posy+1, posx)) not in verif_pos_1:
                    if posy < rows-1:
                        matriz_botones[posy][posx].configure(image=rotar_imagen_b2(1, verif))
                        matriz_botones[posy+1][posx].configure(image=rotar_imagen_b2(2, verif))
                        verif_pos_1.append((posy, posx))
                        verif_pos_1.append((posy+1, posx))
                        barcos_jugador1.append((2, (posy, posx), angulo_rotacion, (posy+1, posx), (posy, posx)))

                elif angulo_rotacion == 270 and ((posy, posx)) not in verif_pos_1 and ((posy-1, posx)) not in verif_pos_1:
                    if posy < rows:
                        matriz_botones[posy][posx].configure(image=rotar_imagen_b2(1, verif))
                        matriz_botones[posy-1][posx].configure(image=rotar_imagen_b2(2, verif))
                        verif_pos_1.append((posy, posx))
                        verif_pos_1.append((posy-1, posx))
                        barcos_jugador1.append((2, (posy, posx), angulo_rotacion, (posy-1, posx), (posy, posx)))

        elif config == 3:
            var = 0
            for x in imagenes3_1:
                var+=1
            if var < 6:
                if angulo_rotacion == 0 and ((posy, posx)) not in verif_pos_1 and ((posy, posx-1)) not in verif_pos_1 and ((posy, posx-2)) not in verif_pos_1:
                    if posx > 1:
                        matriz_botones[posy][posx].configure(image=rotar_imagen_b3(1, verif))
                        matriz_botones[posy][posx-1].configure(image=rotar_imagen_b3(2, verif))
                        matriz_botones[posy][posx-2].configure(image=rotar_imagen_b3(3, verif))
                        verif_pos_1.append((posy, posx))
                        verif_pos_1.append((posy, posx-1))
                        verif_pos_1.append((posy, posx-2))
                        barcos_jugador1.append((3, (posy, posx), angulo_rotacion, (posy, posx-1), (posy, posx-2)))

                elif angulo_rotacion == 180 and ((posy, posx)) not in verif_pos_1 and ((posy, posx+1)) not in verif_pos_1 and ((posy, posx+2)) not in verif_pos_1:
                    if posx < columns-2:
                        matriz_botones[posy][posx].configure(image=rotar_imagen_b3(1, verif))
                        matriz_botones[posy][posx+1].configure(image=rotar_imagen_b3(2, verif))
                        matriz_botones[posy][posx+2].configure(image=rotar_imagen_b3(3, verif))
                        verif_pos_1.append((posy, posx))
                        verif_pos_1.append((posy, posx+1))
                        verif_pos_1.append((posy, posx+2))
                        barcos_jugador1.append((3, (posy, posx), angulo_rotacion, (posy, posx+1), (posy, posx+2)))

                elif angulo_rotacion == 90 and ((posy, posx)) not in verif_pos_1 and ((posy+1, posx)) not in verif_pos_1 and ((posy+2, posx)) not in verif_pos_1:
                    if posy < rows-2:
                        matriz_botones[posy][posx].configure(image=rotar_imagen_b3(1, verif))
                        matriz_botones[posy+1][posx].configure(image=rotar_imagen_b3(2, verif))
                        matriz_botones[posy+2][posx].configure(image=rotar_imagen_b3(3, verif))
                        verif_pos_1.append((posy, posx))
                        verif_pos_1.append((posy+1, posx))
                        verif_pos_1.append((posy+2, posx))
                        barcos_jugador1.append((3, (posy, posx), angulo_rotacion, (posy+1, posx), (posy+2, posx)))

                elif angulo_rotacion == 270 and ((posy, posx)) not in verif_pos_1 and ((posy-1, posx)) not in verif_pos_1 and ((posy-2, posx)) not in verif_pos_1:
                    if posy > 1:
                        matriz_botones[posy][posx].configure(image=rotar_imagen_b3(1, verif))
                        matriz_botones[posy-1][posx].configure(image=rotar_imagen_b3(2, verif))
                        matriz_botones[posy-2][posx].configure(image=rotar_imagen_b3(3, verif))
                        verif_pos_1.append((posy, posx))
                        verif_pos_1.append((posy-1, posx))
                        verif_pos_1.append((posy-2, posx))
                        barcos_jugador1.append((3, (posy, posx), angulo_rotacion, (posy-1, posx), (posy-2, posx)))

def extra_barcos_2(posx, posy):
    global verif
    if nj == True:
        verif = 2
        if config == 1:
                var = 0
                for x in imagenes1_2:
                    var+=1
                if var < 6:
                    if ((posy, posx)) not in verif_pos_2:
                        matriz_botones_2[posy][posx].configure(image=rotar_imagen(verif))
                        verif_pos_2.append((posy, posx))
                        barcos_jugador2.append((1, (posy, posx), angulo_rotacion, (posy, posx), (posy, posx)))

        elif config == 2:
            var = 0
            for x in imagenes2_2:
                var+=1
            if var < 8:
                if angulo_rotacion == 0 and ((posy, posx)) not in verif_pos_2 and ((posy, posx-1)) not in verif_pos_2:
                    if posy < rows and posx > 0 and posx < columns-1:
                        matriz_botones_2[posy][posx].configure(image=rotar_imagen_b2(1, verif))
                        matriz_botones_2[posy][posx-1].configure(image=rotar_imagen_b2(2, verif))
                        verif_pos_2.append((posy, posx))
                        verif_pos_2.append((posy, posx-1))
                        barcos_jugador2.append((2, (posy, posx), angulo_rotacion, (posy, posx-1), (posy, posx)))

                elif angulo_rotacion == 180 and ((posy, posx)) not in verif_pos_2 and ((posy, posx+1)) not in verif_pos_2:
                    if posx < columns-1:
                        matriz_botones_2[posy][posx].configure(image=rotar_imagen_b2(1, verif))
                        matriz_botones_2[posy][posx+1].configure(image=rotar_imagen_b2(2, verif))
                        verif_pos_2.append((posy, posx))
                        verif_pos_2.append((posy, posx+1))
                        barcos_jugador2.append((2, (posy, posx), angulo_rotacion, (posy, posx+1), (posy, posx)))
                        
                elif angulo_rotacion == 90 and ((posy, posx)) not in verif_pos_2 and ((posy+1, posx)) not in verif_pos_2:
                    if posy < rows-1:
                        matriz_botones_2[posy][posx].configure(image=rotar_imagen_b2(1, verif))
                        matriz_botones_2[posy+1][posx].configure(image=rotar_imagen_b2(2, verif))
                        verif_pos_2.append((posy, posx))
                        verif_pos_2.append((posy+1, posx))
                        barcos_jugador2.append((2, (posy, posx), angulo_rotacion, (posy+1, posx), (posy, posx)))

                elif angulo_rotacion == 270 and ((posy, posx)) not in verif_pos_2 and ((posy-1, posx)) not in verif_pos_2:
                    if posy < rows:
                        matriz_botones_2[posy][posx].configure(image=rotar_imagen_b2(1, verif))
                        matriz_botones_2[posy-1][posx].configure(image=rotar_imagen_b2(2, verif))
                        verif_pos_2.append((posy, posx))
                        verif_pos_2.append((posy-1, posx))
                        barcos_jugador2.append((2, (posy, posx), angulo_rotacion, (posy-1, posx), (posy, posx)))

        elif config == 3:
            var = 0
            for x in imagenes3_2:
                var+=1
            if var < 6:
                if angulo_rotacion == 0 and ((posy, posx)) not in verif_pos_2 and ((posy, posx-1)) not in verif_pos_2 and ((posy, posx-2)) not in verif_pos_2:
                    if posx > 1:
                        matriz_botones_2[posy][posx].configure(image=rotar_imagen_b3(1, verif))
                        matriz_botones_2[posy][posx-1].configure(image=rotar_imagen_b3(2, verif))
                        matriz_botones_2[posy][posx-2].configure(image=rotar_imagen_b3(3, verif))
                        verif_pos_2.append((posy, posx))
                        verif_pos_2.append((posy, posx-1))
                        verif_pos_2.append((posy, posx-2))
                        barcos_jugador2.append((3, (posy, posx), angulo_rotacion, (posy, posx-1), (posy, posx-2)))

                elif angulo_rotacion == 180 and ((posy, posx)) not in verif_pos_2 and ((posy, posx+1)) not in verif_pos_2 and ((posy, posx+2)) not in verif_pos_2:
                    if posx < columns-2:
                        matriz_botones_2[posy][posx].configure(image=rotar_imagen_b3(1, verif))
                        matriz_botones_2[posy][posx+1].configure(image=rotar_imagen_b3(2, verif))
                        matriz_botones_2[posy][posx+2].configure(image=rotar_imagen_b3(3, verif))
                        verif_pos_2.append((posy, posx))
                        verif_pos_2.append((posy, posx+1))
                        verif_pos_2.append((posy, posx+2))
                        barcos_jugador2.append((3, (posy, posx), angulo_rotacion, (posy, posx+1), (posy, posx+2)))

                elif angulo_rotacion == 90 and ((posy, posx)) not in verif_pos_2 and ((posy+1, posx)) not in verif_pos_2 and ((posy+2, posx)) not in verif_pos_2:
                    if posy < rows-2:
                        matriz_botones_2[posy][posx].configure(image=rotar_imagen_b3(1, verif))
                        matriz_botones_2[posy+1][posx].configure(image=rotar_imagen_b3(2, verif))
                        matriz_botones_2[posy+2][posx].configure(image=rotar_imagen_b3(3, verif))
                        verif_pos_2.append((posy, posx))
                        verif_pos_2.append((posy+1, posx))
                        verif_pos_2.append((posy+2, posx))
                        barcos_jugador2.append((3, (posy, posx), angulo_rotacion, (posy+1, posx), (posy+2, posx)))

                elif angulo_rotacion == 270 and ((posy, posx)) not in verif_pos_2 and ((posy-1, posx)) not in verif_pos_2 and ((posy-2, posx)) not in verif_pos_2:
                    if posy > 1:
                        matriz_botones_2[posy][posx].configure(image=rotar_imagen_b3(1, verif))
                        matriz_botones_2[posy-1][posx].configure(image=rotar_imagen_b3(2, verif))
                        matriz_botones_2[posy-2][posx].configure(image=rotar_imagen_b3(3, verif))
                        verif_pos_2.append((posy, posx))
                        verif_pos_2.append((posy-1, posx))
                        verif_pos_2.append((posy-2, posx))
                        barcos_jugador2.append((3, (posy, posx), angulo_rotacion, (posy-1, posx), (posy-2, posx)))

def rotar_imagen(verif):
    global imagen, angulo_rotacion
    imagen_pil1 = Image.open(os.path.join(current_dir, f'b1.png'))
    imagen_rotada1 = imagen_pil1.rotate(angulo_rotacion, expand=True)
    imagen_rotada1 = imagen_rotada1.resize((50, 50))
    global imagen1
    imagen1 = ImageTk.PhotoImage(imagen_rotada1)
    if verif == 1:
        imagenes1_1.append(imagen1)
    if verif == 2:
        imagenes1_2.append(imagen1)
    return imagen1

def rotar_imagen_b2(num, verif):
    imagen_pil = Image.open(os.path.join(current_dir, f'b2{num}.png'))
    imagen_rotada = imagen_pil.rotate(angulo_rotacion, expand=True)
    imagen_rotada = imagen_rotada.resize((50, 50))
    global imagen2
    imagen2 = ImageTk.PhotoImage(imagen_rotada)
    if verif == 1:
        imagenes2_1.append(imagen2)
    if verif == 2:
        imagenes2_2.append(imagen2)
    return imagen2

def rotar_imagen_b3(num, verif):
    imagen_pil = Image.open(os.path.join(current_dir, f'b3{num}.png'))
    imagen_rotada = imagen_pil.rotate(angulo_rotacion, expand=True)
    imagen_rotada = imagen_rotada.resize((50, 50))
    global imagen3
    imagen3 = ImageTk.PhotoImage(imagen_rotada)
    if verif == 1:
        imagenes3_1.append(imagen3)
    if verif == 2:
        imagenes3_2.append(imagen3)
    return imagen3

def iniciar_juego(x, y, j1, j2):
    global rows, columns
    rows = y
    columns = x
    for widget in ventana.winfo_children():
        widget.destroy()  # Limpiar la ventana
    ventana.state("zoomed")
    ventana.title("Tablero")

    global matriz_botones, matriz_botones_2
    matriz_botones = [[tk.Button(ventana, command=lambda posx=c, posy=f: extra_barcos(posx, posy), bg="Blue") for c in range(x // 2)] for f in range(y)]

    # Crear una segunda matriz de botones
    matriz_botones_2 = [[tk.Button(ventana, command=lambda posx=c, posy=f: extra_barcos_2(posx, posy), bg="Blue") for c in range(x - x // 2)] for f in range(y)]

    # Calcular las posiciones x e y para centrar las matrices
    ancho_ventana = ventana.winfo_screenwidth()
    posx_matriz1 = (ancho_ventana//2)-(x*50//2)-20 # Restar 100 píxeles para dejar espacio
    posy_matriz1 = 50
    posx_matriz2 = (ancho_ventana//2)+20  # Sumar 150 píxeles para dejar espacio
    posy = posy_matriz1
    for fila_botones, fila_botones_2 in zip(matriz_botones, matriz_botones_2):
        posx = posx_matriz1
        posx2 = posx_matriz2
        for boton, boton2 in zip(fila_botones, fila_botones_2):
            boton.place(x=posx, y=posy, height=50, width=50)
            boton2.place(x=posx2, y=posy, height=50, width=50)
            boton.bind("<Leave>", ocultar_imagen)
            boton.bind("<Enter>", mostrar_imagen)
            boton2.bind("<Leave>", ocultar_imagen_2)
            boton2.bind("<Enter>", mostrar_imagen_2)
            posx += 50
            posx2 += 50
        posy += 50

    rot_derecha = tk.Button(ventana, command=rotar_barco_d)
    rot_derecha.place(x=x*10,y=y*50+50)
    rot_derecha.configure(text="Derecha",font=("",14))

    rot_izquierda = tk.Button(ventana, command=rotar_barco_i)
    rot_izquierda.place(x=x*10,y=y*50+100)
    rot_izquierda.configure(text="Izquierda",font=("",14))

    rot_arriba = tk.Button(ventana, command=rotar_barco_a)
    rot_arriba.place(x=x*10+100,y=y*50+50)
    rot_arriba.configure(text="Arriba",font=("",14))

    rot_abajo = tk.Button(ventana, command=rotar_barco_b)
    rot_abajo.place(x=x*10+100,y=y*50+100)
    rot_abajo.configure(text="Abajo",font=("",14))

    config1 = tk.Button(ventana)
    config2 = tk.Button(ventana)
    config3 = tk.Button(ventana)

    config1.place(x=x*25,y=y*50+50)
    config2.place(x=x*25,y=y*50+80)
    config3.place(x=x*25,y=y*50+110)

    config1.configure(text="1 Barco", command=lambda: cambiar_config(1))
    config2.configure(text="2 Barcos", command=lambda: cambiar_config(2))
    config3.configure(text="3 Barcos", command=lambda: cambiar_config(3))

    reiniciar = tk.Button(ventana)
    reiniciar.place(x=x*25+100,y=y*50+110)
    reiniciar.configure(command=lambda: restart(x, y, j1, j2), text="Reiniciar")

    Jug1 = tk.Label(text=f"{j1}", font=("Comic Sans MS", 20), bg="LightBlue")
    label_x = posx_matriz1+(x//2)*50//2-Jug1.winfo_reqwidth()//2
    label_y = posy_matriz1-50  # Adjust the value as needed
    Jug1.place(x=label_x, y=label_y)

    Jug2 = tk.Label(text=f"{j2}", font=("Comic Sans MS", 20), bg="LightBlue")
    label_x = posx_matriz2+(x//2)*50//2-Jug2.winfo_reqwidth()//2
    label_y = posy_matriz1-50  # Adjust the value as needed
    Jug2.place(x=label_x, y=label_y)

    nj = tk.Button(ventana)
    nj.place(x=x*25+200, y=y*50+110)
    nj.configure(text="Siguiente Jugador", command=lambda: next_pj())

def next_pj():
    global nj
    if nj == True:
        for fila in matriz_botones_2:
            for boton in fila:
                for i in imagenes1_2:
                    if boton["image"] == str(i):
                        boton.configure(image=ImageTk.PhotoImage(Image.open(os.path.join(current_dir, f'b11.png'))))
                for i in imagenes2_2:
                    if boton["image"] == str(i):
                        boton.configure(image=ImageTk.PhotoImage(Image.open(os.path.join(current_dir, f'b11.png'))))
                for i in imagenes3_2:
                    if boton["image"] == str(i):
                        boton.configure(image=ImageTk.PhotoImage(Image.open(os.path.join(current_dir, f'b11.png'))))
        mover_barcos_1()
        restaurar_barcos_1()
        nj = False
    elif nj == False:
        for fila in matriz_botones:
            for boton in fila:
                for i in imagenes1_1:
                    if boton["image"] == str(i):
                        boton.configure(image=ImageTk.PhotoImage(Image.open(os.path.join(current_dir, f'b11.png'))))
                for i in imagenes2_1:
                    if boton["image"] == str(i):
                        boton.configure(image=ImageTk.PhotoImage(Image.open(os.path.join(current_dir, f'b11.png'))))
                for i in imagenes3_1:
                    if boton["image"] == str(i):
                        boton.configure(image=ImageTk.PhotoImage(Image.open(os.path.join(current_dir, f'b11.png'))))
        restaurar_barcos_2()
        nj = True

def restaurar_barcos_1():
    for tipo, posicion1, rotacion, posicion2, posicion3 in barcos_jugador1:
        t = tipo
        fila1, columna1 = posicion1
        fila2, columna2 = posicion2
        fila3, columna3 = posicion3
        global angulo_rotacion
        angulo_rotacion = rotacion
        if t == 3:
            matriz_botones[fila1][columna1].configure(image=rotar_imagen_b3(1, 1))
            matriz_botones[fila2][columna2].configure(image=rotar_imagen_b3(2, 1))
            matriz_botones[fila3][columna3].configure(image=rotar_imagen_b3(3, 1))
        if t == 2:
            matriz_botones[fila1][columna1].configure(image=rotar_imagen_b2(1, 1))
            matriz_botones[fila2][columna2].configure(image=rotar_imagen_b2(2, 1))
        if t == 1:
            if limite == False:
                matriz_botones[fila1][columna1].configure(image=rotar_imagen(1))

def restaurar_barcos_2():
    for tipo, posicion1, rotacion, posicion2, posicion3 in barcos_jugador2:
        t = tipo
        fila1, columna1 = posicion1
        fila2, columna2 = posicion2
        fila3, columna3 = posicion3
        global angulo_rotacion
        angulo_rotacion = rotacion
        if t == 3:
            matriz_botones_2[fila1][columna1].configure(image=rotar_imagen_b3(1, 2))
            matriz_botones_2[fila2][columna2].configure(image=rotar_imagen_b3(2, 2))
            matriz_botones_2[fila3][columna3].configure(image=rotar_imagen_b3(3, 2))
        if t == 2:
            matriz_botones_2[fila1][columna1].configure(image=rotar_imagen_b2(1, 2))
            matriz_botones_2[fila2][columna2].configure(image=rotar_imagen_b2(2, 2))
        if t == 1:
            matriz_botones_2[fila1][columna1].configure(image=rotar_imagen(2))

def restart(x, y, j1, j2):
    iniciar_juego(x, y, j1, j2)
    verif_pos_1.clear()
    verif_pos_2.clear()
    imagenes1_1.clear()
    imagenes1_2.clear()
    imagenes2_1.clear()
    imagenes2_2.clear()
    imagenes3_1.clear()
    imagenes3_2.clear()
    barcos_jugador1.clear()
    barcos_jugador2.clear()

def rotar_barco_i():
    global angulo_rotacion
    angulo_rotacion = 180
    return angulo_rotacion

def rotar_barco_d():
    global angulo_rotacion
    angulo_rotacion = 0
    return angulo_rotacion

def rotar_barco_a():
    global angulo_rotacion
    angulo_rotacion = 90
    return angulo_rotacion

def rotar_barco_b():
    global angulo_rotacion
    angulo_rotacion = 270
    return angulo_rotacion

def mover_barcos_1():
    global angulo_rotacion, limite
    ult_posx = len(matriz_botones[0])
    ult_posy = len(matriz_botones)
    for p in barcos_jugador1:
        tipo, pos1, ang, pos2, pos3 = p
        posy1, posx1 = pos1
        posy2, posx1 = pos2
        posy3, posx3 = pos3
        if tipo == 1:
            if ang == 0:
                if posx1 != ult_posx-1:
                    limite = False
                if ((posy1, posx1+2)) not in verif_pos_1 and posx1 < ult_posx-2:
                    p[1] = [posy1, posx1+2]
                    p[3] = [posy1, posx1+2]
                    p[4] = [posy1, posx1+2]
                elif ((posy1, posx1+1)) not in verif_pos_1 and posx1 < ult_posx:
                    p[1] = [posy1, posx1+1]
                    p[3] = [posy1, posx1+1]
                    p[4] = [posy1, posx1+1]
                if posx1 == ult_posx-1:
                    limite = True
                    p[2] = 180
                    angulo_rotacion = 180
                    matriz_botones[posy1][posx1].configure(image=rotar_imagen(1))
            if ang == 180:
                if posx1 !=0:
                    limite = False
                if ((posy1, posx1-2)) not in verif_pos_1 and posx1 == ult_posx-1:
                    p[1] = [posy1, posx1-2]
                    p[3] = [posy1, posx1-2]
                    p[4] = [posy1, posx1-2]
                if ((posy1, posx1-2)) not in verif_pos_1 and posx1 > 1:
                    p[1] = [posy1, posx1-2]
                    p[3] = [posy1, posx1-2]
                    p[4] = [posy1, posx1-2]
                elif ((posy1, posx1-1)) not in verif_pos_1 and posx1 > 0:
                    p[1] = [posy1, posx1-1]
                    p[3] = [posy1, posx1-1]
                    p[4] = [posy1, posx1-1]
                if posx1 == 0:
                    limite = True
                    p[2] = 0
                    angulo_rotacion = 0
                    matriz_botones[posy1][posx1].configure(image=rotar_imagen(1))
            if ang == 90:
                if posy1 != 0:
                    limite = False
                if ((posy1-2, posx1)) not in verif_pos_1 and posy1 > 1:
                    p[1] = [posy1-2, posx1]
                    p[3] = [posy1-2, posx1]
                    p[4] = [posy1-2, posx1]
                elif ((posy1-1, posx1)) not in verif_pos_1 and posy1 > 0:
                    p[1] = [posy1-1, posx1]
                    p[3] = [posy1-1, posx1]
                    p[4] = [posy1-1, posx1]
                if posy1 == 0:
                    limite = True
                    p[2] = 270
                    angulo_rotacion = 270
                    matriz_botones[posy1][posx1].configure(image=rotar_imagen(1))
            if ang == 270:
                if posy1 != ult_posy-1:
                    limite = False
                if ((posy1+2, posx1)) not in verif_pos_1 and posy1 < ult_posy-2:
                    p[1] = [posy1+2, posx1]
                    p[3] = [posy1+2, posx1]
                    p[4] = [posy1+2, posx1]
                elif ((posy1+1, posx1)) not in verif_pos_1 and posy1 < ult_posy-1:
                    p[1] = [posy1+1, posx1]
                    p[3] = [posy1+1, posx1]
                    p[4] = [posy1+1, posx1]
                if posy1 == ult_posy-1:
                    limite = True
                    p[2] = 90
                    angulo_rotacion = 90
                    matriz_botones[posy1][posx1].configure(image=rotar_imagen(1))

def iniciar__juego(c,f,j1,j2):
    if int(c.get()) >= 20 and int(f.get()) >= 10:
        iniciar_juego(int(c.get()), int(f.get()), str(j1.get()), str(j2.get()))

def pantalla_inicio() -> tk.Tk:
    global ventana
    ventana = tk.Tk()  # Set the window state to full screen
    ventana.title("Tablero")
    ventana.configure(bg="LightBlue")

    titulo = tk.Label(text="Battleship TEC Edition", font=("Comic Sans MS", 20), bg="LightBlue")
    titulo.grid(row=0, column=0, columnspan=4, pady=10)

    c_enter = tk.Entry(ventana)
    f_enter = tk.Entry(ventana)

    boton_inicio = tk.Button(ventana, text="Iniciar Juego", font=("Comic Sans MS", 8), bg="Gray",
                             command=lambda: iniciar__juego(c_enter, f_enter, j1_enter, j2_enter))
    boton_inicio.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

    c = tk.Label(text="Cantidad de columnas:", font=("Comic Sans MS", 14), bg="LightBlue")
    c.grid(row=6, column=0, sticky="w", padx=10)
    c_enter.grid(row=6, column=1, padx=10)

    f = tk.Label(text="Cantidad de filas:", font=("Comic Sans MS", 14), bg="LightBlue")
    f.grid(row=7, column=0, sticky="w", padx=10)
    f_enter.grid(row=7, column=1, padx=10)

    btn_salir = tk.Button(ventana, text="Salir del juego", font=("Comic Sans MS", 8), bg="Gray", command=salir_juego)
    btn_salir.grid(row=4, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

    j1 = tk.Label(text="Nombre jugador 1:", font=("Comic Sans MS", 14), bg="LightBlue")
    j1.grid(row=8, column=0, sticky="w", padx=10)
    j1_enter = tk.Entry(ventana)
    j1_enter.grid(row=8, column=1, padx=10)

    j2 = tk.Label(text="Nombre jugador 2:", font=("Comic Sans MS", 14), bg="LightBlue")
    j2.grid(row=9, column=0, sticky="w", padx=10)
    j2_enter = tk.Entry(ventana)
    j2_enter.grid(row=9, column=1, padx=10)

    desc = tk.Label(text="El mejor jueguito de battleship que te vas a encontrar", font=("Comic Sans MS", 20),
                    bg="LightBlue")
    desc.grid(row=1, column=0, columnspan=4, pady=10)

    # Make the rows and columns resizable
    ventana.grid_rowconfigure(0, weight=1)
    ventana.grid_rowconfigure(2, weight=1)
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(3, weight=1)

    ventana.mainloop()

pantalla_inicio()

#2k = 40x25
#FHD = 36x17