# Conversor de MKV a MP3

![Icon](icono.ico)

## Descripción

El **Conversor de MKV a MP3** es una herramienta sencilla y eficiente diseñada para extraer pistas de audio de archivos MKV y convertirlas a formato MP3. Con una interfaz gráfica de usuario amigable, puedes seleccionar fácilmente el archivo MKV, elegir la pista de audio deseada y convertirla a MP3 con unos pocos clics.

## Características

- **Interfaz gráfica amigable**: Fácil de usar para usuarios de todos los niveles.
- **Selección de pistas de audio**: Permite seleccionar la pista de audio deseada de un archivo MKV.
- **Conversión rápida**: Convierte rápidamente la pista de audio seleccionada a formato MP3.
- **Animación de progreso**: Muestra una animación mientras se realiza la conversión.

## Requisitos del sistema

Para que este software funcione correctamente, necesitas tener instalados los siguientes programas en tu sistema:

1. **FFmpeg**
   - Descarga e instala FFmpeg desde [FFmpeg](https://ffmpeg.org/download.html).
   - Asegúrate de agregar FFmpeg a tu PATH del sistema.

2. **MKVToolNix**
   - Descarga e instala MKVToolNix desde [MKVToolNix](https://mkvtoolnix.download/).
   - Asegúrate de que `mkvextract.exe` esté en `C:\Program Files\MKVToolNix\`.

3. **FFprobe**
   - FFprobe se incluye con la instalación de FFmpeg.
   - Asegúrate de que esté disponible en tu PATH del sistema.

## Instalación



### Uso del Instalador

1. Descomprime y descarga el archivo de instalador [Instalador_Conversor_MKV_a_MP3.zip](https://github.com/fredycoding/mkvextractor/raw/main/Output/Instalador_Conversor_MKV_a_MP3.zip).
2. Ejecuta el instalador y sigue las instrucciones en pantalla.
   - Si aparece una advertencia de Windows Defender, sigue estos pasos:
   - Haz clic en "Más información".
   - Haz clic en "Ejecutar de todas formas".
3. Sigue las instrucciones en pantalla para completar la instalación.
4. Una vez completada la instalación, puedes encontrar el programa en el menú de inicio o en el escritorio.

5. Una vez completada la instalación, puedes encontrar el programa en el menú de inicio o en el escritorio.


### Ejecución desde el Código Fuente

1. Asegúrate de tener Python instalado en tu sistema.
2. Clona este repositorio o descarga el código fuente.
3. Instala las dependencias necesarias:
   ```sh
   pip install -r requirements.txt
