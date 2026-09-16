from modules.utils import (
    leer_opcion,
    borrar_consola,
    pausar,
)
from modules.biseccion import ejecutar_biseccion


def run():
    """Método principal para ejecutar el menú."""
    while True:
        borrar_consola()
        print("=== Método de Bisección ===\n")
        print("Menú:")
        print("  1) Calcular raíz de polinomio")
        print("  2) Salir")
        
        opcion = leer_opcion("Selecciona una opción (1-2): ", 1, 2)
        
        try:
            if opcion == 1:
                ejecutar_biseccion()
            elif opcion == 2:
                print("¡Hasta luego!")
                break
        except ValueError as error:
            print(f"Error: {error}\n")
        except (KeyboardInterrupt, EOFError):
            print("\n¡Hasta luego!")
            break
        
        pausar()