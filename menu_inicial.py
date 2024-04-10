import tkinter as tk

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
    boton_inicio.configure(width=30, height=5, text="Iniciar Juego", bg="Gray")

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
    btn_salir.configure(width=30, height=5, text="Salir del juego", bg="Gray")

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