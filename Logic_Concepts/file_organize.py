import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            os.makedirs(f"{folder_path}/Texts", exist_ok=True)
            shutil.move(f"{folder_path}/{filename}", f"{folder_path}/Texts/{filename}")
        elif filename.endswith(".pdf"):
            os.makedirs(f"{folder_path}/PDFs", exist_ok=True)
            shutil.move(f"{folder_path}/{filename}", f"{folder_path}/PDFs/{filename}")

# Usage: organize_files("/Users/Name/Downloads")