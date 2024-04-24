import tkinter as tk
import var_imagenes as im
puntuacion_j1=0
puntuacion_j2=0
nombre_j1=""
nombre_j2=""
ultimo_intento=[False,False]

vidas_jugador1={"barcos_pequenos":6,
                "barcos_medianos":4,
                "barcos_grandes":2}
vidas_jugador2={"barcos_pequenos":6,
                "barcos_medianos":4,
                "barcos_grandes":2}

def quitar_vidas(jugador:int,tipo_barco:str):
    print(vidas_jugador2["barcos_medianos"])
    global ultimo_intento
    if jugador==1:
        vidas_jugador1[tipo_barco]-=1
    if jugador==2:
        vidas_jugador2[tipo_barco]-=1
    if vidas_jugador1["barcos_medianos"] == 3 or vidas_jugador1["barcos_medianos"] == 2 or vidas_jugador1["barcos_medianos"] == 1:
        im.ptsj2+=2
    if vidas_jugador2["barcos_medianos"] == 3 or vidas_jugador2["barcos_medianos"] == 2 or vidas_jugador2["barcos_medianos"] == 1:
        im.ptsj1+=2
    if vidas_jugador1["barcos_grandes"] == 1 or vidas_jugador1["barcos_grandes"] == 0:
        im.ptsj2+=3
    if vidas_jugador2["barcos_grandes"] == 1 or vidas_jugador2["barcos_grandes"] == 0:
        im.ptsj1+=3
    #si las dos son cero es empate
    if vidas_jugador1["barcos_pequenos"]==0 and vidas_jugador1["barcos_medianos"]==0 and vidas_jugador1["barcos_grandes"]==0:
        if vidas_jugador2["barcos_pequenos"]==0 and vidas_jugador2["barcos_medianos"]==0 and vidas_jugador2["barcos_grandes"]==0:
            empate()
            return
    #Gana jugador 2
    #si una es cero y la otra mayor a 1 gana la primera
    if vidas_jugador1["barcos_pequenos"]==0 and vidas_jugador1["barcos_medianos"]==0 and vidas_jugador1["barcos_grandes"]==0:
        if vidas_jugador2["barcos_pequenos"]+vidas_jugador2["barcos_medianos"]+vidas_jugador2["barcos_grandes"]>1:
            anunciar_ganador(nombre_j2)
            return
    #si uno es cero y la otra es 1 el turno continua
    if vidas_jugador1["barcos_pequenos"]==0 and vidas_jugador1["barcos_medianos"]==0 and vidas_jugador1["barcos_grandes"]==0:
        if vidas_jugador2["barcos_pequenos"]+vidas_jugador2["barcos_medianos"]+vidas_jugador2["barcos_grandes"]==1:
            if ultimo_intento[0]==False:
                p_empate()
                ultimo_intento[0]=True
            else:
                anunciar_ganador(nombre_j2)
                return
    #Gana jugador 1
    #si una es cero y la otra mayor a 1 gana la primera
    if vidas_jugador2["barcos_pequenos"]==0 and vidas_jugador2["barcos_medianos"]==0 and vidas_jugador2["barcos_grandes"]==0:
        if vidas_jugador1["barcos_pequenos"]+vidas_jugador1["barcos_medianos"]+vidas_jugador1["barcos_grandes"]>1:
            anunciar_ganador(nombre_j1)
    #si uno es cero y la otra es 1 el turno continua
    if vidas_jugador2["barcos_pequenos"]==0 and vidas_jugador2["barcos_medianos"]==0 and vidas_jugador2["barcos_grandes"]==0:
        if vidas_jugador1["barcos_pequenos"]+vidas_jugador1["barcos_medianos"]+vidas_jugador1["barcos_grandes"]==1:
            if ultimo_intento[1]==False:
                p_empate()
                ultimo_intento[1]=True
            else:
                anunciar_ganador(nombre_j1)
                return

def perder_empate(jugador:int,mar:list,pos_y:int,pos_x:int):
    if ultimo_intento[jugador]==True and mar[pos_y][pos_x]["pieza"]==".":
        if jugador==0:
            anunciar_ganador(nombre_j2)
            return
        if jugador==1:
            anunciar_ganador(nombre_j1)
            return

def anunciar_ganador(jugador):
    ventana = tk.Tk()
    label = tk.Label(ventana, text=f"El ganador de esta partida es {jugador}",font=("ComicSansMS",25),bg="#8e582c",fg="#ffedba")
    ventana.title("Ganador")
    label.grid()
    ventana.mainloop()

def empate():
    ventana_empate = tk.Tk()
    label = tk.Label(ventana_empate, text=f"El resultado del juego ha sido un empate",font=("ComicSansMS",25),bg="#8e582c",fg="#ffedba")
    ventana_empate.title("Empate")
    label.grid()
    ventana_empate.mainloop()

def p_empate():
    ventana_p_empate = tk.Tk()
    label = tk.Label(ventana_p_empate, text=f"Hay posibilidad de empate",font=("ComicSansMS",25),bg="#8e582c",fg="#ffedba")
    ventana_p_empate.title("Posible Empate")
    label.grid()
    ventana_p_empate.mainloop()