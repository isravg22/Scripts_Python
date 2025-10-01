import os
import shutil

def rename_files_in_folder(folder_path):
    renamed_folder = os.path.join(folder_path, "renombrados")
    os.makedirs(renamed_folder, exist_ok=True)
    
    new_name = input("Ingrese el nuevo nombre para los archivos: ")
    
    files = [f for f in os.listdir(folder_path) 
             if os.path.isfile(os.path.join(folder_path, f)) and f != "renombrados"]

    
    for index, f in enumerate(files, start=1):
        ext = os.path.splitext(f)[1]
        new_filename = f"{new_name}_{index}{ext}"
        src = os.path.join(folder_path, f)
        dst = os.path.join(renamed_folder, new_filename)
        shutil.copy2(src, dst)

    print("Archivos renombrados y guardados en la carpeta 'renombrados'.")

if __name__ == "__main__":
    ruta = input("Ingrese la ruta de la carpeta: ")
    rename_files_in_folder(ruta)
