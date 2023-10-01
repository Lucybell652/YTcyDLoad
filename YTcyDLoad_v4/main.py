#Version 4
from art import * # Importamos "art" para diseños to' wuapos
from modulos.sistema import mensaje as msg # Importamos la funcion de mensaje
from modulos.descargas import ( 
    descargar_mp3_playlist as dmp, # Funcion de descarga audio para playlist
    descargar_video_playlist as dvp, # Funcion de descarga video para playlist
    descarga_video as dv, # Funcion para descarga video individual
    descargar_video_mp3 as dvm, # Funcion para descarga audio individual
)


def opcion(respuesta, opcion_valida): # Creamos funcion para las opciones del usuario
    while True:
        try:
            opcion = int(input(respuesta)) # Solicitamos opcion, y la convertimos a digito
            if opcion in opcion_valida: 
                return opcion
            else:
                msg()  # Limpia la consola en caso de opción no válida
        except ValueError:
            msg()  # Limpia la consola en caso de entrada no válida

def main(): # La "interfaz"
    while True:
        msg() # Limpia consola
        opcion_vid_play = opcion( # Guardamos opcion del usuario para video/playlist
            "Ingresa el digito correspondiente:\n1.- Un video\n2.- Playlist\n\n> ",
            [1, 2]
        )

        msg()
        opcion_vid_mp3 = opcion( # Guardamos opcion del usuario para formato
            "En qué formato deseas la descarga?:\n1.- Video\n2.- Audio\n\n> ",
            [1, 2]
        )

        msg()
        mlink = "Ingresa tu enlace de YouTube"
        print(f"{mlink:^62}") # Centramos
        print()
        link = input("> ") # Solicitamos link

        if opcion_vid_play == 1: # Si elige "video"...
            if opcion_vid_mp3 == 1: #... y formato "video"
                dv(link) # Descarga el video individual
            else: # Pero si elige "Audio"...
                dvm(link) # ... Descarga el audio individual
        else: # Pero si eligue "Playlist"...
            if opcion_vid_mp3 == 1: # ... y "Video"
                dvp(link) # Descarga video por lista
            else: # Pero si elige "Audio"
                dmp(link) # Descarga audio por lista
        
        dterm = "Descarga terminada" # Un mensaje de termino
        print(f"{dterm:^62}")
        print()
        respuesta = input("¿Deseas hacer otra descarga (Y/N)? ").strip().lower() # Preguntamos si quiere seguir o cerrar
        if respuesta != 'y': # Si no pulsa "y"
            break # Cerramos

if __name__ == "__main__":
    main()
