vidas_jugador1={"barcos_pequeños":6,
                "barcos_medianos":4,
                "barcos_grandes":2}
vidas_jugador2={"barcos_pequeños":6,
                "barcos_medianos":4,
                "barcos_grandes":2}

def quitar_vidas(jugador:int,tipo_barco:str):
    if jugador==1:
        vidas_jugador1[tipo_barco]-=1
    if jugador==2:
        vidas_jugador2[tipo_barco]-=1
    if vidas_jugador1["barcos_pequeños"]==0 and vidas_jugador1["barcos_medianos"]==0 and vidas_jugador1["barcos_grandes"]==0:
        print("El ganador es el jugador 2")
    if vidas_jugador2["barcos_pequeños"]==0 and vidas_jugador2["barcos_medianos"]==0 and vidas_jugador2["barcos_grandes"]==0:
        print("El ganador es el jugador 1")