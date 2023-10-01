#Version 3
import os
import time
from pytube import YouTube, Playlist
from moviepy.editor import *
from modulos.sistema import (
    ruta_fin_audio as rfa,
    ruta_fin_video as rfv,
    limpiar_nombre as lnom,
    mensaje as msg,
    sep,
)

def descarga_video(link):
    yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    carpeta_video = rfv()
    try:
        titulo_video = lnom(yt.title) # Obtener el título...
        autor_video = lnom(yt.author) #... y el autor del video y limpiarlos

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
    carpeta_audio = rfa()
    try:
        titulo_video = lnom(yt.title)
        autor_video = lnom(yt.author)
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
    carpeta_video = rfv()
    try:
        playlist = Playlist(link)
        for video_url in playlist.video_urls:
            yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)  # Mueve esta línea aquí
            
            msg()
            sep()
            titulo_video = lnom(yt.title)
            autor_video = lnom(yt.author)
            print(f"Iniciando descarga de: {titulo_video} por {autor_video}")
            yt.streams.get_highest_resolution().download(carpeta_video)
            print("Finalizado")
            sep()
            time.sleep(2)
            msg()
    except Exception as e:
        print(f"La descarga falló: {str(e)}")


def descargar_mp3_playlist(link):
    carpeta_audio = rfa()
    try:
        playlist = Playlist(link)
        for video_url in playlist.video_urls:
            yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)  # Mueve esta línea aquí
            
            msg()
            sep()
            titulo_video = lnom(yt.title)
            autor_video = lnom(yt.author)
            titulo_video_limpio = titulo_video + " - " + autor_video
            print(f"Iniciando descarga de: {titulo_video} por {autor_video}")

            video_stream = yt.streams.get_highest_resolution()
            video_path = video_stream.download(carpeta_audio)
            audio_path = os.path.join(carpeta_audio, f"{titulo_video_limpio}.mp3")
            video_clip = VideoFileClip(video_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(audio_path)
            video_clip.close()
            os.remove(video_path)

            print("Finalizado")
            sep()
            time.sleep(2)
            msg()
    except Exception as e:
        print(f"La descarga falló: {str(e)}")
