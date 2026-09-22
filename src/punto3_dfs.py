"""
Punto 3: Recorridos en Profundidad (DFS)
Lenguajes de Programación y Traducción - Universidad Sergio Arboleda
Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona
"""

from typing import Any, Dict, List, Optional, Tuple
from src.tree_node import TreeNode
from src.punto1_conceptos import construir_arbol_punto1


def dfs_recursivo_preorden(nodo: Optional[TreeNode], visitados: List[Any] = None) -> List[Any]:
    """
    1. Algoritmo DFS recursivo en preorden.
    Visita el nodo actual y recursivamente visita a sus hijos de izquierda a derecha.
    """
    if visitados is None:
        visitados = []
    if nodo is None:
        return visitados

    visitados.append(nodo.value)
    for hijo in nodo.children:
        dfs_recursivo_preorden(hijo, visitados)
    return visitados


def dfs_iterativo_pila(raiz: Optional[TreeNode]) -> List[Any]:
    """
    2. Algoritmo DFS iterativo utilizando una pila explícita (LIFO).
    Para mantener el orden de izquierda a derecha (idéntico a la recursión),
    los hijos se apilan en orden inverso (de derecha a izquierda).
    """
    if raiz is None:
        return []

    visitados = []
    pila = [raiz]

    while pila:
        actual = pila.pop()
        visitados.append(actual.value)
        # Apilar hijos en orden inverso para que el primer hijo salga primero
        for hijo in reversed(actual.children):
            pila.append(hijo)

    return visitados


def dfs_buscar_valor(raiz: Optional[TreeNode], valor_buscado: Any) -> Dict[str, Any]:
    """
    3. Búsqueda de un valor mediante DFS.
    Retorna si se encontró, la secuencia de nodos visitados hasta hallarlo (o hasta agotar el árbol)
    y la cantidad de nodos examinados.
    """
    if raiz is None:
        return {
            "encontrado": False,
            "valor_buscado": valor_buscado,
            "nodos_visitados": [],
            "cantidad_visitados": 0,
            "nodo_encontrado": None
        }

    visitados = []
    encontrado = False
    nodo_encontrado = None

    pila = [raiz]
    while pila:
        actual = pila.pop()
        visitados.append(actual.value)

        if actual.value == valor_buscado:
            encontrado = True
            nodo_encontrado = actual
            break

        for hijo in reversed(actual.children):
            pila.append(hijo)

    return {
        "encontrado": encontrado,
        "valor_buscado": valor_buscado,
        "nodos_visitados": visitados,
        "cantidad_visitados": len(visitados),
        "nodo_encontrado": nodo_encontrado
    }


def dfs_contar_hojas(nodo: Optional[TreeNode]) -> int:
    """
    4. Conteo de nodos hoja mediante DFS recursivo.
    """
    if nodo is None:
        return 0
    if nodo.is_leaf():
        return 1
    return sum(dfs_contar_hojas(hijo) for hijo in nodo.children)


def dfs_calcular_altura(nodo: Optional[TreeNode]) -> int:
    """
    5. Cálculo de la altura del árbol mediante DFS recursivo (en aristas).
    Un nodo hoja tiene altura 0; un árbol vacío tiene altura -1.
    """
    if nodo is None:
        return -1
    if nodo.is_leaf():
        return 0
    return 1 + max(dfs_calcular_altura(hijo) for hijo in nodo.children)


def ejecutar_pruebas_dfs() -> str:
    """
    Ejecuta las pruebas solicitadas en el taller con el árbol del Punto 1:
    - Valor cercano a la raíz ('B')
    - Valor del último nivel ('L')
    - Valor que no exista ('Z')
    """
    raiz, _ = construir_arbol_punto1()
    orden_global = dfs_recursivo_preorden(raiz)
    total_hojas = dfs_contar_hojas(raiz)
    altura_arbol = dfs_calcular_altura(raiz)

    lineas = [
        "=" * 70,
        "PUNTO 3: RECORRIDOS EN PROFUNDIDAD (DFS)",
        "=" * 70,
        "Recorrido DFS Preorden Global:",
        f"  • DFS Recursivo: {' -> '.join(map(str, orden_global))}",
        f"  • DFS Iterativo: {' -> '.join(map(str, dfs_iterativo_pila(raiz)))}",
        f"  • Número total de hojas: {total_hojas} (Hojas: E, J, G, K, L, I)",
        f"  • Altura del árbol (aristas): {altura_arbol} (Niveles: {altura_arbol + 1})",
        "\nEJECUCIÓN DE PRUEBAS DE BÚSQUEDA EXIGIDAS:",
        "-" * 70,
    ]

    casos_prueba = [
        ("Cercano a la raíz", "B"),
        ("Último nivel", "L"),
        ("Inexistente", "Z")
    ]

    for desc, val in casos_prueba:
        res = dfs_buscar_valor(raiz, val)
        lineas.extend([
            f"Caso de prueba: Valor {desc} ('{val}')",
            f"   • Valor buscado:               {res['valor_buscado']}",
            f"   • ¿Encontrado?:                {'SÍ' if res['encontrado'] else 'NO'}",
            f"   • Orden de visita:             {' -> '.join(map(str, res['nodos_visitados']))}",
            f"   • Cantidad de nodos visitados: {res['cantidad_visitados']}",
            f"   • Número de hojas del árbol:   {total_hojas}",
            f"   • Altura del árbol:            {altura_arbol}",
            "-" * 70,
        ])

    # Tabla y análisis de complejidad
    lineas.extend([
        "\nTABLA DE COMPLEJIDAD PARA OPERACIONES CON DFS:",
        "+" + "-" * 26 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+",
        "| Operación con DFS        | Mejor caso     | Peor caso      | Espacio       |",
        "+" + "-" * 26 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+",
        "| Recorrer todo el árbol   | O(N)           | O(N)           | O(h)          |",
        "| Buscar un valor          | O(1) [en raíz] | O(N) [no está] | O(h)          |",
        "| Contar hojas             | O(N)           | O(N)           | O(h)          |",
        "| Calcular la altura       | O(N)           | O(N)           | O(h)          |",
        "+" + "-" * 26 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+",
        "\nANÁLISIS DE CONSUMO DE MEMORIA:",
        "1. Diferencia entre DFS Recursivo y DFS Iterativo:",
        "   • DFS Recursivo utiliza la pila de llamadas del sistema (Call Stack). Cada llamada",
        "     apila un stack frame con variables locales, dirección de retorno y punteros de entorno,",
        "     lo que conlleva mayor sobrecarga por marco y riesgo de RecursionError.",
        "   • DFS Iterativo gestiona una pila explícita en memoria heap (objeto List en Python).",
        "     Solo almacena referencias a los nodos, siendo más eficiente en uso de memoria y libre",
        "     del límite estricto de recursión del intérprete.",
        "2. Árbol Balanceado vs. Árbol Completamente Desbalanceado:",
        "   • En un árbol balanceado de N nodos, la altura h = O(log N). El espacio en pila en",
        "     cualquier momento es O(log N), muy eficiente.",
        "   • En un árbol completamente desbalanceado (degenerado en lista), la altura h = N. El",
        "     consumo de memoria espacial escala a O(N), agotando rápidamente los recursos de pila.",
        "=" * 70,
    ])

    return "\n".join(lineas)


if __name__ == "__main__":
    print(ejecutar_pruebas_dfs())
