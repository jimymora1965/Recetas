import os
from pathlib import Path

def agregar_receta(categoria, nombre_receta, ingredientes, pasos):
    # Construir la ruta del archivo de receta
    categoria_directory = Path(base_directory) / categoria
    receta_file = categoria_directory / (nombre_receta + ".txt")

    # Verificar si la categoría existe y crearla si es necesario
    if not categoria_directory.exists():
        categoria_directory.mkdir(parents=True)

    # Escribir la información de la receta en el archivo
    with receta_file.open("w") as f:
        f.write("Nombre de la receta: " + nombre_receta + "\n")
        f.write("Ingredientes: " + ingredientes + "\n")
        f.write("Pasos de preparación: " + pasos + "\n")

    print("Receta agregada con éxito.")

def buscar_receta(categoria, nombre_receta):
    # Construir la ruta del archivo de receta
    categoria_directory = Path(base_directory) / categoria
    receta_file = categoria_directory / (nombre_receta + ".txt")

    # Verificar si el archivo de receta existe
    if receta_file.exists():
        # Leer y mostrar la información de la receta
        with receta_file.open("r") as f:
            receta_info = f.read()
            print("Información de la receta:", receta_info)
    else:
        print("Receta no encontrada.")

def eliminar_receta(categoria, nombre_receta):
    # Construir la ruta del archivo de receta
    categoria_directory = Path("C:/Users/jimym/Documents/Udemy/Recetas") / categoria
    receta_file = categoria_directory / (nombre_receta + ".txt")

    # Verificar si el archivo de receta existe y eliminarlo si es necesario
    if receta_file.exists():
        receta_file.unlink()
        print("Receta eliminada con éxito.")
    else:
        print("Receta no encontrada.")

def crear_categoria(categoria):
    # Construir la ruta de la nueva categoría
    nueva_categoria_directory = Path("C:/Users/jimym/Documents/Udemy/Recetas") / categoria

    # Verificar si la categoría ya existe
    if nueva_categoria_directory.exists():
        print("La categoría ya existe.")
    else:
        nueva_categoria_directory.mkdir()
        print("Categoría creada con éxito.")

def eliminar_categoria(categoria):
    # Construir la ruta de la categoría a eliminar
    categoria_directory = Path("C:/Users/jimym/Documents/Udemy/Recetas") / categoria

    # Verificar si la categoría existe y eliminarla si es necesario
    if categoria_directory.exists():
        categoria_directory.rmdir()
        print("Categoría eliminada con éxito.")
    else:
        print("Categoría no encontrada.")

def imprimir_menu():
    print("Menú de Opciones:")
    print("1. Agregar Receta")
    print("2. Buscar Receta")
    print("3. Eliminar Receta")
    print("4. Crear Categoría")
    print("5. Eliminar Categoría")
    print("6. Cerrar Programa")

def mostrar_ruta():
    ruta_carpeta = Path("C:/Users/jimym/Documents/Udemy/Recetas")
    print("La carpeta de recetas se encuentra en:", ruta_carpeta.resolve())

def saludar_usuario(nombre_usuario):
    print(f"¡Bienvenido al programa de recetas, {nombre_usuario}!")
    mostrar_ruta()

base_directory = "Recetas"

nombre_usuario = input("Por favor, ingrese su nombre: ")
saludar_usuario(nombre_usuario)

while True:
    os.system("cls" if os.name == "nt" else "clear")  # Limpiar la consola

    imprimir_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Agregar receta
        categoria = input("Ingrese la categoría de la receta: ")
        nombre_receta = input("Ingrese el nombre de la receta: ")
        ingredientes = input("Ingrese los ingredientes: ")
        pasos = input("Ingrese los pasos de preparación: ")
        agregar_receta(categoria, nombre_receta, ingredientes, pasos)
    elif opcion == "2":
        # Buscar receta
        categoria = input("Ingrese la categoría de la receta: ")
        nombre_receta = input("Ingrese el nombre de la receta a buscar: ")
        buscar_receta(categoria, nombre_receta)
    elif opcion == "3":
        # Eliminar receta
        categoria = input("Ingrese la categoría de la receta: ")
        nombre_receta = input("Ingrese el nombre de la receta a eliminar: ")
        eliminar_receta(categoria, nombre_receta)
    elif opcion == "4":
        # Crear categoría
        nueva_categoria = input("Ingrese el nombre de la nueva categoría: ")
        crear_categoria(nueva_categoria)
    elif opcion == "5":
        # Eliminar categoría
        categoria = input("Ingrese el nombre de la categoría a eliminar: ")
        eliminar_categoria(categoria)
    elif opcion == "6":
        # Cerrar programa
        break
    else:
        print("Opción no válida. Intente de nuevo.")

print("Programa cerrado.")
