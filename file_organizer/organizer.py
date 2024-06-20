import os
import shutil
from typing import Dict
from collections import defaultdict

folder_path = "documents"
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def create_folder(folder_path: str, extension: str, folder_extensions: dict, file:str) -> Dict[str,str]|None:

    new_folder = False
    folder = extension.split(".")[1].upper()

    if folder_extensions[extension] == 0: 
        if not os.path.exists(os.path.join(folder_path,folder)):
            os.mkdir(os.path.join(folder_path,folder))
            print(f"El folder {folder} ha sido creado")
            new_folder = True

    move_file(os.path.join(folder_path,file),os.path.join(folder_path,folder,file),file)

    return {extension:folder} if new_folder else None

def move_file(current_path, destiny_path, file_name):
    shutil.move(current_path, destiny_path)
    print(f"El archivo {file_name} ha sido movido")


extensions = set()
folder_extensions = defaultdict(lambda:0)

for file in files:
    extension = os.path.splitext(file)[1]
    folder = create_folder(folder_path=folder_path,
                  extension=extension,
                  folder_extensions=folder_extensions,
                  file=file)
    if folder:
        folder_extensions.update(folder)


print(folder_extensions)

