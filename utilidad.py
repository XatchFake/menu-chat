import random
import json

# Diccionario para almacenar las películas
peliculas = {}

# Función para agregar una película
def agregar_pelicula():
    codigo = random.randint(1, 1000)
    while codigo in peliculas:
        codigo = random.randint(1, 1000)
    nombre = input("Ingrese el nombre de la película: ")
    año = input("Ingrese el año de la película: ")
    categoria = input("Ingrese la categoría de la película: ")
    actores = input("Ingrese los actores (separados por comas): ").split(',')
    director = input("Ingrese el director de la película: ")
    
    peliculas[codigo] = {
        "nombre": nombre,
        "año": año,
        "categoria": categoria,
        "actores": actores,
        "director": director
    }

    print(f"Película '{nombre}' agregada con código {codigo}.")


def listar_peliculas():
    if not peliculas:
        print("No hay películas en la base de datos.")
    else:
        for codigo, info in peliculas.items():
            print(f"Código: {codigo}")
            print(f"  Nombre: {info['nombre']}")
            print(f"  Año: {info['año']}")
            print(f"  Categoría: {info['categoria']}")
            print(f"  Actores: {', '.join(info['actores'])}")
            print(f"  Director: {info['director']}")
            print("")


def buscar_peliculas():
    categoria = input("Ingrese la categoría de la película que desea buscar: ")
    found = False
    for codigo, info in peliculas.items():
        if info['categoria'].lower() == categoria.lower():
            print("")
            print(f"  Código: {codigo}")
            print(f"  Nombre: {info['nombre']}")
            print(f"  Año: {info['año']}")
            print(f"  Categoría: {info['categoria']}")
            print(f"  Actores: {', '.join(info['actores'])}")
            print(f"  Director: {info['director']}")
            print("")
            found = True
    if not found:
        print(f"No se encontraron películas en la categoría '{categoria}'.")


def sumar_años_peliculas():
    if not peliculas:
        print("No hay películas en la base de datos.")
    else:
        total = sum(int(info['año']) for info in peliculas.values())
        print(f"La suma de todos los años de las películas es: {total}")        


# Función principal del menú
def menu():
    while True:
        print("\n--- Menú de Gestión de Películas ---")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Buscar Películas por Categoría")
        print("4. Sumar Años de Películas")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                agregar_pelicula()
            elif opcion == 2:
                listar_peliculas()
            elif opcion == 3:
                buscar_peliculas()
            elif opcion == 4:
                sumar_años_peliculas()
            elif opcion == 5:
                print("Guardando películas en 'archivo.txt'...")
                with open("archivo.txt", "a") as file:
                    json.dump(peliculas, file, indent=4)
                print("Películas guardadas en 'archivo.txt'. ¡Adiós!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")



