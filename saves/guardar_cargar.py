import turnos as tur
import logica.vidas as vidas
import var_imagenes as imagenes

def guardar_juego(mar1,mar2):
    nombre_archivo=input("Ponle un nombre a tu archivo, se sobreescribirá si ya existe")
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
        archivo.write(str(imagenes.imagenes1_1)+"\n")
        archivo.write(str(imagenes.imagenes1_2)+"\n")
        archivo.write(str(imagenes.imagenes2_1)+"\n")
        archivo.write(str(imagenes.imagenes2_2)+"\n")
        archivo.write(str(imagenes.imagenes3_1)+"\n")
        archivo.write(str(imagenes.imagenes3_2)+"\n")
        archivo.write(str(imagenes.verif_pos_1)+"\n")
        archivo.write(str(imagenes.verif_pos_2)+"\n")

def cargar_mar(nombre_archivo):
    try:
        archivo=open(nombre_archivo, "tr")
    except:
        print("no hay archivo")
    with open(nombre_archivo, "tr") as archivo:
        lineas=archivo.readlines()
        mar1=lineas[7]
        mar1=eval(mar1)
        mar2=lineas[8]
        mar2=eval(mar2)
        return(mar1,mar2)

def cargar_otros(nombre_archivo):
    try:
        archivo=open(nombre_archivo, "tr")
    except:
        print("no hay archivo")
    with open("sss.txt", "tr") as archivo:
        lineas=archivo.readlines()
        tur.mi=lineas[0][:-1]
        tur.nj=lineas[1][:-1]
        tur.fnl=lineas[2][:-1]
        tur.fase_barcos_1=lineas[3][:-1]
        tur.fase_barcos_2=lineas[4][:-1]
        tur.turno=lineas[5][:-1]
        tur.ataque_posible=lineas[6][:-1]
        vidas.nombre_j1=lineas[9][:-1]
        vidas.nombre_j2=lineas[10][:-1]
        vidas.vidas_jugador1=lineas[11][:-1]
        vidas.vidas_jugador1=lineas[12][:-1]

