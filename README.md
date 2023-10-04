# YTcyDLoad o(*￣▽￣*)ブ
(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧ YouTube Lucy DownLoader (⁠ ⁠ꈍ⁠ᴗ⁠ꈍ⁠)

## Descripción 👌
YTcyDLoad es un programa de línea de comandos (CLI) diseñado para descargar videos y audio de YouTube. El programa ofrece opciones para descargar videos individuales, listas de reproducción de videos y convertir videos en formato MP3. El código está estructurado en varios módulos para mantenerlo organizado y modular.

## Requisitos 💻
- Python 3.x
- Bibliotecas de Python: pytube, moviepy, art

## Uso 👩‍💻
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

## Estructura del Código 💻
- `main.py`: Este es el punto de entrada del programa. Controla la interfaz de usuario y llama a las funciones de descarga correspondientes.
- `modulos/sistema.py`: Contiene funciones para la gestión de la consola, limpieza de nombres de archivos y obtención de rutas de destino.
- `modulos/descargas.py`: Contiene funciones para la descarga de videos y conversiones a MP3. Utiliza la biblioteca `pytube` para descargar videos de YouTube y `moviepy` para convertir videos a MP3.

## Personalización 🖖
- Puedes personalizar las carpetas de destino modificando las funciones `ruta_fin_video()` y `ruta_fin_audio()` en `modulos/sistema.py`.
- Puedes personalizar el comportamiento de las funciones de descarga agregando opciones adicionales o ajustando la resolución de los videos descargados en `modulos/descargas.py`.

## Notas Importantes ‼️
- Este programa se basa en bibliotecas de terceros y utiliza la API de YouTube para descargar contenido. Asegúrate de cumplir con los términos de servicio de YouTube al utilizar esta herramienta.
- El programa utiliza la biblioteca "art" para imprimir un título decorativo en la consola. Asegúrate de tener esta biblioteca instalada para obtener una mejor experiencia visual.

## Errores detectados 😓
- Aún falla la descarga en videos con restricciones de edad o enlaces privados.
- A veces la autorización OAuth falla, deteniendo la descarga o cerrando la consola.

## Futuras actualizaciones ♥️
- Mejorar el manejo de errores y evitar que las descargas se detengan cuando un link falla.
- Solucionar el problema con OAuth
- Crear una interfaz gráfica para facilitar el uso del programa.

¡Disfruta descargando contenido de YouTube con YTcyDLoad!
