from PIL import Image, ImageTk
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def rotar_imagen(verif, angulo_rotacion, imagenes1_1, imagenes1_2):
    """Esta funcion se encarga de cambiar la rotacion de la imagen para el barco de una casilla

    Args:
        verif (_type_): Matriz donde se va a trabajar
        angulo_rotacion (_type_): Angulo que se aplicara a la imagen
        imagenes1_1 (_type_): Lista con las imagenes creadas de la matriz 1
        imagenes1_2 (_type_): Lista con las imagenes creadas de la matriz 2

    Returns:
        _type_: Imagen rotada segun el angulo de rotacion proporcionado

    Autor: Rafael Odio
    """
    global imagen
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

def rotar_imagen_b2(num, verif, angulo_rotacion, imagenes2_1, imagenes2_2):
    """Esta funcion se encarga de cambiar la rotacion de las imagenes para el barco de dos casillas

    Args:
        verif (_type_): Matriz donde se va a trabajar
        angulo_rotacion (_type_): Angulo que se aplicara a la imagen
        imagenes2_1 (_type_): Lista con las imagenes creadas de la matriz 1
        imagenes2_2 (_type_): Lista con las imagenes creadas de la matriz 2

    Returns:
        _type_: Imagenes rotadas segun el angulo de rotacion proporcionado

    Autor: Rafael Odio
    """
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

def rotar_imagen_b3(num, verif, angulo_rotacion, imagenes3_1, imagenes3_2):
    """Esta funcion se encarga de cambiar la rotacion de las imagenes para el barco de tres casillas

    Args:
        verif (_type_): Matriz donde se va a trabajar
        angulo_rotacion (_type_): Angulo que se aplicara a la imagen
        imagenes3_1 (_type_): Lista con las imagenes creadas de la matriz 1
        imagenes3_2 (_type_): Lista con las imagenes creadas de la matriz 2

    Returns:
        _type_: Imagenes rotadas segun el angulo de rotacion proporcionado

    Autor: Rafael Odio
    """
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
