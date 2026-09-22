"""
Punto 4: Recorrido en Anchura (BFS)
Lenguajes de Programación y Traducción - Universidad Sergio Arboleda
Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona
"""

from collections import deque
from typing import Any, Dict, List, Optional, Tuple
from src.tree_node import TreeNode
from src.punto1_conceptos import construir_arbol_punto1


def bfs_recorrido_completo(raiz: Optional[TreeNode]) -> Tuple[List[Any], Dict[int, List[Any]]]:
    """
    Realiza el recorrido en anchura BFS utilizando una cola FIFO.
    Retorna:
    - Lista con el orden general de visita.
    - Diccionario agrupando los nodos por su nivel de profundidad.
    """
    if raiz is None:
        return [], {}

    orden_visita = []
    niveles: Dict[int, List[Any]] = {}

    cola = deque([(raiz, 0)])

    while cola:
        actual, nivel = cola.popleft()
        orden_visita.append(actual.value)

        if nivel not in niveles:
            niveles[nivel] = []
        niveles[nivel].append(actual.value)

        for hijo in actual.children:
            cola.append((hijo, nivel + 1))

    return orden_visita, niveles


def bfs_buscar_valor(raiz: Optional[TreeNode], valor_buscado: Any) -> Dict[str, Any]:
    """
    Búsqueda de un valor mediante BFS con cola FIFO.
    Registra el orden de visita, la cantidad de nodos visitados y el nivel exacto
    donde se ubica el valor (si fue encontrado).
    """
    if raiz is None:
        return {
            "encontrado": False,
            "valor_buscado": valor_buscado,
            "nivel_encontrado": None,
            "nodos_visitados": [],
            "cantidad_visitados": 0
        }

    visitados = []
    encontrado = False
    nivel_encontrado = None

    cola = deque([(raiz, 0)])

    while cola:
        actual, nivel = cola.popleft()
        visitados.append(actual.value)

        if actual.value == valor_buscado:
            encontrado = True
            nivel_encontrado = nivel
            break

        for hijo in actual.children:
            cola.append((hijo, nivel + 1))

    return {
        "encontrado": encontrado,
        "valor_buscado": valor_buscado,
        "nivel_encontrado": nivel_encontrado,
        "nodos_visitados": visitados,
        "cantidad_visitados": len(visitados)
    }


def ejecutar_pruebas_bfs() -> str:
    """
    Ejecuta las pruebas solicitadas en el taller con el formato especificado en la guía:
    - Nivel 0: ...
    - Nivel 1: ...
    - Valor buscado: ...
    - Resultado: encontrado/no encontrado
    - Nivel del valor: ...
    - Nodos visitados: ...
    """
    raiz, _ = construir_arbol_punto1()
    orden_global, niveles = bfs_recorrido_completo(raiz)

    lineas = [
        "=" * 70,
        "PUNTO 4: RECORRIDO EN ANCHURA (BFS)",
        "=" * 70,
        "1. Nodos agrupados por nivel (Estructura jerárquica):"
    ]

    for nivel in sorted(niveles.keys()):
        lineas.append(f"Nivel {nivel}: {', '.join(map(str, niveles[nivel]))}")

    lineas.append(f"\nOrden global de visita BFS: {' -> '.join(map(str, orden_global))}")
    lineas.append("\n" + "-" * 70)
    lineas.append("EJECUCIÓN DE PRUEBAS DE BÚSQUEDA BFS:")
    lineas.append("-" * 70)

    casos_prueba = [
        ("Valor cercano a la raíz", "B"),
        ("Valor del último nivel", "L"),
        ("Valor inexistente", "Z")
    ]

    for desc, val in casos_prueba:
        res = bfs_buscar_valor(raiz, val)
        resultado_str = "encontrado" if res["encontrado"] else "no encontrado"
        nivel_str = str(res["nivel_encontrado"]) if res["encontrado"] else "N/A"

        lineas.extend([
            f"Prueba: {desc} ('{val}')",
            f"Valor buscado:   {res['valor_buscado']}",
            f"Resultado:       {resultado_str}",
            f"Nivel del valor: {nivel_str}",
            f"Nodos visitados: {res['cantidad_visitados']} ({' -> '.join(map(str, res['nodos_visitados']))})",
            "-" * 70
        ])

    lineas.extend([
        "\nRESPUESTAS A LAS PREGUNTAS DE ANÁLISIS DE BFS:",
        "1. ¿Por qué BFS requiere una cola?",
        "   R: Porque una cola sigue la disciplina FIFO (First In, First Out). Esto garantiza que",
        "      todos los nodos pertenecientes al nivel actual (k) se extraigan y procesen antes",
        "      que cualquiera de sus hijos correspondientes al nivel siguiente (k + 1).",
        "\n2. ¿Qué sucedería si se utilizara una pila?",
        "   R: Una pila opera bajo la disciplina LIFO (Last In, First Out). Al apilar los hijos,",
        "      el algoritmo pasaría a explorar inmediatamente el último hijo ingresado hacia el",
        "      fondo del árbol, transformándose automáticamente en un recorrido en profundidad (DFS).",
        "\n3. ¿Cuál es la complejidad temporal de BFS?",
        "   R: O(N), donde N es el número total de nodos. Cada nodo entra y sale de la cola",
        "      exactamente una vez, y cada arista se recorre una sola vez para encolar a los hijos.",
        "\n4. ¿Cuál es su complejidad espacial?",
        "   R: O(W), donde W es el ancho máximo del árbol (el nivel con mayor cantidad de nodos).",
        "      En el peor caso (por ejemplo, un árbol estrella donde la raíz tiene N-1 hijos), la cola",
        "      almacena hasta O(N) nodos simultáneamente.",
        "\n5. ¿Cuál recorrido puede consumir más memoria en un árbol ancho: DFS o BFS?",
        "   R: En un árbol muy ancho, BFS consume significativamente más memoria que DFS. BFS debe",
        "      mantener todos los nodos del nivel más ancho en la cola (O(W) cercano a O(N)), mientras",
        "      que DFS únicamente necesita almacenar el camino de la rama activa en su pila (O(h)),",
        "      la cual es muy reducida en árboles anchos y poco profundos.",
        "\n6. Si se busca el nodo menos profundo que cumpla una condición, ¿cuál resulta más apropiado?",
        "   R: BFS es indudablemente el más apropiado. Dado que BFS expande los nodos en orden estricto",
        "      de niveles crecientes de profundidad (d = 0, 1, 2, ...), el primer nodo encontrado que",
        "      satisfaga la condición tiene garantizada la distancia mínima a la raíz (menor profundidad).",
        "      DFS, en cambio, podría descender por una rama muy profunda e irrelevante antes de notar",
        "      un nodo objetivo que estaba justo al lado de la raíz.",
        "=" * 70
    ])

    return "\n".join(lineas)


if __name__ == "__main__":
    print(ejecutar_pruebas_bfs())
