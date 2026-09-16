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

def leer_entero(prompt: str) -> int:
    """Lee un número entero del usuario."""
    while True:
        entrada = input(prompt).strip()
        try:
            return int(entrada)
        except ValueError:
            print(f'"{entrada}" no es un número entero válido.')

def leer_real(prompt: str) -> float:
    """Lee un número real del usuario."""
    while True:
        entrada = input(prompt).strip()
        try:
            return float(entrada)
        except ValueError:
            print(f'"{entrada}" no es un número real válido.')

def borrar_consola():
    """Detecta el sistema operativo y borra la consola."""
    if not sys.stdin.isatty():
        return
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    """Simula el comportamiento de pause en cmd."""
    if not sys.stdin.isatty():
        return
    if os.name == "nt":
        os.system("pause")
    else:
        input("Presiona Enter para continuar...")