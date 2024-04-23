import tkinter as tk
nombre_j1=""
nombre_j2=""

vidas_jugador1={"barcos_pequenos":6,
                "barcos_medianos":4,
                "barcos_grandes":2}
vidas_jugador2={"barcos_pequenos":6,
                "barcos_medianos":4,
                "barcos_grandes":2}

def quitar_vidas(jugador:int,tipo_barco:str):
    if jugador==1:
        vidas_jugador1[tipo_barco]-=1
    if jugador==2:
        vidas_jugador2[tipo_barco]-=1
    if vidas_jugador1["barcos_pequenos"]==0 and vidas_jugador1["barcos_medianos"]==0 and vidas_jugador1["barcos_grandes"]==0:
        anunciar_ganador(nombre_j2)
    if vidas_jugador2["barcos_pequenos"]==0 and vidas_jugador2["barcos_medianos"]==0 and vidas_jugador2["barcos_grandes"]==0:
        
        
        
        
        anunciar_ganador(nombre_j1)

def anunciar_ganador(jugador):
    ventana = tk.Tk()
    label = tk.Label(ventana, text=f"El ganador de esta partida es {jugador}",font=("ComicSansMS",25),bg="#8e582c",fg="#ffedba")
    ventana.title("Ganador")
    label.grid()
    ventana.mainloop()