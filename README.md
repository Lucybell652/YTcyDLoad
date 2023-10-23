# YouTube Lucy DownLoader (YTcyDLoad) o(*￣▽￣*)ブ

![logo-removebg-preview](https://github.com/Lucybell652/YTcyDLoad/assets/142288977/9a4273d1-597c-4f3e-9c9e-6c7fe89aaf50)

## Descripción 👌
YTcyDLoad es un programa de línea de comandos (CLI) e intefaz grafica diseñado para descargar videos y audio de YouTube. El programa ofrece opciones para descargar videos individuales, listas de reproducción de videos y convertir videos en formato MP3. El código está estructurado en varios módulos para mantenerlo organizado y modular.

## Requisitos 💻
1. Python 3.x
2. Bibliotecas de Python:
   - pytube
   - moviepy
   - requests
   - customtkinter
   - art (para la version de consola)

## Uso 👩‍💻
En consola:
1. Ejecuta `main.py` para iniciar el programa.
2. Selecciona la opción deseada ingresando el número correspondiente:
   - 1: Descargar un video individual.
   - 2: Descargar una lista de reproducción (playlist).
3. Elige el formato de descarga:
   - 1: Video.
   - 2: Audio (MP3).
4. Ingresa el enlace de YouTube del video o lista de reproducción que deseas descargar.
5. El programa descargará el contenido seleccionado en la carpeta "Downloads" de tu sistema, en subcarpetas "video" o "audio", según corresponda.
6. Después de la descarga, verás un mensaje de finalización y se te preguntará si deseas realizar otra descarga.

En interfaz:
1. Ejecuta `main.py` para iniciar el programa.
2. Ingresa el link en el cuadro de texto.
3. Selecciona el boton correspondiente:
   - 1: Descargar un video individual.
   - 2: Descargar una lista de reproducción (playlist).
4. Pulsa el boton de formato de descarga:
   - 1: Video (MP4).
   - 2: Audio (MP3).
5. El programa descargará el contenido seleccionado en la carpeta "Downloads" de tu sistema, en subcarpetas "video" o "audio", según corresponda.
6. Terminado la descarga, mostrará un mensaje de "Listo". Aun no permite la descarga multiple, debe cerrar ventana y abrir nuevamente.

## Estructura del Código 💻
- `main.py`: Este es el punto de entrada del programa. Controla la interfaz de usuario y llama a las funciones de descarga correspondientes.
- `modulos/sistema.py`: Contiene funciones para la gestión de la consola, limpieza de nombres de archivos y obtención de rutas de destino.
- `modulos/descargas.py`: Contiene funciones para la descarga de videos y conversiones a MP3. Utiliza la biblioteca `pytube` para descargar videos de YouTube y `moviepy` para convertir videos a MP3.
- `modulos/interfaz.py`: Contiene el codigo de la interfaz grafica en una class. Utiliza `customtkinter` para una interfaz mas moderna a `tkinter` 

## Personalización 🖖
- Puedes personalizar las carpetas de destino modificando las funciones `ruta_fin_video()` y `ruta_fin_audio()` en `modulos/sistema.py`.
- Puedes personalizar el comportamiento de las funciones de descarga agregando opciones adicionales o ajustando la resolución de los videos descargados en `modulos/descargas.py`.
- Puedes personalizar los elementos que conforman la interfaz, como botones, lebels, barras de progreso, etc. en `modulos/interfaz.py`

## Notas Importantes ‼️
- Este programa se basa en bibliotecas de terceros y utiliza la API de YouTube para descargar contenido. Asegúrate de cumplir con los términos de servicio de YouTube al utilizar esta herramienta.
- El programa utiliza la biblioteca "art" para imprimir un título decorativo en la consola. Asegúrate de tener esta biblioteca instalada para obtener una mejor experiencia visual.

## Errores detectados 😓
- Aún falla la descarga en videos con restricciones de edad o enlaces privados.
- A veces la autorización OAuth falla, deteniendo la descarga o cerrando la consola.
- En la interfaz, si la descarga falla por un error de red o el enlace es incorrecto, falla sin mostar error y no permite continuar con la descarga
- No se puede realizar una nueva descarga desde la venta abierta. Debe cerrarse y abrir nuevamente para descargar otro video o playlist.

## Futuras actualizaciones ♥️
- Mejorar el manejo de errores y evitar que las descargas se detengan cuando un link falla.
- Solucionar el problema con OAuth
- Mejorar la interfaz gráfica agregando una barra de progreso.
- La opcion de realizar una nueva descarga sin cerrar la interfaz.

¡Disfruta descargando contenido de YouTube con YTcyDLoad!
