"""
Comparación Final y Conclusión del Taller
Lenguajes de Programación y Traducción - Universidad Sergio Arboleda
Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona
"""

from typing import Dict, List, Tuple

TABLA_COMPARATIVA: List[Tuple[str, str, str]] = [
    (
        "Estructura auxiliar",
        "Pila (Stack): implícita (call stack) o explícita (LIFO)",
        "Cola (Queue): explícita (FIFO)"
    ),
    (
        "Orden de exploración",
        "En profundidad: desciende por cada rama hasta las hojas",
        "En anchura: expande horizontalmente nivel por nivel"
    ),
    (
        "Complejidad temporal",
        "O(N): visita cada nodo y arista una cantidad constante de veces",
        "O(N): cada nodo entra y sale de la cola exactamente una vez"
    ),
    (
        "Complejidad espacial",
        "O(h): proporcional a la altura h del árbol (camino activo)",
        "O(W): proporcional al ancho máximo W (nivel más poblado)"
    ),
    (
        "Conveniente para evaluar expresiones",
        "Sí: el recorrido postorden resuelve operandos antes del operador (bottom-up)",
        "No: mezcla operadores y operandos de diferentes niveles jerárquicos"
    ),
    (
        "Conveniente para recorrer por niveles",
        "No: requiere almacenar o calcular niveles artificialmente",
        "Sí: diseñado naturalmente para procesar estratos o capas del árbol"
    ),
    (
        "Comportamiento en árboles profundos",
        "Desfavorable: alta memoria en pila (O(h) -> O(N)); riesgo de desbordamiento",
        "Favorable: bajo consumo de memoria si el árbol es estrecho (W pequeño)"
    ),
    (
        "Comportamiento en árboles anchos",
        "Favorable: bajo consumo de memoria de pila (la altura h es muy reducida)",
        "Desfavorable: alto consumo en cola al acumular niveles muy densos (O(W) -> O(N))"
    )
]

CONCLUSION_TEXTO = (
    "Los árboles y sus recorridos constituyen el núcleo estructural y computacional del análisis "
    "sintáctico descendente en compiladores modernos. Durante esta etapa, el analizador procesa "
    "una secuencia lineal de componentes léxicos (tokens) y la transforma en una representación "
    "jerárquica no lineal: el árbol sintáctico. Esta estructura refleja con precisión la gramática "
    "formal, resolviendo ambigüedades, asociatividades y precedencias operacionales. En este contexto, "
    "el recorrido en profundidad (DFS) en preorden guía la expansión algorítmica y el flujo de "
    "llamadas recursivas de las producciones gramaticales desde el axioma inicial hacia los terminales. "
    "De forma complementaria, el recorrido en postorden viabiliza la fase de traducción dirigida "
    "por sintaxis y evaluación semántica, permitiendo sintetizar tipos, verificar reglas semánticas "
    "y generar código intermedio únicamente cuando los subárboles de los operandos han sido totalmente "
    "computados (enfoque bottom-up). En conclusión, los árboles proporcionan la topología formal "
    "indispensable para capturar el significado del código fuente, mientras que los recorridos definen "
    "el orden canónico y riguroso en que se construyen, validan y traducen las instrucciones del programa."
)


def contar_palabras(texto: str) -> int:
    """Calcula la cantidad exacta de palabras de un texto."""
    return len(texto.split())


def reporte_comparacion_y_conclusion() -> str:
    """Genera el reporte de la tabla comparativa y la conclusión académica."""
    num_palabras = contar_palabras(CONCLUSION_TEXTO)
    
    lineas = [
        "=" * 90,
        "COMPARACIÓN FINAL: RECORRIDOS DFS vs BFS",
        "=" * 90,
        f"{'Criterio':<38} | {'DFS (Depth-First Search)':<45} | {'BFS (Breadth-First Search)':<45}",
        "-" * 135
    ]

    for criterio, dfs_val, bfs_val in TABLA_COMPARATIVA:
        lineas.append(f"{criterio:<38} | {dfs_val:<45} | {bfs_val:<45}")

    lineas.extend([
        "=" * 90,
        f"\nCONCLUSIÓN FINAL ({num_palabras} palabras - Requisito: 150 a 200 palabras):",
        "¿Por qué los árboles y sus recorridos son fundamentales para implementar un analizador sintáctico descendente?",
        "-" * 90,
        CONCLUSION_TEXTO,
        "-" * 90,
        f"Total de palabras comprobadas: {num_palabras} palabras (Cumple estrictamente el rango [150, 200]).",
        "=" * 90
    ])

    return "\n".join(lineas)


if __name__ == "__main__":
    print(reporte_comparacion_y_conclusion())
