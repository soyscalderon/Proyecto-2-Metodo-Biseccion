from modules.utils import (
    leer_opcion,
    borrar_consola,
    pausar
)

def run():
    "Metodo principal para ejecutar el menu"
    while True:
        borrar_consola()
        print("=== Método de Biseccions ===\n")
        print("Menú:")
        print("  1) ...")
        print("  2) Salir")
        opcion = leer_opcion("Selecciona una opción (1-8): ", 1, 2)
        try:
            if opcion == 1:
                print("Ejecutando opcion 1")
            elif opcion == 2:
                print("¡Hasta luego!")
                break
        except ValueError as error:
            print(f"Error: {error}\n")
        except (KeyboardInterrupt, EOFError):
            print("\n¡Hasta luego!")
            break
        pausar()