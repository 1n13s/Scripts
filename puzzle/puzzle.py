import os
import re

folder_path = 'extracted_content'
subfolders = os.listdir(folder_path)
#Obtains all the folders
folders = [folder for folder in subfolders if os.path.isdir(os.path.join(folder_path, folder))]

for folder in folders:
    current_folder = os.path.join(folder_path,folder)
    files = [f for f in os.listdir(current_folder) if os.path.isfile(os.path.join(current_folder, f))]

    #Obtains all the files in each folder
    for file in files:
        ruta_archivo = os.path.join(current_folder, file)
        with open(ruta_archivo, 'r') as file:
            contenido = file.read()
            pattern = r'\d{3}-\d{3}-\d{4}'
            matches = re.findall(pattern,contenido)
            if len(matches) > 0:
                for match in matches:
                    phone_number = match

print(f"The phone number is {phone_number}")
                    
