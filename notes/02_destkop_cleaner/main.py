import os
import shutil

# Masaüstü yolu (Windows)
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")

# Dosya türleri
FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Archives": [".zip", ".rar"]
}

def clean_desktop():
    for file in os.listdir(DESKTOP_PATH):
        file_path = os.path.join(DESKTOP_PATH, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)

            for folder, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    folder_path = os.path.join(DESKTOP_PATH, folder)

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    shutil.move(file_path, folder_path)
                    break

if __name__ == "__main__":
    clean_desktop()
    print("Masaüstü temizlendi ✔")
