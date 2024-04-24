import tkinter as tk
from PIL import ImageTk, Image
import os
import logica.movimiento as mov
import turnos as tur
import rotar_imagenes as rot
import var_imagenes as im
import logica.insertar as insert
import logica.logica_botones as botones
import logica.vidas as vidas
import saves.guardar_cargar as saves

config = 1
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
    if tur.mi == True and tur.fase_barcos_1 == True:
        boton = event.widget
        for f in range(len(matriz_botones)):
            for c in range(len(matriz_botones[f])):
                if matriz_botones[f][c] == boton:
                    if config == 1:
                        boton.configure(bg="Green")
                    try:
                        if config == 2 and im.angulo_rotacion == 0:
                            if c > 0:
                                boton.configure(bg="Green")
                                matriz_botones[f][c-1].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 2 and im.angulo_rotacion == 270:
                            if f > 0:
                                boton.configure(bg="Green")
                                matriz_botones[f-1][c].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 2 and im.angulo_rotacion == 180:
                            if c < columns:
                                boton.configure(bg="Green")
                                matriz_botones[f][c+1].configure(bg="Green")
                            if c == columns:
                                boton.configure(bg="Red")
                        elif config == 2 and im.angulo_rotacion == 90:
                            if f < rows:
                                boton.configure(bg="Green")
                                matriz_botones[f+1][c].configure(bg="Green")
                    except IndexError:
                        boton.configure(bg="Red")
                    try:
                        if config == 3 and im.angulo_rotacion == 0:
                            if c > 1:
                                boton.configure(bg="Green")
                                matriz_botones[f][c-1].configure(bg="Green")
                                matriz_botones[f][c-2].configure(bg="Green")
                            elif c > 0:
                                boton.configure(bg="Red")
                                matriz_botones[f][c-1].configure(bg="Red")
                            elif c == 0:
                                boton.configure(bg="Red")
                        elif config == 3 and im.angulo_rotacion == 270:
                            if f > 1:
                                boton.configure(bg="Green")
                                matriz_botones[f-1][c].configure(bg="Green")
                                matriz_botones[f-2][c].configure(bg="Green")
                            elif f == 1:
                                boton.configure(bg="Red")
                                matriz_botones[f-1][c].configure(bg="Red")
                            elif f == 0:
                                boton.configure(bg="Red")
                        elif config == 3 and im.angulo_rotacion == 180:
                            if c < columns-1:
                                boton.configure(bg="Green")
                                matriz_botones[f][c+1].configure(bg="Green")
                                matriz_botones[f][c+2].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 3 and im.angulo_rotacion == 90:
                            if f < rows-1:
                                boton.configure(bg="Green")
                                matriz_botones[f+1][c].configure(bg="Green")
                                matriz_botones[f+2][c].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                                matriz_botones[f+1][c].configure(bg="Red")
                    except IndexError:
                        boton.configure(bg="Red")
                        if im.angulo_rotacion == 180:
                            boton.configure(bg="Red")
                            matriz_botones[f][c+1].configure(bg="Red")
                        if im.angulo_rotacion == 270:
                            boton.configure(bg="Red")
                            matriz_botones[f+1][c].configure(bg="Red")
                        if im.angulo_rotacion == 90:
                            boton.configure(bg="Red")
                            matriz_botones[f+1][c].configure(bg="Red")
                        break

