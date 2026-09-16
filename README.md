# Proyecto 2 - Metodo de Biseccion

Implementacion del metodo de biseccion para encontrar raices de polinomios, desarrollado como proyecto del curso de Analisis Numerico (5to semestre).

## Descripcion

El metodo de biseccion es un algoritmo de busqueda de raices que funciona subdividiendo repetidamente un intervalo `[a, b]` y seleccionando el sub-intervalo donde la funcion cambia de signo. El algoritmo garantiza convergencia para funciones continuas que cambian de signo en el intervalo dado.

## Requisitos

- Python 3.8 o superior (desarrollado en Python 3.14)
- No requiere dependencias externas

## Ejecucion

```bash
# Opcion 1: usar el script de ejecucion
bash exec.sh

# Opcion 2: ejecutar directamente
python3 src/main.py
```

## Estructura del proyecto

```
.
├── exec.sh                         # Script de ejecucion
├── generate_flowcharts.py          # Generador de diagramas de flujo
├── src/
│   ├── main.py                     # Punto de entrada
│   └── modules/
│       ├── __init__.py             # Paquete
│       ├── biseccion.py            # Algoritmo de biseccion
│       ├── menu.py                 # Menu interactivo
│       └── utils.py                # Funciones de utilidad
└── diagramas/                      # Diagramas de flujo generados
```

## Uso

Al ejecutar el programa se muestra un menu interactivo con las siguientes opciones:

1. **Calcular raiz de un polinomio** - Solicita:
   - Coeficientes del polinomio (de mayor a menor grado, ej: `1 -3 2` para x^2 - 3x + 2)
   - Limite izquierdo del intervalo `[a, b]`
   - Limite derecho del intervalo `[a, b]`
   - Valor de tolerancia

2. **Salir** - Termina el programa

El resultado muestra una tabla de iteraciones con las columnas: Iteracion, a, b, c (punto medio) y f(c).

## Funcionamiento del algoritmo

1. Se evalua `f(a)` y `f(b)` y se verifica que `f(a) * f(b) < 0` (cambio de signo)
2. Se calcula el punto medio `c = (a + b) / 2`
3. Si `|f(c)| <= tolerancia` o `(b - a) / 2 <= tolerancia`, se detiene
4. Si `f(a) * f(c) < 0`, la raiz esta en `[a, c]`; de lo contrario, esta en `[c, b]`
5. Se repite desde el paso 2

## Autores

Desarrollado como proyecto del curso de Analisis Numerico.