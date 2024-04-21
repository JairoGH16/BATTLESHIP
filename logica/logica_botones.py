import turnos as tur
import logica.insertar as insert
import logica.logica_damage as damage


def accion_boton(posx,posy,config,columns,rows,matriz_botones,matriz_botones_rival,num_mar:int,mar1,mar2):
    if tur.turno<=2:
        insert.insertar_barcos(posx,posy,config,columns,rows,matriz_botones,num_mar,mar1,mar2)
    else:
        if num_mar==1 and tur.turno%2==0:
            damage.damage(posx,posy,mar1)
            tur.next_pj(matriz_botones,matriz_botones_rival,mar1,mar2)
            tur.next_pj(matriz_botones,matriz_botones_rival,mar1,mar2)
        elif num_mar==2 and tur.turno%2!=0:
            damage.damage(posx,posy,mar2)
            tur.next_pj(matriz_botones,matriz_botones_rival,mar1,mar2)
            tur.next_pj(matriz_botones,matriz_botones_rival,mar1,mar2)