def mostrar_imagen_2(event):
    if tur.mi == False and tur.fase_barcos_2 == True:
        boton = event.widget
        for f in range(len(matriz_botones_2)):
            for c in range(len(matriz_botones_2[f])):
                if matriz_botones_2[f][c] == boton:
                    if config == 1:
                        boton.configure(bg="Green")
                    try:
                        if config == 2 and im.angulo_rotacion == 0:
                            if c > 0:
                                boton.configure(bg="Green")
                                matriz_botones_2[f][c-1].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 2 and im.angulo_rotacion == 270:
                            if f > 0:
                                boton.configure(bg="Green")
                                matriz_botones_2[f-1][c].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 2 and im.angulo_rotacion == 180:
                            if c < columns:
                                boton.configure(bg="Green")
                                matriz_botones_2[f][c+1].configure(bg="Green")
                            if c == columns:
                                boton.configure(bg="Red")
                        elif config == 2 and im.angulo_rotacion == 90:
                            if f < rows:
                                boton.configure(bg="Green")
                                matriz_botones_2[f+1][c].configure(bg="Green")
                    except IndexError:
                        boton.configure(bg="Red")
                    try:
                        if config == 3 and im.angulo_rotacion == 0:
                            if c > 1:
                                boton.configure(bg="Green")
                                matriz_botones_2[f][c-1].configure(bg="Green")
                                matriz_botones_2[f][c-2].configure(bg="Green")
                            elif c > 0:
                                boton.configure(bg="Red")
                                matriz_botones_2[f][c-1].configure(bg="Red")
                            elif c == 0:
                                boton.configure(bg="Red")
                        elif config == 3 and im.angulo_rotacion == 270:
                            if f > 1:
                                boton.configure(bg="Green")
                                matriz_botones_2[f-1][c].configure(bg="Green")
                                matriz_botones_2[f-2][c].configure(bg="Green")
                            elif f == 1:
                                boton.configure(bg="Red")
                                matriz_botones_2[f-1][c].configure(bg="Red")
                            elif f == 0:
                                boton.configure(bg="Red")
                        elif config == 3 and im.angulo_rotacion == 180:
                            if c < columns-1:
                                boton.configure(bg="Green")
                                matriz_botones_2[f][c+1].configure(bg="Green")
                                matriz_botones_2[f][c+2].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                        elif config == 3 and im.angulo_rotacion == 90:
                            if f < rows-1:
                                boton.configure(bg="Green")
                                matriz_botones_2[f+1][c].configure(bg="Green")
                                matriz_botones_2[f+2][c].configure(bg="Green")
                            else:
                                boton.configure(bg="Red")
                                matriz_botones_2[f+1][c].configure(bg="Red")
                    except IndexError:
                        boton.configure(bg="Red")
                        if im.angulo_rotacion == 180:
                            boton.configure(bg="Red")
                            matriz_botones_2[f][c+1].configure(bg="Red")
                        if im.angulo_rotacion == 270:
                            boton.configure(bg="Red")
                            matriz_botones_2[f+1][c].configure(bg="Red")
                        if im.angulo_rotacion == 90:
                            boton.configure(bg="Red")
                            matriz_botones_2[f+1][c].configure(bg="Red")
                        break

def ocultar_imagen(event):
    if tur.mi == True and tur.fase_barcos_1 == True:
        boton = event.widget
        for f in range(len(matriz_botones)):
            for c in range(len(matriz_botones[f])):
                if matriz_botones[f][c] == boton:
                    boton.configure(bg="#7EC0EE")
                    if config == 2 and im.angulo_rotacion == 0:
                        if c > 0:
                            matriz_botones[f][c-1].configure(bg="#7EC0EE")
                    elif config == 2 and im.angulo_rotacion == 270:
                        matriz_botones[f-1][c].configure(bg="#7EC0EE")
                    elif config == 2 and im.angulo_rotacion == 180:
                        matriz_botones[f][c+1].configure(bg="#7EC0EE")
                    elif config == 2 and im.angulo_rotacion == 90:
                        matriz_botones[f+1][c].configure(bg="#7EC0EE")
                    if config == 3 and im.angulo_rotacion == 0:
                        matriz_botones[f][c-1].configure(bg="#7EC0EE")
                        matriz_botones[f][c-2].configure(bg="#7EC0EE")
                    elif config == 3 and im.angulo_rotacion == 270:
                        matriz_botones[f-1][c].configure(bg="#7EC0EE")
                        matriz_botones[f-2][c].configure(bg="#7EC0EE")
                    elif config == 3 and im.angulo_rotacion == 180:
                        matriz_botones[f][c+1].configure(bg="#7EC0EE")
                        matriz_botones[f][c+2].configure(bg="#7EC0EE")
                    elif config == 3 and im.angulo_rotacion == 90:
                        matriz_botones[f+1][c].configure(bg="#7EC0EE")
                        matriz_botones[f+2][c].configure(bg="#7EC0EE")
                    break

