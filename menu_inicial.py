import tkinter as tk
from PIL import ImageTk, Image

angulo_rotacion = 0

def salir_juego():
    exit()

def mostrar_imagen(event):
    boton = event.widget
    boton.config(image=imagen)
    boton.image = imagen  # Mantener una referencia a la imagen

def accion(event):
    boton = event.widget
    boton.unbind("<Leave>")  # Desvinculamos el evento <Leave>

def ocultar_imagen(event):
    boton = event.widget
    if boton.winfo_viewable():
        boton.config(image="")

def actualizar_botones(matriz_botones):
    for fila in matriz_botones:
        for boton in fila:
            if boton.image == imagen:
                pass
            else:
                boton.config(image=imagen)
                boton.image = imagen
                boton.config(image="")

def rotar_imagen():
    global imagen, angulo_rotacion
    imagen_pil = Image.open("C:\\Users\\rafao\\Downloads\\png-transparent-boating-boat-top-artwork-boat-boating.png")
    imagen_rotada = imagen_pil.rotate(angulo_rotacion, expand=True)
    imagen_rotada = imagen_rotada.resize((50, 50))
    imagen = ImageTk.PhotoImage(imagen_rotada)
    return imagen


def iniciar_juego(x, y):
    for widget in ventana.winfo_children():
        widget.destroy()  # Limpiar la ventana

    ventana.geometry(f"{x*50}x{y*50+500}+0+0")
    ventana.title("Tablero")

    # Cargar la imagen que deseas mostrar con Pillow
    imagen = rotar_imagen()
    global matriz_botones
    matriz_botones = [[tk.Button(ventana) for c in range(x)] for f in range(y)]
    posx = 0
    posy = 0
    for fila_botones in matriz_botones:
        posx=0
        for boton in fila_botones:
            boton.place(x=posx, y=posy, height=imagen.height(), width=imagen.width())
            boton.bind("<Enter>", mostrar_imagen)
            boton.bind("<Button-1>", accion)
            boton.bind("<Leave>", ocultar_imagen)

            posx += imagen.width()  # Mover posición x para el próximo botón
        posx = 0
        posy += imagen.height()  # Mover posición y para la próxima fila

    rot_derecha = tk.Button(ventana, command=rotar_botones_d)
    rot_derecha.place(x=x*30,y=y*50+250)
    rot_derecha.configure(text="Pos Derecha",font=("",14))

    rot_izquierda = tk.Button(ventana, command=rotar_botones_i)
    rot_izquierda.place(x=x*10,y=y*50+250)
    rot_izquierda.configure(text="Pos Izquierda",font=("",14))

def rotar_botones_i():
    global angulo_rotacion
    angulo_rotacion = (angulo_rotacion + 90) % 360
    imagen = rotar_imagen()
    actualizar_botones(matriz_botones)

def rotar_botones_d():
    global angulo_rotacion
    angulo_rotacion = (angulo_rotacion - 90) % 360
    imagen = rotar_imagen()
    actualizar_botones(matriz_botones)

def pantalla_inicio(x: int, y: int) -> tk.Tk:
    global ventana
    ventana = tk.Tk()
    ventana.geometry(f"{x*70}x{y*70}+0+0")
    ventana.title("Tablero")
    ventana.configure(bg="LightBlue")

    titulo = tk.Label(text="Battleship TEC Edition", font=("ComicSans",20), bg="LightBlue")
    titulo.place(x=x*25,y=5)

    c_enter = tk.Entry(ventana)
    f_enter = tk.Entry(ventana)

    boton_inicio = tk.Button(ventana)
    boton_inicio.place(x=x*35, y=y*24)
    boton_inicio.configure(width=30, height=5, text="Iniciar Juego", bg="Gray", command= lambda: iniciar_juego(int(c_enter.get()),int(f_enter.get())))

    c = tk.Label(text="Cantidad de columnas:",font=("ComicSans",14), bg="LightBlue")
    c.place(x=x*10,y=y*38)
    c_enter.place(x=x*20,y=y*38)
    c_enter.configure(font=("ComicSans",14))

    f = tk.Label(text="Cantidad de filas:",font=("ComicSans",14), bg="LightBlue")
    f.place(x=x*10,y=y*34)
    f_enter.place(x=x*18,y=y*34)
    f_enter.configure(font=("ComicSans",14))

    btn_salir = tk.Button(ventana)
    btn_salir.place(x=x*35, y=y*33)
    btn_salir.configure(width=30, height=5, text="Salir del juego", bg="Gray", command=salir_juego)

    j1 = tk.Label(text="Nombre jugador 1:", font=("ComicSans",14), bg="LightBlue")
    j1.place(x=x*10,y=y*26)
    j1_enter = tk.Entry(ventana)
    j1_enter.place(x=x*18,y=y*26)
    j1_enter.configure(font=("ComicSans",14))

    j2 = tk.Label(text="Nombre jugador 2:", font=("ComicSans",14), bg="LightBlue")
    j2.place(x=x*10,y=y*30)
    j2_enter = tk.Entry(ventana)
    j2_enter.place(x=x*18,y=y*30)
    j2_enter.configure(font=("ComicSans",14))

    desc = tk.Label(text="El mejor jueguito de battleship que te vas a encontrar",font=("ComicSans",20), bg="LightBlue")
    desc.place(x=x*15,y=y*10)

    ventana.mainloop()

pantalla_inicio(20,10)