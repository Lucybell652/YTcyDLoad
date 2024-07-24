import os 
import time
from pytubefix import YouTube, Playlist # Pytube para las descargas de videos...
from moviepy.editor import * #... y MoviePy para convertir a mp3
from modulos.sistema import (
    ruta_fin_audio,
    ruta_fin_video,
    limpiar_nombre,
    mensaje as msg,
    sep,
)

def descarga_video(link):
    yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    carpeta_video = ruta_fin_video()
    try:
        titulo_video = limpiar_nombre(yt.title) # Obtener el título...
        autor_video = limpiar_nombre(yt.author) #... y el autor del video y limpiarlos

        msg()
        sep()
        print(f"Iniciando descarga de: {titulo_video} por {autor_video}")
        yt.streams.get_highest_resolution().download(carpeta_video)
        print("Finalizado")
        sep()
        time.sleep(2)
        msg()
    except Exception as e:
        print(f"La descarga falló: {str(e)}")


def descargar_video_mp3(link):
    yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    carpeta_audio = ruta_fin_audio()
    try:
        titulo_video = limpiar_nombre(yt.title)
        autor_video = limpiar_nombre(yt.author)
        titulo_video_limpio = titulo_video + " - " + autor_video

        msg()
        sep() 
        print(f"Iniciando descarga de: {titulo_video} por {autor_video}")
        video_stream = yt.streams.get_highest_resolution()
        video_path = video_stream.download(carpeta_audio)  # Descarga el video a la carpeta "audio"
        audio_path = os.path.join(carpeta_audio, f"{titulo_video_limpio}.mp3") # Convierte el video a formato MP3
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_path)
        video_clip.close() # Cierra el archivo de video antes de eliminarlo
        os.remove(video_path) # Elimina el archivo de video después de cerrarlo
        sep()
        print("Finalizado")
        time.sleep(2)
        msg()
    except Exception as e:
        print(f"La descarga falló: {str(e)}")


def descargar_video_playlist(link):
    carpeta_video = ruta_fin_video()
    try:
        playlist = Playlist(link)
        for video_url in playlist.video_urls:
            descarga_video(video_url)  # Llama a la función descarga_video
    except Exception as e:
        print(f"La descarga falló: {str(e)}")


def descargar_mp3_playlist(link):
    carpeta_audio = ruta_fin_audio()
    try:
        playlist = Playlist(link)
        for video_url in playlist.video_urls:
            descargar_video_mp3(video_url)
    except Exception as e:
        print(f"La descarga falló: {str(e)}")