def ocultar_imagen_2(event):
    if tur.mi == False and tur.fase_barcos_2 == True:
        boton = event.widget
        for f in range(len(matriz_botones_2)):
            for c in range(len(matriz_botones_2[f])):
                if matriz_botones_2[f][c] == boton:
                    boton.configure(bg="#7EC0EE")
                    if config == 2 and im.angulo_rotacion == 0:
                        if c > 0:
                            matriz_botones_2[f][c-1].configure(bg="#7EC0EE")
                    elif config == 2 and im.angulo_rotacion == 270:
                        matriz_botones_2[f-1][c].configure(bg="#7EC0EE")
                    elif config == 2 and im.angulo_rotacion == 180:
                        matriz_botones_2[f][c+1].configure(bg="#7EC0EE")
                    elif config == 2 and im.angulo_rotacion == 90:
                        matriz_botones_2[f+1][c].configure(bg="#7EC0EE")
                    if config == 3 and im.angulo_rotacion == 0:
                        matriz_botones_2[f][c-1].configure(bg="#7EC0EE")
                        matriz_botones_2[f][c-2].configure(bg="#7EC0EE")
                    elif config == 3 and im.angulo_rotacion == 270:
                        matriz_botones_2[f-1][c].configure(bg="#7EC0EE")
                        matriz_botones_2[f-2][c].configure(bg="#7EC0EE")
                    elif config == 3 and im.angulo_rotacion == 180:
                        matriz_botones_2[f][c+1].configure(bg="#7EC0EE")
                        matriz_botones_2[f][c+2].configure(bg="#7EC0EE")
                    elif config == 3 and im.angulo_rotacion == 90:
                        matriz_botones_2[f+1][c].configure(bg="#7EC0EE")
                        matriz_botones_2[f+2][c].configure(bg="#7EC0EE")
                    break

mar1=[]
mar2=[]

def mandar_guardar():
    ar = tk.Tk()
    label = tk.Label(ar, text="Ingrese el nombre del archivo")
    label.grid(row=0, column=0) 
    entry_arch = tk.Entry(ar)
    entry_arch.grid(row=1, column=0)

    aceptar = tk.Button(ar, text="Aceptar")
    aceptar.grid(row=2, column=0)

    def get_name():
        nombre_archivo = entry_arch.get() 
        saves.guardar_juego(mar1, mar2, nombre_archivo)
        ar.destroy()

    aceptar.config(command=get_name)

    ar.mainloop()

