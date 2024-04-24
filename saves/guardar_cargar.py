import turnos as tur
import logica.vidas as vidas
import var_imagenes as imagenes

def guardar_juego(mar1:list,mar2:list, nombre_archivo:str):
    """guarda los datos del juego

    Args:
        mar1 (list): mar1
        mar2 (list): mar2
        nombre_archivo (str): nombre del archivo
    """
    if not nombre_archivo.endswith(".txt"):
        nombre_archivo = nombre_archivo+".txt"
    nombre_archivo=nombre_archivo.replace("/","_").replace("\\","_").replace(":","_").replace(" ","_")
    with open(nombre_archivo, "tw") as archivo:
        archivo.write(str(tur.mi)+"\n")
        archivo.write(str(tur.nj)+"\n")
        archivo.write(str(tur.fnl)+"\n")
        archivo.write(str(tur.fase_barcos_1)+"\n")
        archivo.write(str(tur.fase_barcos_2)+"\n")
        archivo.write(str(tur.turno)+"\n")
        archivo.write(str(tur.ataque_posible)+"\n")
        archivo.write(str(mar1)+"\n")
        archivo.write(str(mar2)+"\n")
        archivo.write(vidas.nombre_j1+"\n")
        archivo.write(vidas.nombre_j2+"\n")
        archivo.write(str(vidas.vidas_jugador1)+"\n")
        archivo.write(str(vidas.vidas_jugador2)+"\n")
        archivo.write(str(imagenes.angulo_rotacion)+"\n")
        archivo.write(str(imagenes.barcos1_1)+"\n")
        archivo.write(str(imagenes.barcos1_2)+"\n")
        archivo.write(str(imagenes.barcos2_1)+"\n")
        archivo.write(str(imagenes.barcos2_2)+"\n")
        archivo.write(str(imagenes.barcos3_1)+"\n")
        archivo.write(str(imagenes.barcos3_2)+"\n")
        archivo.write(str(imagenes.verif_pos_1)+"\n")
        archivo.write(str(imagenes.verif_pos_2)+"\n")
        archivo.write(str(vidas.ultimo_intento)+"\n")
        archivo.write(str(vidas.puntuacion_j1)+"\n")
        archivo.write(str(vidas.puntuacion_j2)+"\n")

def cargar_mar(nombre_archivo:str):
    """carga las matrices del mar

    Args:
        nombre_archivo (str): nombre del archivo
    """
    try:
        with open(f"{nombre_archivo}"+".txt", "tr") as archivo:
            lineas=archivo.readlines()
            mar1=lineas[7]
            mar1=eval(mar1)
            mar2=lineas[8]
            mar2=eval(mar2)
            return(mar1,mar2)
    except:
        print("no hay achivo con ese nombre")

def cargar_otros(nombre_archivo:str):
    """carga el resto de datos

    Args:
        nombre_archivo (str): el nombre del archivo
    """
    try:
        with open(f"{nombre_archivo}"+".txt", "tr") as archivo:
            lineas=archivo.readlines()
            tur.mi=eval(lineas[0][:-1])
            tur.nj=eval(lineas[1][:-1])
            tur.fnl=eval(lineas[2][:-1])
            tur.fase_barcos_1=eval(lineas[3][:-1])
            tur.fase_barcos_2=eval(lineas[4][:-1])
            tur.turno=eval(lineas[5][:-1])
            tur.ataque_posible=eval(lineas[6][:-1])
            vidas.nombre_j1=(lineas[9][:-1])
            print(vidas.nombre_j1)
            vidas.nombre_j2=(lineas[10][:-1])
            vidas.vidas_jugador1=eval(lineas[11][:-1])
            vidas.vidas_jugador2=eval(lineas[12][:-1])
            imagenes.angulo_rotacion=(lineas[13:-1])
            imagenes.verif_pos_1=eval(lineas[14][:-1])
            imagenes.verif_pos_2=eval(lineas[15][:-1])
            vidas.ultimo_intento=eval(lineas[16][:-1])
            vidas.puntuacion_j1=eval(lineas[17][:-1])
            vidas.puntuacion_j1=eval(lineas[18][:-1])

    except:
        print("no hay archivo con ese nombre")
        print("no hay archivo")
    with open(f"{nombre_archivo}"+".txt", "tr") as archivo:
        lineas=archivo.readlines()
        tur.mi=eval(lineas[0][:-1])
        tur.nj=eval(lineas[1][:-1])
        tur.fnl=eval(lineas[2][:-1])
        tur.fase_barcos_1=eval(lineas[3][:-1])
        tur.fase_barcos_2=eval(lineas[4][:-1])
        tur.turno=eval(lineas[5][:-1])
        tur.ataque_posible=eval(lineas[6][:-1])
        vidas.nombre_j1=(lineas[9][:-1])
        vidas.nombre_j2=(lineas[10][:-1])
        vidas.vidas_jugador1=(lineas[11][:-1])
        vidas.vidas_jugador1=(lineas[12][:-1])
        imagenes.barcos1_1=eval(lineas[14][:-1])
        imagenes.barcos1_2=eval(lineas[15][:-1])
        imagenes.barcos2_1=eval(lineas[16][:-1])
        imagenes.barcos2_2=eval(lineas[17][:-1])
        imagenes.barcos3_1=eval(lineas[18][:-1])
        imagenes.barcos3_2=eval(lineas[19][:-1])
        imagenes.verif_pos_1=eval(lineas[20][:-1])
        imagenes.verif_pos_2=eval(lineas[21][:-1])