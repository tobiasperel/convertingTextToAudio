import PyPDF2
from gtts import gTTS
import os

# rute of the pdf file
pdf_path = "" # here goes the path of the pdf file
output_audio_path = "" #here goes the path of the output audio file


# read the pdf file and extract the text
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


# extract the text
pdf_text = extract_text_from_pdf(pdf_path)

# clear the text
pdf_text = clear_text(pdf_text)
print(pdf_text)

# generate the audio
tts = gTTS(text=pdf_text, lang="es")
tts.save(output_audio_path)

# Reproducir el audio (opcional)
os.system("start " + output_audio_path)  # Esto es para sistemas Windows
# Para sistemas macOS puedes usar: os.system("open " + output_audio_path)
# Para sistemas Linux puedes usar: os.system("xdg-open " + output_audio_path)