def iniciar_juego(x, y, j1, j2,carga,nombre_archivo):
    vidas.nombre_j1=j1
    vidas.nombre_j2=j2
    global mar1,mar2
    if carga==False:
        mar1.extend([[{"direccion":"","pieza":".","caminando":True,"danado":False} for c in range(int(x/2))]for f in range(y)])
        mar2.extend([[{"direccion":"","pieza":".","caminando":True,"danado":False} for c in range(int(x/2))]for f in range(y)])
    else:
        mar1,mar2=saves.cargar_mar(f"{nombre_archivo}")

    global rows, columns, Jug1, Jug2
    rows = y
    columns = x
    for widget in ventana.winfo_children():
        widget.destroy()  # Limpiar la ventana
    ventana.state("zoomed")
    ventana.title("Tablero")

    guardar=tk.Button(ventana, text="Guardar", command=mandar_guardar, height=5,width=7)
    guardar.place(x=0,y=0)

    global matriz_botones, matriz_botones_2
    matriz_botones = [[tk.Button(ventana, borderwidth=2, bg="""#7EC0EE""", command=lambda posx=c, posy=f: botones.accion_boton(posx,posy,config,columns,rows,matriz_botones,matriz_botones_2,1,mar1,mar2)) for c in range(x // 2)] for f in range(y)]

    # Crear una segunda matriz de botones
    matriz_botones_2 = [[tk.Button(ventana, borderwidth=2, bg="""#7EC0EE""", command=lambda posx=c, posy=f: botones.accion_boton(posx,posy,config,columns,rows,matriz_botones_2,matriz_botones,2,mar1,mar2)) for c in range(x - x // 2)] for f in range(y)]

    # Calcular las posiciones x e y para centrar las matrices
    ancho_ventana = ventana.winfo_screenwidth()
    posx_matriz1 = (ancho_ventana//2)-(x*50//2)-20
    posy_matriz1 = 50
    posx_matriz2 = (ancho_ventana//2)+20
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

    config1.configure(text="Destructor", command=lambda: cambiar_config(1))
    config2.configure(text="Crucero", command=lambda: cambiar_config(2))
    config3.configure(text="Acorazado", command=lambda: cambiar_config(3))

    reiniciar = tk.Button(ventana)
    reiniciar.place(x=x*25+100,y=y*50+110)
    reiniciar.configure(command=lambda: restart(ventana), text="Reiniciar")

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
    nj.configure(text="Siguiente", command= lambda: tur.next_pj(matriz_botones,matriz_botones_2,mar1,mar2,pts_j1,pts_j2))

    if tur.turno==1 and tur.visible==True:
        tur.rest_barcos(matriz_botones,mar1)
    if tur.turno==2 and tur.visible==True:
        tur.rest_barcos(matriz_botones_2,mar2)

    pts_j1 = tk.Label(ventana, text=im.ptsj1, bg = "LightBlue", font=("Comic Sans MS", 20))
    pts_j1.place(x=(ancho_ventana//2-50), y=0)
    pts_j2 = tk.Label(ventana, text=im.ptsj2, bg = "LightBlue", font=("Comic Sans MS", 20))
    pts_j2.place(x=(ancho_ventana//2+50), y=0)

def restart(ventana):
    ventana.destroy()
    pantalla_inicio()

def rotar_barco_i():
    im.angulo_rotacion = 180
    return im.angulo_rotacion

def rotar_barco_d():
    im.angulo_rotacion = 0
    return im.angulo_rotacion

def rotar_barco_a():
    im.angulo_rotacion = 90
    return im.angulo_rotacion

def rotar_barco_b():
    im.angulo_rotacion = 270
    return im.angulo_rotacion

def validar_inicio(c,f,j1,j2,nj1,nj2,carga):
    if carga == True:
            ar = tk.Tk()
            label = tk.Label(ar, text="Ingrese el nombre del archivo a cargar: ")
            label.grid(row=0, column=0) 
            entry_arch = tk.Entry(ar)
            entry_arch.grid(row=1, column=0)
            aceptar = tk.Button(ar, text="Aceptar")
            aceptar.grid(row=2, column=0)
            def get_name():
                nombre_archivo = entry_arch.get() 
                saves.cargar_otros(f"{nombre_archivo}")
                mar1,mar2=saves.cargar_mar(f"{nombre_archivo}")
                iniciar_juego(len(mar1[0])*2,len(mar1),vidas.nombre_j1,vidas.nombre_j2,carga,nombre_archivo)
                ar.destroy()
            aceptar.config(command=get_name)
            ar.mainloop()

    elif int(c.get()) >= 20 and int(f.get()) >= 10 and int(c.get())%2 == 0 and str(j1.get()) != "" and str(j2.get()) != "" and str(j1.get()) != str(j2.get()) and str(nj1.get()) != "" and str(nj2.get()) != "" and str(nj1.get()) != str(nj2.get()):
        iniciar_juego(int(c.get()), int(f.get()), str(j1.get()), str(j2.get()),carga,"")

def pantalla_inicio() -> tk.Tk:
    global ventana
    ventana = tk.Tk()
    ventana.attributes("-fullscreen",True)
    ventana.title("Tablero")
    ventana.configure(bg="LightBlue")

    titulo = tk.Label(text="Battleship TEC Edition", font=("Comic Sans MS", 60), bg="LightBlue")
    titulo.grid(row=0, column=0, columnspan=4, pady=10)

    c_enter = tk.Entry(ventana)
    f_enter = tk.Entry(ventana)

    boton_carga = tk.Button(ventana, text="Cargar Juego", font=("Comic Sans MS", 26), bg="Gray",
                             command=lambda: validar_inicio(c_enter, f_enter, j1_enter, j2_enter,nj1_enter,nj2_enter,True))
    boton_carga.grid(row=4, column=0, columnspan=4, pady=10, padx=10)

    boton_inicio = tk.Button(ventana, text="Iniciar Juego", font=("Comic Sans MS", 26), bg="Gray",
                             command=lambda: validar_inicio(c_enter, f_enter, j1_enter, j2_enter,nj1_enter,nj2_enter,False))
    boton_inicio.grid(row=3, column=0, columnspan=4, pady=10, padx=10)

    c = tk.Label(text="Cantidad de columnas:", font=("Comic Sans MS", 20), bg="LightBlue")
    c.grid(row=6, column=0, sticky="w", padx=10)
    c_enter.grid(row=6, column=0, ipadx=100)

    f = tk.Label(text="Cantidad de filas:", font=("Comic Sans MS", 20), bg="LightBlue")
    f.grid(row=7, column=0, sticky="w", padx=10)
    f_enter.grid(row=7, column=0, ipadx=100)

    btn_salir = tk.Button(ventana, text="Salir del juego", font=("Comic Sans MS", 26), bg="Gray", command=salir_juego)
    btn_salir.grid(row=5, column=0, columnspan=4, pady=10, padx=10)

    j1 = tk.Label(text="Nombre jugador 1:", font=("Comic Sans MS", 20), bg="LightBlue")
    j1.grid(row=8, column=0, sticky="w", padx=10)
    j1_enter = tk.Entry(ventana)
    j1_enter.grid(row=8, column=0, ipadx=100)

    nj1 = tk.Label(text="Nickname J1:", font=("Comic Sans MS", 20), bg="LightBlue")
    nj1.grid(row=9, column=0, sticky="w", padx=10)
    nj1_enter = tk.Entry(ventana)
    nj1_enter.grid(row=9, column=0, ipadx= 100)

    j2 = tk.Label(text="Nombre jugador 2:", font=("Comic Sans MS", 20), bg="LightBlue")
    j2.grid(row=10, column=0, sticky="w", padx=10)
    j2_enter = tk.Entry(ventana)
    j2_enter.grid(row=10, column=0, ipadx=100)

    nj2 = tk.Label(text="Nickname J2:", font=("Comic Sans MS", 20), bg="LightBlue")
    nj2.grid(row=11, column=0, sticky="w", padx=10)
    nj2_enter = tk.Entry(ventana)
    nj2_enter.grid(row=11, column=0, ipadx=100)

    desc = tk.Label(text="""BattleShip es un juego de estrategia basado en destruir la flota enemiga adivinando sus posiciones, gana el primero en derribar todas las embarcaciones enemigas\n\n
                    Instrucciones de uso:\n
                    -Minimo de columnas: 20(debe ser una cantidad par)\n
                    -Minimo de filas: 10\n
                    -Los nombres y nicknames de cada jugador deben ser distintos entre si, y no deben estar vacios\n
                    -Se deben colocar todos los barcos para pasar al siguiente jugador en la fase de barcos""", font=("Comic Sans MS", 20),
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