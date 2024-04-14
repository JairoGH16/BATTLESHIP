import tkinter as tk
from PIL import ImageTk, Image

angulo_rotacion = 0
config = 1
imagenes1 = []
imagenes2 = []
imagenes3 = []
verif_pos = []

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

def ocultar_imagen(event):
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

def extra_barcos(posx, posy):
    if config == 1:
            var = 0
            for x in imagenes1:
                var+=1
            if var < 6:
                if ((posy, posx)) not in verif_pos:
                    matriz_botones[posy][posx].configure(image=rotar_imagen())
                    verif_pos.append((posy, posx))
    elif config == 2:
        var = 0
        for x in imagenes2:
            var+=1
        if var < 8:
            if angulo_rotacion == 0 and ((posy, posx)) not in verif_pos and ((posy, posx-1)) not in verif_pos:
                if posy < rows and posx > 0 and posx < columns-1:
                    matriz_botones[posy][posx].configure(image=rotar_imagen_b2(1))
                    matriz_botones[posy][posx-1].configure(image=rotar_imagen_b2(2))
                    verif_pos.append((posy, posx))
                    verif_pos.append((posy, posx-1))
            elif angulo_rotacion == 180 and ((posy, posx)) not in verif_pos and ((posy, posx+1)) not in verif_pos:
                if posx < columns-1:
                    matriz_botones[posy][posx].configure(image=rotar_imagen_b2(1))
                    matriz_botones[posy][posx+1].configure(image=rotar_imagen_b2(2))
                    verif_pos.append((posy, posx))
                    verif_pos.append((posy, posx+1))
            elif angulo_rotacion == 90 and ((posy, posx)) not in verif_pos and ((posy+1, posx)) not in verif_pos:
                if posy < rows-1:
                    matriz_botones[posy][posx].configure(image=rotar_imagen_b2(1))
                    matriz_botones[posy+1][posx].configure(image=rotar_imagen_b2(2))
                    verif_pos.append((posy, posx))
                    verif_pos.append((posy+1, posx))
            elif angulo_rotacion == 270 and ((posy, posx)) not in verif_pos and ((posy-1, posx)) not in verif_pos:
                if posy < rows:
                    matriz_botones[posy][posx].configure(image=rotar_imagen_b2(1))
                    matriz_botones[posy-1][posx].configure(image=rotar_imagen_b2(2))
                    verif_pos.append((posy, posx))
                    verif_pos.append((posy-1, posx))
    elif config == 3:
        var = 0
        for x in imagenes3:
            var+=1
        if var < 6:
            if angulo_rotacion == 0 and ((posy, posx)) not in verif_pos and ((posy, posx-1)) not in verif_pos and ((posy, posx-2)) not in verif_pos:
                if posx > 1:
                    matriz_botones[posy][posx].configure(image=rotar_imagen_b3(1))
                    matriz_botones[posy][posx-1].configure(image=rotar_imagen_b3(2))
                    matriz_botones[posy][posx-2].configure(image=rotar_imagen_b3(3))
                    verif_pos.append((posy, posx))
                    verif_pos.append((posy, posx-1))
                    verif_pos.append((posy, posx-2))
            elif angulo_rotacion == 180 and ((posy, posx)) not in verif_pos and ((posy, posx+1)) not in verif_pos and ((posy, posx+2)) not in verif_pos:
                if posx < columns-2:
                    matriz_botones[posy][posx].configure(image=rotar_imagen_b3(1))
                    matriz_botones[posy][posx+1].configure(image=rotar_imagen_b3(2))
                    matriz_botones[posy][posx+2].configure(image=rotar_imagen_b3(3))
                    verif_pos.append((posy, posx))
                    verif_pos.append((posy, posx+1))
                    verif_pos.append((posy, posx+2))
            elif angulo_rotacion == 90 and ((posy, posx)) not in verif_pos and ((posy+1, posx)) not in verif_pos and ((posy+2, posx)) not in verif_pos:
                if posy < rows-2:
                    matriz_botones[posy][posx].configure(image=rotar_imagen_b3(1))
                    matriz_botones[posy+1][posx].configure(image=rotar_imagen_b3(2))
                    matriz_botones[posy+2][posx].configure(image=rotar_imagen_b3(3))
                    verif_pos.append((posy, posx))
                    verif_pos.append((posy+1, posx))
                    verif_pos.append((posy+2, posx))
            elif angulo_rotacion == 270 and ((posy, posx)) not in verif_pos and ((posy-1, posx)) not in verif_pos and ((posy-2, posx)) not in verif_pos:
                if posy > 1:
                    matriz_botones[posy][posx].configure(image=rotar_imagen_b3(1))
                    matriz_botones[posy-1][posx].configure(image=rotar_imagen_b3(2))
                    matriz_botones[posy-2][posx].configure(image=rotar_imagen_b3(3))
                    verif_pos.append((posy, posx))
                    verif_pos.append((posy-1, posx))
                    verif_pos.append((posy-2, posx))

