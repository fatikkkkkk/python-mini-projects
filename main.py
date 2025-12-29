import speech_recognition as sr
from datetime import datetime
import os

# main.py'nin bulunduğu dizini al
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_DIR = os.path.join(BASE_DIR, "notes")

# notes klasörü yoksa oluştur
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Konuşabilirsiniz...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="tr-TR")
    print("Algılanan Metin:", text)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")
    file_path = os.path.join(NOTES_DIR, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    print("Not kaydedildi:", file_path)

except sr.UnknownValueError:
    print("Ses anlaşılamadı.")
except sr.RequestError:
    print("Servise ulaşılamadı.")
