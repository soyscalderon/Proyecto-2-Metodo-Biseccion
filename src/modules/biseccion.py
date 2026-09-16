from typing import List, Tuple

from modules.utils import leer_real

def ejecutar_biseccion():
    """Ejecuta el método de bisección con entrada del usuario."""
    print("\n--- Método de Bisección ---\n")
    
    # Leer coeficientes del polinomio
    print("Ingresa los coeficientes del polinomio (de mayor a menor grado)")
    print("Ejemplo: para x² - 3x + 2, ingresa: 1 -3 2")
    entrada = input("Coeficientes: ").strip().split()
    
    try:
        coeficientes = [float(c) for c in entrada]
    except ValueError:
        print("Error: Los coeficientes deben ser números.")
        return
    
    if len(coeficientes) == 0:
        print("Error: Debes ingresar al menos un coeficiente.")
        return
    
    # Leer intervalo [a, b]
    lim_izq = leer_real("Extremo izquierdo (a): ")
    lim_der = leer_real("Extremo derecho (b): ")
    
    if lim_izq >= lim_der:
        print("Error: 'a' debe ser menor que 'b'.")
        return
    
    # Leer tolerancia
    tolerancia = leer_real("Tolerancia (ej. 0.000001): ")
    
    try:
        raiz, iteraciones, historial = biseccion(coeficientes, lim_izq, lim_der, tolerancia)
        
        # Mostrar resultados
        print("\n=== Resultados ===")
        print(f"Raíz encontrada: {raiz}")
        print(f"Iteraciones: {iteraciones}")
        
        # Mostrar tabla de iteraciones
        print("\n--- Tabla de iteraciones ---")
        print(f"{'Iter':>4} {'a':>12} {'b':>12} {'c':>12} {'f(c)':>12}")
        print("-" * 56)
        for i, a_val, b_val, c, fa, fb, fc in historial:
            print(f"{i:>4} {a_val:>12.6f} {b_val:>12.6f} {c:>12.6f} {fc:>12.6f}")
        
    except ValueError as error:
        print(f"Error: {error}")

def biseccion(coeficientes: List[float], lim_izq: float, lim_der: float, 
              tolerancia: float = 1e-6, max_iter: int = 100) -> Tuple[float, int, List[Tuple]]:
    """Implementa el método de bisección para encontrar una raíz.
    
    Args:
        coeficientes: Función continua
        lim_izq: Extremo izquierdo del intervalo
        lim_der: Extremo derecho del intervalo
        tolerancia: Tolerancia (criterio de parada)
        max_iter: Número máximo de iteraciones
    
    Returns:
        Tuple[float, int, List[Tuple]]: Tupla con (raíz, iteraciones, historial)
    
    Raises:
        ValueError: Si f(a) * f(b) >= 0 (no hay cambio de signo)
    """
    
    f_lim_izq = evaluar_polimonio(coeficientes, lim_izq)
    f_lim_der = evaluar_polimonio(coeficientes, lim_der)
    
    # Check if one of the fa and fb is actually a solution
    
    if f_lim_izq * f_lim_der >= 0:
        raise ValueError("No hay cambio de signo en el intervalo [a, b]. No se puede aplicar bisección.")
    
    historial = []
    
    for i in range(0, max_iter):
        punto_medio = (lim_izq + lim_der) / 2
        f_punto_medio = evaluar_polimonio(coeficientes, punto_medio)
        
        historial.append((i+1, lim_izq, lim_der, punto_medio, f_lim_izq, f_lim_der, f_punto_medio))
        
        if abs(f_punto_medio) <= tolerancia or (lim_der - lim_izq) / 2 <= tolerancia:
            return punto_medio, i, historial
        
        if f_lim_izq * f_punto_medio < 0:
            lim_der = punto_medio
            f_lim_der = f_punto_medio
        else:
            lim_izq = punto_medio
            f_lim_izq = f_punto_medio
    
    return punto_medio, max_iter, historial

def evaluar_polimonio(coeficientes: List[float], x: float) -> float:
    """Evalúa un polinomio en un punto x dado sus coeficientes.
    Los coeficientes se ordenan de mayor a menor grado.
    Ejemplo: [1, -3, 2] representa x^2 - 3x + 2
    
    Args:
        coeficientes: Coeficientes del polinomio.
        x: Valor de x a evaluar en el polinomio.
        
    Returns:
        float: Valor de la funcion evaluada en x.
    """
    resultado = 0.0
    n = len(coeficientes)
    for i, c in enumerate(coeficientes):
        grado = n - 1 - i
        resultado += c * (x ** grado)
    return resultado