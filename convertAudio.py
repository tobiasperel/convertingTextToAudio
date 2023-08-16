import PyPDF2
from gtts import gTTS
import os

# Ruta del archivo PDF
pdf_path = "E:\Programacion\Python\convertingTextToAudio\libro.pdf"

# Leer el contenido del PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def clear_text(text):
    text = text.replace("_", "")
    return text

# Nombre y ruta para el archivo de audio de salida
output_audio_path = "E:\Programacion\Python\convertingTextToAudio\exit.mp3"

# Extraer texto del PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Limpiar el texto extraído
pdf_text = clear_text(pdf_text)
print(pdf_text)

# Generar audio a partir del texto extraído
tts = gTTS(text=pdf_text, lang="es")
tts.save(output_audio_path)

# Reproducir el audio (opcional)
os.system("start " + output_audio_path)  # Esto es para sistemas Windows
# Para sistemas macOS puedes usar: os.system("open " + output_audio_path)
# Para sistemas Linux puedes usar: os.system("xdg-open " + output_audio_path)
