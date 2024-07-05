
### Código Principal
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import subprocess
import os
import json
from threading import Thread

def find_executable(executable_name):
    if os.name == 'nt':  # Si es Windows
        command = ["where", executable_name]
    else:  # Si es Unix-like (Linux, MacOS)
        command = ["which", executable_name]
    
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return None
    return result.stdout.strip()

def check_ffmpeg():
    ffmpeg_path = find_executable("ffmpeg")
    if not ffmpeg_path:
        messagebox.showerror("Error", "No se pudo encontrar ffmpeg. Asegúrate de que ffmpeg esté instalado y en tu PATH.")
        return None
    return ffmpeg_path

def check_mkvextract():
    mkvextract_path = r"C:\Program Files\MKVToolNix\mkvextract.exe"
    if not os.path.exists(mkvextract_path):
        messagebox.showerror("Error", "No se pudo encontrar mkvextract. Asegúrate de que mkvextract esté instalado en 'C:\\Program Files\\MKVToolNix\\'.")
        return None
    return mkvextract_path

def open_mkv():
    global file_path, audio_tracks
    file_path = filedialog.askopenfilename(filetypes=[("MKV files", "*.mkv")])
    if not file_path:
        return

    # Extraer información de las pistas de audio
    try:
        ffprobe_path = find_executable("ffprobe")
        if not ffprobe_path:
            messagebox.showerror("Error", "No se pudo encontrar ffprobe. Asegúrate de que ffprobe esté instalado y en tu PATH.")
            return

        result = subprocess.run([ffprobe_path, "-v", "error", "-select_streams", "a", "-show_entries", "stream=index:stream_tags=language", "-of", "json", file_path], capture_output=True, text=True)
        info = json.loads(result.stdout)
        audio_tracks = [(stream['index'], stream['tags'].get('language', 'unknown')) for stream in info['streams']]
        
        if not audio_tracks:
            messagebox.showerror("Error", "No se encontraron pistas de audio en el archivo.")
            return
        
        # Actualizar el ComboBox con las pistas de audio
        audio_select['values'] = [f"Track {index} - {language}" for index, language in audio_tracks]
        audio_select.current(0)
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al analizar el archivo MKV: {e}")

def convert_to_mp3():
    if not file_path:
        messagebox.showerror("Error", "No se ha seleccionado ningún archivo MKV.")
        return

    selected_index = audio_select.current()
    if selected_index == -1:
        messagebox.showerror("Error", "No se ha seleccionado ninguna pista de audio.")
        return

    track_index = audio_tracks[selected_index][0]
    
    ffmpeg_path = check_ffmpeg()
    if not ffmpeg_path:
        return

    # Obtener ruta de guardado
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if not save_path:
        return

    # Mostrar animación de conversión en progreso
    start_animation()

    # Ejecutar la conversión en un hilo separado
    def conversion_task():
        try:
            extract_command = [ffmpeg_path, "-i", file_path, "-map", f"0:{track_index}", "-q:a", "0", save_path]
            subprocess.run(extract_command, check=True)
            root.after(0, on_conversion_complete, True)
        except subprocess.CalledProcessError as e:
            root.after(0, on_conversion_complete, False, str(e))

    thread = Thread(target=conversion_task)
    thread.start()

def on_conversion_complete(success, error_message=None):
    stop_animation()
    if success:
        messagebox.showinfo("Éxito", "Conversión completada con éxito")
    else:
        messagebox.showerror("Error", f"Hubo un error durante la conversión: {error_message}")

def show_help():
    help_text = (
        "Para que este software funcione correctamente, necesitas tener instalados los siguientes programas:\n\n"
        "1. FFmpeg:\n"
        "   - Descarga e instala FFmpeg desde https://ffmpeg.org/download.html\n"
        "   - Asegúrate de agregar FFmpeg a tu PATH del sistema.\n\n"
        "2. MKVToolNix:\n"
        "   - Descarga e instala MKVToolNix desde https://mkvtoolnix.download/\n"
        "   - Asegúrate de que 'mkvextract.exe' esté en 'C:\\Program Files\\MKVToolNix\\'.\n\n"
        "3. FFprobe:\n"
        "   - FFprobe se incluye con la instalación de FFmpeg.\n"
        "   - Asegúrate de que esté disponible en tu PATH del sistema."
    )
    messagebox.showinfo("Ayuda", help_text)

def start_animation():
    global animation_running
    animation_running = True
    update_animation()

def stop_animation():
    global animation_running
    animation_running = False
    animation_label.config(image='')

def update_animation():
    global animation_frames, animation_index, animation_running
    if animation_running:
        animation_index = (animation_index + 1) % len(animation_frames)
        animation_label.config(image=animation_frames[animation_index])
        root.after(100, update_animation)  # Cambia el frame cada 100 ms

def load_animation_frames(gif_path):
    frames = []
    with Image.open(gif_path) as img:
        for frame in range(img.n_frames):
            img.seek(frame)
            frame_image = ImageTk.PhotoImage(img.copy())
            frames.append(frame_image)
    return frames

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def main():
    global file_path, audio_tracks, audio_select, animation_label, animation_frames, animation_index, animation_running, root

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Conversor de MKV a MP3")
    root.iconbitmap("icono.ico")  # Ruta del archivo .ico
    root.configure(bg='white')

    # Centrar la ventana
    window_width = 600
    window_height = 450
    center_window(root, window_width, window_height)

    # Estilo para ttk
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TLabel', background='white', font=('Arial', 12))
    style.configure('TButton', font=('Arial', 12), padding=5)
    style.configure('TCombobox', padding=5)

    # Crear un menú
    menubar = tk.Menu(root)
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Ayuda", command=show_help)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)
    root.config(menu=menubar)

    # Título
    title_label = tk.Label(root, text="Conversor de MKV a MP3", font=("Arial", 20, 'bold'), bg='white')
    title_label.pack(pady=10)

    # Crear un botón para seleccionar el archivo MKV
    btn_open = ttk.Button(root, text="Abrir archivo MKV", command=open_mkv)
    btn_open.pack(pady=10)

    # ComboBox para seleccionar la pista de audio
    audio_select_label = ttk.Label(root, text="Selecciona la pista de audio:")
    audio_select_label.pack(pady=5)

    audio_select = ttk.Combobox(root, font=("Arial", 12))
    audio_select.pack(pady=5)

    # Botón para convertir a MP3
    btn_convert = ttk.Button(root, text="Convertir a MP3", command=convert_to_mp3)
    btn_convert.pack(pady=20)

    # Label para mostrar el estado de la conversión
    animation_label = tk.Label(root, bg='white')
    animation_label.pack(pady=10)

    # Cargar frames de la animación GIF
    gif_path = "CONVIRTIENDO.gif"
    animation_frames = load_animation_frames(gif_path)

    animation_index = 0
    animation_running = False

    # Iniciar la aplicación
    root.mainloop()

if __name__ == "__main__":
    file_path = None
    audio_tracks = []
    main()
