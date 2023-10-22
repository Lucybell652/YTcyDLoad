import customtkinter as CTk # Una version mejorada de Tkinter
from modulos.descargas import (
    descarga_video,
    descargar_video_mp3,
    descargar_video_playlist,
    descargar_mp3_playlist
)

boton_elegido = None
boton_formato = None

def video_indiv(): # Opcion de un solo video 
    global boton_elegido
    boton_elegido = "video_individual"
    crear_botones_inferiores()

def playlist(): # Opcion de playlist
    global boton_elegido
    boton_elegido = "playlist"
    crear_botones_inferiores()

def video_formato(): # Opcion de descargar el video (mp4)
    global boton_formato
    boton_formato = "video_formato"
    boton_descarga()

def mp3(): # Opcion de solo audio
    global boton_formato
    boton_formato = "mp3"
    boton_descarga()

def crear_botones_inferiores(): # Para mostrar los botones de las opciones "Video" y "MP3 (Audio)"
    CTk.CTkLabel(window, text="Elige formato a descargar:").place(x=133, y=150)
    boton_video = CTk.CTkButton(window, text="Video", width=100, height=25, command=video_formato).place(x=96, y=180)
    boton_mp3 = CTk.CTkButton(window, text="MP3", width=100, height=25, command=mp3).place(x=212, y=180)
    window.geometry("400x210") # Cambiamos tamaño de la ventana, solo por razones esteticas

def boton_descarga():
    inicio = CTk.CTkLabel(window, text="Pulse para descargar").place(x=150, y=210)
    boton_descarga = CTk.CTkButton(window, text="Descargar", width=100, height=25, command=iniciar_descarga).place(x=155, y=240)
    window.geometry("400x300") # Nuevamente cambiamos tamaño de la ventana

def iniciar_descarga():
    url = entrada_url.get()  # Obtiene la URL del campo de entrada

    if boton_elegido == "video_individual":
        if boton_formato == "video_formato":
            descarga_video(url)
            fin.place(x=190, y=270)
        else:
            descargar_video_mp3(url)
            fin.place(x=190, y=270)
    else:
        if boton_formato == "video_formato":
            descargar_video_playlist(url)
            fin.place(x=190, y=270)
        else:
            descargar_mp3_playlist
            fin.place(x=190, y=270)

window = CTk.CTk() # Creamos ventana...
window.title("YTcyDLoad")
window.geometry("400x180") # ... con este tamaño.

CTk.CTkLabel(window, text="YTcyDLoad", font=CTk.CTkFont(size=20, weight="bold")).pack(pady=10) 
CTk.CTkLabel(window, text="Ingresa el URL de Youtube:").pack()
entrada_url = CTk.CTkEntry(window, width=300, placeholder_text="URL...").pack()
boton_video = CTk.CTkButton(window, text="Video", width=100, height=25, command=video_indiv).place(x=96, y=120)
boton_playlist = CTk.CTkButton(window, text="Playlist", width=100, height=25, command=playlist).place(x=212, y=120)
fin = CTk.CTkLabel(window, text="Listo") # Todos los botones están colocados en la ventana, menos éste porque se muestra con la funcion "iniciar_descarga()"

# Mostramos la ventana
window.mainloop()