def rotar_imagen():
    global imagen, angulo_rotacion
    imagen_pil1 = Image.open("C:\\Users\\rafao\\Documents\\IIProyecto\\b1.png")
    imagen_rotada1 = imagen_pil1.rotate(angulo_rotacion, expand=True)
    imagen_rotada1 = imagen_rotada1.resize((50, 50))
    global imagen1
    imagen1 = ImageTk.PhotoImage(imagen_rotada1)
    imagenes1.append(imagen1)
    return imagen1

def rotar_imagen_b2(num):
    imagen_pil = Image.open(f"C:\\Users\\rafao\\Documents\\IIProyecto\\b2{num}.png")
    imagen_rotada = imagen_pil.rotate(angulo_rotacion, expand=True)
    imagen_rotada = imagen_rotada.resize((50, 50))
    global imagen2
    imagen2 = ImageTk.PhotoImage(imagen_rotada)
    imagenes2.append(imagen2)
    return imagen2

def rotar_imagen_b3(num):
    imagen_pil = Image.open(f"C:\\Users\\rafao\\Documents\\IIProyecto\\b3{num}.png")
    imagen_rotada = imagen_pil.rotate(angulo_rotacion, expand=True)
    imagen_rotada = imagen_rotada.resize((50, 50))
    global imagen3
    imagen3 = ImageTk.PhotoImage(imagen_rotada)
    imagenes3.append(imagen3)
    return imagen3

def iniciar_juego(x, y):
    global rows, columns
    rows = y
    columns = x
    for widget in ventana.winfo_children():
        widget.destroy()  # Limpiar la ventana
    ventana.state("zoomed")
    ventana.title("Tablero")

    # Cargar la rotar_imagen_b2(2) que deseas mostrar con Pillow
    global matriz_botones
    matriz_botones = [[tk.Button(ventana, command=lambda posx=c,posyy=f:extra_barcos(posx,posyy), bg="Blue") for c in range(x)] for f in range(y)]
    posy = 50
    for fila_botones in matriz_botones:
        posx=1920/2
        for boton in fila_botones:
            if posx == 1485:
                print("iadshvofa")
            boton.place(x=posx, y=posy, height=50, width=50)
            boton.bind("<Leave>", ocultar_imagen)
            boton.bind("<Enter>", mostrar_imagen)  # Vincular la función obtener_coordenadas al evento <Enter>
            posx += 50  # Mover posición x para el próximo botón
        posy += 50  # Mover posición y para la próxima fila

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

    config1.configure(text="1 Barco", command= lambda: cambiar_config(1))
    config2.configure(text="2 Barcos", command=lambda: cambiar_config(2))
    config3.configure(text="3 Barcos", command=lambda: cambiar_config(3))

def rotar_barco_i():
    global angulo_rotacion
    angulo_rotacion = 180

def rotar_barco_d():
    global angulo_rotacion
    angulo_rotacion = 0

def rotar_barco_a():
    global angulo_rotacion
    angulo_rotacion = 90

def rotar_barco_b():
    global angulo_rotacion
    angulo_rotacion = 270

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
                             command=lambda: iniciar_juego(int(c_enter.get()), int(f_enter.get())))
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