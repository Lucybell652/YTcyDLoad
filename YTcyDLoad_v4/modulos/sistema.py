#Version 3
import os
from art import *

def cls():
    os.system('cls')


def sep():
    print("=" * 71)


def mensaje():
    cls()
    tprint("YTcyDLoad")
    lucy = "LucyFer"
    print(f"{lucy:=^62}")
    print()


def ruta_fin_video():
    descargas_path = os.path.join(os.path.expanduser('~'), 'Downloads') #Obtener ruta raiz de descargas
    carpeta_video = os.path.join(descargas_path, 'video') #Crear carpeta de video
    if not os.path.exists(carpeta_video): #Si la carpeta no existe...
        os.makedirs(carpeta_video)  #...pues lo crea
    return carpeta_video


def ruta_fin_audio():
    descargas_path = os.path.join(os.path.expanduser('~'), 'Downloads') #Obtener ruta raiz de descargas
    carpeta_audio = os.path.join(descargas_path, 'audio') #Crear carpeta de audio
    if not os.path.exists(carpeta_audio): #Si la carpeta no existe...
        os.makedirs(carpeta_audio)  #...pues lo crea
    return carpeta_audio


def limpiar_nombre(archivo):
    nombre, extension = os.path.splitext(archivo)
    invalid_chars = r'\/:*?"<>|\''
    for char in invalid_chars:
        nombre = nombre.replace(char, '_')
    archivo_limpio = nombre + extension
    return archivo_limpio