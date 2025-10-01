# Calculador y Verificador de Hashes / Hash Calculator and Verifier

## Español

### Descripción

Este programa es una herramienta de verificación de integridad de archivos que calcula y compara hashes criptográficos. Permite verificar si los archivos han sido modificados o corrompidos comparando sus hashes SHA256 con valores de referencia almacenados en un archivo de texto.

### ¿Qué hace el programa?

1. **Calcula hashes**: Genera hash SHA256 de archivos utilizando bloques de 4096 bytes para optimizar el uso de memoria
2. **Lee archivo de hashes**: Procesa un archivo de texto que contiene nombres de archivos y sus hashes esperados
3. **Compara integridad**: Verifica si los archivos actuales coinciden con los hashes de referencia
4. **Reporta resultados**: Muestra si cada archivo es íntegro o ha sido modificado

### Características

- Soporte para algoritmo SHA256 (configurable para otros algoritmos de hashlib)
- Procesamiento eficiente de archivos grandes mediante lectura por bloques
- Manejo robusto de errores (archivos no encontrados, formatos incorrectos, etc.)
- Interfaz interactiva por línea de comandos
- Comparación detallada con resultados claros

### Formato del archivo de hashes

El archivo debe contener líneas con el formato:

```text
nombre_archivo.ext: hash_sha256_en_hexadecimal
```

Ejemplo:

```text
documento.pdf: a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456
imagen.jpg: 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```

### Uso

1. Ejecutar el programa: `python comprobación_hash.py`
2. Introducir la ruta del archivo que contiene los hashes esperados
3. Introducir la ruta del directorio donde están los archivos a verificar
4. El programa mostrará los resultados de la verificación para cada archivo

### Casos de uso

- Verificar la integridad de descargas
- Detectar modificaciones no autorizadas en archivos
- Validar copias de seguridad
- Control de calidad en transferencias de archivos
- Auditorías de seguridad

---

## English

### Description

This program is a file integrity verification tool that calculates and compares cryptographic hashes. It allows you to verify if files have been modified or corrupted by comparing their SHA256 hashes with reference values stored in a text file.

### What does the program do?

1. **Calculates hashes**: Generates SHA256 hash of files using 4096-byte blocks to optimize memory usage
2. **Reads hash file**: Processes a text file containing filenames and their expected hashes
3. **Compares integrity**: Verifies if current files match the reference hashes
4. **Reports results**: Shows whether each file is intact or has been modified

### Features

- Support for SHA256 algorithm (configurable for other hashlib algorithms)
- Efficient processing of large files through block reading
- Robust error handling (file not found, incorrect formats, etc.)
- Interactive command-line interface
- Detailed comparison with clear results

### Hash file format

The file should contain lines with the format:

```text
filename.ext: sha256_hash_in_hexadecimal
```

Example:

```text
document.pdf: a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456
image.jpg: 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```

### Usage

1. Run the program: `python comprobación_hash.py`
2. Enter the path to the file containing the expected hashes
3. Enter the path to the directory where the files to verify are located
4. The program will display the verification results for each file

### Use cases

- Verify download integrity
- Detect unauthorized file modifications
- Validate backups
- Quality control in file transfers
- Security audits

---

## Requisitos / Requirements

- Python 3.x
- Módulos estándar: `os`, `hashlib` / Standard modules: `os`, `hashlib`

## Autor / Author

Desarrollado para verificación de integridad de archivos / Developed for file integrity verification
