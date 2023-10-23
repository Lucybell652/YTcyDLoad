import requests
from pathlib import Path
import customtkinter as cTk
from modulos.descargas import (
    descarga_video,
    descargar_video_mp3,
    descargar_video_playlist,
    descargar_mp3_playlist
)

icono = Path(__file__).parent / "icono/icon.ico"

class Interfaz(cTk.CTk):
    """Interfaz grafica para descargar videos y playlists de Youtube.

        Metodos:
        crear_elementos(): Crea los elementos principales de la interfaz.
        update_url(): Actualiza la variable `url` con el texto ingresado por el usuario.
        crear_botones_inferiores(): Crea los botones para elegir el formato de descarga.
        evento_boton_video(): Guarda en la variable 'boton_elegido' la opcion de descargar video individual.
        evento_boton_playlist(): Guarda en la variable 'boton_elegido' la opcion de descargar una lista (playlist).
        evento_video_formato(): Guarda en la variable 'formato' la opcion de descargar en formato mp4 (video).
        evento_mp3_formato(): Guarda en la variable 'formato' la opcion de descargar en formato mp3 (audio).
        boton_descarga(): Crea un boton, le vinculamos la funcion de descarga y cambiamos el tamañó de pantalla.
        evento_boton_descarga(): Funcion de descarga.
    """

    def __init__(self):
        super().__init__()
        cTk.set_appearance_mode("dark")
        cTk.set_default_color_theme("green")
        self.iconbitmap(icono)
        self.geometry("400x180")
        self.url = ""
        self.boton_elegido = ""
        self.formato = ""
        self.crear_elementos()

    def crear_elementos(self):
        """Creamos la mayoria de elementos que se muestran en pantalla.
        """
        cTk.CTkLabel(self, text="YTcyDLoad", font=cTk.CTkFont(size=20, weight="bold")).pack(pady=10)
        cTk.CTkLabel(self, text="Ingresa el URL de Youtube:").pack()

        # Vincular entrada_url a una función que retorna el link ingresado
        self.entrada_url = cTk.CTkEntry(self, width=300, placeholder_text="URL...")
        self.entrada_url.bind('<KeyRelease>', self.update_url)
        self.entrada_url.place(x=52, y =77)

        self.boton_video = cTk.CTkButton(self, text="Video", text_color= ("black"), font=cTk.CTkFont(weight="bold"),width=100, height=25, command=self.evento_boton_video).place(x=96, y=120)
        self.boton_playlist = cTk.CTkButton(self, text="Playlist", text_color= ("black"), font=cTk.CTkFont(weight="bold"), width=100, height=25, command=self.evento_boton_playlist).place(x=212, y=120)
        self.fin = cTk.CTkLabel(self, text="Listo") # Todos los botones están colocados en la ventana, menos éste porque se muestra con la funcion "iniciar_descarga()"

    def update_url(self, event):
        """Actualiza la variable `url` con el texto ingresado por el usuario.

        Args:
            event (tkinter.Event): El evento que desencadenó la llamada a la función. En este caso, es la liberación de una tecla en la entrada de texto.
        """
        self.url = self.entrada_url.get() # Actualiza entrada_url con el link ingresado

    def crear_botones_inferiores(self):
        """Creamos los botones para elegir el formato de descarga (MP4 y MP3).
        """
        self.texto_formato = cTk.CTkLabel(self, text="Elige formato a descargar:").place(x=133, y=150)
        self.boton_video = cTk.CTkButton(self, text="Video", text_color= ("black"), font=cTk.CTkFont(weight="bold"), width=100, height=25, command=self.evento_video_formato).place(x=96, y=180)
        self.boton_mp3 = cTk.CTkButton(self, text="MP3", text_color= ("black"), font=cTk.CTkFont(weight="bold"), width=100, height=25, command=self.evento_mp3_formato).place(x=212, y=180)
        self.geometry("400x210") # Cambiamos tamaño de la ventana, solo por razones esteticas

    def evento_boton_video(self):
        """Guardamos en la variable 'boton_elegido' la opcion de descargar video individual
        """
        self.boton_elegido = "video_individual"
        self.crear_botones_inferiores()

    def evento_boton_playlist(self):
        """Guardamos en la variable 'boton_elegido' la opcion de descargar una lista (playlist)
        """
        self.boton_elegido = "playlist"
        self.crear_botones_inferiores()

    def evento_video_formato(self):
        """Guardamos en la variable 'formato' la opcion de descargar en formato mp4 (video)
        """
        self.formato = "video"
        self.boton_descarga()

    def evento_mp3_formato(self):
        """Guardamos en la variable 'formato' la opcion de descargar en formato mp3 (audio)
        """
        self.formato = "mp3"
        self.boton_descarga()

    def boton_descarga(self):
        """Creamos un boton, le vinculamos la funcion de descarga y cambiamos el tamañó de pantalla
        """
        cTk.CTkLabel(self, text="Pulsa el boton para iniciar").place(x=135, y=210)
        self.boton_descarga = cTk.CTkButton(self, text="Descarga", text_color= ("black"), font=cTk.CTkFont(weight="bold"), command=self.evento_boton_descarga).place(x=137, y=240)
        self.geometry("400x300")

    def evento_boton_descarga(self):
        """Funcion de descarga

        Una vez pulsado el boton de descarga, toma las variables 'boton_elegido' y 'formato' para descargar segun las indicaciones del usuario.
        Al final muestra el label "fin" (ya creado anteriormente) en pantalla
        """
        try:
            url = self.entrada_url.get()

            try:
                response = requests.get(url)
            except requests.exceptions.HTTPError:
                print("La URL ingresada no es valida")
                return

            if self.boton_elegido == "video_individual":
                if self.formato == "video":
                    descarga_video(url)
                    self.fin.place(x=190, y=270)
                else:
                    descargar_video_mp3(url)
                    self.fin.place(x=190, y=270)
            else:
                if self.formato == "video":
                    descargar_video_playlist(url)
                    self.fin.place(x=190, y=270)

                else:
                    descargar_mp3_playlist(url)
                    self.fin.place(x=190, y=270)
        except AttributeError:
            print("Debes ingresar una URL antes de iniciar la descarga.")