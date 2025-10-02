# Fuerza Brute / Brute Force

## Español

Este script permite **buscar la contraseña original** correspondiente a un **hash SHA-256** dentro de un archivo de diccionario de contraseñas.

### Funcionamiento

1. El usuario introduce un hash SHA-256 por consola.
2. El programa abre un archivo de texto (`contrasenas_test.txt`) que contiene una lista de posibles contraseñas.
3. Cada contraseña del archivo se convierte en SHA-256 y se compara con el hash introducido.
4. Si encuentra coincidencia, devuelve la contraseña original.
5. Si no encuentra coincidencia, informa que la contraseña no está en la lista.

### Uso

1. Guarda tus contraseñas en un archivo de texto, una por línea.
   Ejemplo (`contrasenas_test.txt`):

   ```
   password123
   admin
   qwerty
   ```
2. Ejecuta el script:

   ```bash
   python script.py
   ```
3. Introduce un hash SHA-256 cuando se te solicite.
4. El programa indicará si encontró la contraseña en el diccionario.

### Ejemplo de ejecución

```
Dime un sha para buscar su contraseña en el diccionario
ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
La contraseña para el sha ef92b778... es password123
```

---

## English

This script allows you to **find the original password** corresponding to a **SHA-256 hash** inside a password dictionary file.

### How it works

1. The user inputs a SHA-256 hash via the console.
2. The program opens a text file (`contrasenas_test.txt`) that contains a list of possible passwords.
3. Each password from the file is hashed using SHA-256 and compared to the provided hash.
4. If a match is found, it returns the original password.
5. If no match is found, it reports that the password is not in the list.

### Usage

1. Save your candidate passwords in a text file, one per line.
   Example (`contrasenas_test.txt`):

   ```
   password123
   admin
   qwerty
   ```
2. Run the script:

   ```bash
   python script.py
   ```
3. Enter a SHA-256 hash when prompted.
4. The program will tell you if it found the password in the dictionary.

### Example execution

```
Dime un sha para buscar su contraseña en el diccionario
ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
La contraseña para el sha ef92b778... es password123
```
