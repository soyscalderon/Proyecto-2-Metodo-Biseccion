import os
import sys

def leer_opcion(prompt:str, lower:int, upper:int) -> int:
    """Lee un entero dentro del rango cerrado [lower, upper]."""
    while True:
        entrada = input(prompt).strip()
        try:
            valor = int(entrada)
            if lower <= valor <= upper:
                return valor
            print(f"Opción fuera de rango (se esperaba entre {lower} y {upper}).")
        except ValueError:
            print(f'"{entrada}" no es un número entero válido.')

def borrar_consola():
    """
    Detecta el sistema operativo y si esta en TTY.\n
    Luego, borra la consola.
    """
    if not sys.stdin.isatty():
        return
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    """
    Detecta el sistema operativo y si esta en TTY.\n
    Luego, simula el comportamiento de pause en cmd.
    """
    if not sys.stdin.isatty():
        return
    if os.name == "nt":
        os.system("pause")
    else:
        input("Presiona Enter para continuar...")