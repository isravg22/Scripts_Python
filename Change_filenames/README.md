# Renombrador de Archivos / File Renamer

## Versión Española

## Descripción

Este script de Python permite renombrar múltiples archivos en una carpeta de forma automática y secuencial. Los archivos renombrados se guardan en una nueva carpeta llamada "renombrados", manteniendo los archivos originales intactos.

## Características

- Renombra múltiples archivos de forma secuencial
- Crea automáticamente una carpeta "renombrados" para los nuevos archivos
- Preserva los archivos originales (hace copias)
- Mantiene las extensiones originales de los archivos
- Permite personalizar el nombre base para todos los archivos

## Cómo usar

### Requisitos

- Python 3.x instalado en tu sistema

### Ejecución

1. Ejecuta el script desde la terminal o línea de comandos:

    ```bash
    python file_name.py
    ```

2. Introduce la ruta de la carpeta que contiene los archivos a renombrar:

    ```text
    Ingrese la ruta de la carpeta: C:\mi_carpeta\fotos
    ```

3. Introduce el nuevo nombre base para los archivos:

    ```text
    Ingrese el nuevo nombre para los archivos: vacaciones
    ```

### Ejemplo de funcionamiento

**Archivos originales:**

```text
mi_carpeta/
├── IMG_001.jpg
├── IMG_002.jpg
├── documento.pdf
└── video.mp4
```

**Después de ejecutar el script:**

```text
mi_carpeta/
├── IMG_001.jpg          (archivos originales intactos)
├── IMG_002.jpg
├── documento.pdf
├── video.mp4
└── renombrados/         (nueva carpeta creada)
    ├── vacaciones-1.jpg
    ├── vacaciones-2.jpg
    ├── vacaciones-3.pdf
    └── vacaciones-4.mp4
```

## Cómo funciona

El script realiza las siguientes operaciones:

1. **Solicita información al usuario:**
   - Ruta de la carpeta con los archivos
   - Nombre base para los nuevos archivos

2. **Crea la carpeta de destino:**
   - Genera una carpeta llamada "renombrados" dentro de la carpeta especificada
   - Si ya existe, la utiliza sin sobrescribir

3. **Lista los archivos:**
   - Obtiene todos los archivos de la carpeta (excluyendo subcarpetas)
   - Ignora la carpeta "renombrados" para evitar conflictos

4. **Renombra y copia:**
   - Mantiene la extensión original de cada archivo
   - Asigna un número secuencial (1, 2, 3...)
   - Copia cada archivo con el nuevo nombre a la carpeta "renombrados"

## Módulos utilizados

- **`os`**: Para operaciones del sistema de archivos (crear carpetas, listar archivos)
- **`shutil`**: Para copiar archivos manteniendo metadatos

## Anotaciones interesantes

- Los archivos originales **NO** se eliminan, solo se copian
- Si la carpeta "renombrados" ya existe, se utilizará sin problemas
- Las extensiones de archivo se mantienen automáticamente
- El script procesa solo archivos, ignorando subcarpetas

## ¿Para que podemos utilizar este script?

- Organizar fotos de eventos o viajes
- Renombrar documentos escaneados secuencialmente
- Preparar archivos para carga masiva en sistemas
- Estandarizar nombres de archivos en proyectos

## English Version

## Description

This Python script automatically and sequentially renames multiple files in a folder. The renamed files are saved in a new folder called "renombrados", keeping the original files intact.

## Features

- Sequentially renames multiple files
- Automatically creates a "renombrados" folder for new files
- Preserves original files (makes copies)
- Keeps the original file extensions
- Allows customizing the base name for all files

## How to Use

### Requirements

- Python 3.x installed on your system

### Execution

1. Run the script from the terminal or command line:

    ```bash
    python file_name.py
    ```

2. Enter the path to the folder containing the files to rename:

    ```text
    Enter the folder path: C:\my_folder\photos
    ```

3. Enter the new base name for the files:

    ```text
    Enter the new name for the files: vacation
    ```

### Example

**Original files:**

```text
my_folder/
├── IMG_001.jpg
├── IMG_002.jpg
├── document.pdf
└── video.mp4
```

**After running the script:**

```text
my_folder/
├── IMG_001.jpg          (original files intact)
├── IMG_002.jpg
├── document.pdf
├── video.mp4
└── renombrados/         (new folder created)
    ├── vacation-1.jpg
    ├── vacation-2.jpg
    ├── vacation-3.pdf
    └── vacation-4.mp4
```

## How It Works

The script performs the following operations:

1. **Requests user input:**
   - Folder path containing the files
   - Base name for the new files

2. **Creates the destination folder:**
   - Generates a folder named "renombrados" inside the specified folder
   - If it already exists, it uses it without overwriting

3. **Lists the files:**
   - Gets all files in the folder (excluding subfolders)
   - Ignores the "renombrados" folder to avoid conflicts

4. **Renames and copies:**
   - Keeps the original extension of each file
   - Assigns a sequential number (1, 2, 3...)
   - Copies each file with the new name to the "renombrados" folder

## Modules Used

- **`os`**: For file system operations (creating folders, listing files)
- **`shutil`**: For copying files while preserving metadata

## Interesting Notes

- Original files are **NOT** deleted, only copied
- If the "renombrados" folder already exists, it will be used without issues
- File extensions are automatically preserved
- The script processes only files, ignoring subfolders

## What Can You Use This Script For?

- Organizing event or travel photos
- Sequentially renaming scanned documents
- Preparing files for bulk upload to systems
- Standardizing file names in projects
