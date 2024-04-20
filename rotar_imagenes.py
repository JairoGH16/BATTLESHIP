from PIL import Image, ImageTk
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def rotar_imagen(verif, angulo_rotacion, imagenes1_1, imagenes1_2):
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