import os

def ruta_fin_video(): # Obtener ruta raiz de descargas, obtener subcarpeta "video" y crearla en caso de no existir
    descargas_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    carpeta_video = os.path.join(descargas_path, 'video') 
    if not os.path.exists(carpeta_video):
        os.makedirs(carpeta_video)
    return carpeta_video


def ruta_fin_audio(): # Lo mismo que la anterior, pero con una subcarpeta "audio"
    descargas_path = os.path.join(os.path.expanduser('~'), 'Downloads') 
    carpeta_audio = os.path.join(descargas_path, 'audio')
    if not os.path.exists(carpeta_audio): 
        os.makedirs(carpeta_audio)
    return carpeta_audio


def limpiar_nombre(archivo): # Quitamos caracteres invalidos en el titulo de la descarga, para evitar errores
    nombre, extension = os.path.splitext(archivo)
    invalid_chars = r'\/:*?"<>|\''
    for char in invalid_chars:
        nombre = nombre.replace(char, '_')
    archivo_limpio = nombre + extension
    return archivo_limpio