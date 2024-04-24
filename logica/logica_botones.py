import turnos as tur
import logica.insertar as insert
import logica.logica_damage as damage
import var_imagenes as im

def accion_boton(posx,posy,config,columns,rows,matriz_botones,num_mar:int,mar1,mar2):
    """dependiendo del turno, hace que los botones reaccionen de maneras diferentes

    Args:
        posx (int): posición x
        posy (int): posición y
        config (int): configuración
        columns (int): columnas
        rows (int): filas
        matriz_botones (list): matriz de botones
        num_mar (int): número del mar, 1 o 2
        mar1 (list): mar del jugador 1
        mar2 (list): mar del jugador 2
    """
    if tur.turno<=2:
        insert.insertar_barcos(posx,posy,config,columns,rows,matriz_botones,num_mar,mar1,mar2)
    else:
        if num_mar==2 and tur.turno%2!=0 and tur.ataque_posible==True:
            damage.damage(posx,posy,mar2,num_mar)
            tur.ataque_posible=False
        elif num_mar==1 and tur.turno%2==0 and tur.ataque_posible==True:
            damage.damage(posx,posy,mar1,num_mar)
            tur.ataque_posible=False