"""
Punto 1: Conceptos y Representación de Árboles
Lenguajes de Programación y Traducción - Universidad Sergio Arboleda
Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona
"""

from typing import Dict, List, Optional, Set, Tuple
from src.tree_node import TreeNode


def construir_arbol_punto1() -> Tuple[TreeNode, Dict[str, TreeNode]]:
    """
    Construye el árbol definido en el Punto 1 según las relaciones padre-hijo:
    A -> B, C, D
    B -> E, F
    C -> G
    D -> H, I
    F -> J
    H -> K, L
    """
    nodos = {letra: TreeNode(letra) for letra in "ABCDEFGHIJKL"}

    nodos["A"].add_children(nodos["B"], nodos["C"], nodos["D"])
    nodos["B"].add_children(nodos["E"], nodos["F"])
    nodos["C"].add_children(nodos["G"])
    nodos["D"].add_children(nodos["H"], nodos["I"])
    nodos["F"].add_children(nodos["J"])
    nodos["H"].add_children(nodos["K"], nodos["L"])

    return nodos["A"], nodos


def obtener_todos_los_nodos(raiz: TreeNode) -> List[TreeNode]:
    """Retorna una lista con todos los nodos del árbol en preorden."""
    lista = []
    pila = [raiz]
    while pila:
        actual = pila.pop(0)
        lista.append(actual)
        pila.extend(actual.children)
    return lista


def obtener_raiz(raiz: TreeNode) -> TreeNode:
    """Retorna el nodo raíz del árbol."""
    return raiz


def obtener_hojas(raiz: TreeNode) -> List[TreeNode]:
    """Retorna la lista de nodos hoja (grado 0)."""
    return [nodo for nodo in obtener_todos_los_nodos(raiz) if nodo.is_leaf()]


def obtener_nodos_internos(raiz: TreeNode) -> List[TreeNode]:
    """Retorna los nodos con al menos un hijo (no hojas)."""
    return [nodo for nodo in obtener_todos_los_nodos(raiz) if not nodo.is_leaf()]


def obtener_padre(nodo: TreeNode) -> Optional[TreeNode]:
    """Retorna el nodo padre directo."""
    return nodo.parent


def obtener_ancestros(nodo: TreeNode) -> List[TreeNode]:
    """Retorna la secuencia de ancestros desde el padre hasta la raíz."""
    ancestros = []
    actual = nodo.parent
    while actual is not None:
        ancestros.append(actual)
        actual = actual.parent
    return ancestros


def obtener_descendientes(nodo: TreeNode) -> List[TreeNode]:
    """Retorna todos los descendientes en el subárbol del nodo dado (excluyendo el nodo)."""
    descendientes = []
    pila = list(nodo.children)
    while pila:
        actual = pila.pop(0)
        descendientes.append(actual)
        pila.extend(actual.children)
    return descendientes


def obtener_hermanos(nodo: TreeNode) -> List[TreeNode]:
    """Retorna los hermanos directos del nodo (mismo padre, excluyéndose a sí mismo)."""
    if nodo.parent is None:
        return []
    return [hijo for hijo in nodo.parent.children if hijo != nodo]


def calcular_profundidad(nodo: TreeNode) -> int:
    """
    Calcula la profundidad del nodo (número de aristas desde la raíz).
    La raíz tiene profundidad 0.
    """
    prof = 0
    actual = nodo.parent
    while actual is not None:
        prof += 1
        actual = actual.parent
    return prof


def calcular_altura(nodo: Optional[TreeNode]) -> int:
    """
    Calcula la altura de un nodo (camino más largo en aristas hacia una hoja descendiente).
    Una hoja tiene altura 0. Si el nodo es None retorna -1.
    """
    if nodo is None:
        return -1
    if nodo.is_leaf():
        return 0
    return 1 + max(calcular_altura(hijo) for hijo in nodo.children)


def analizar_arbol_punto1() -> Dict[str, any]:
    """Ejecuta todos los análisis conceptuales solicitados en el Punto 1."""
    raiz, nodos = construir_arbol_punto1()
    todos = obtener_todos_los_nodos(raiz)

    # Identificación básica
    hojas = [n.value for n in obtener_hojas(raiz)]
    internos = [n.value for n in obtener_nodos_internos(raiz)]
    padre_j = nodos["J"].parent.value if nodos["J"].parent else None
    ancestros_l = [n.value for n in obtener_ancestros(nodos["L"])]
    descendientes_b = [n.value for n in obtener_descendientes(nodos["B"])]
    hermanos_h = [n.value for n in obtener_hermanos(nodos["H"])]

    # Grados
    grados = {n.value: n.degree() for n in todos}
    grado_arbol = max(grados.values())

    # Profundidades y Alturas
    profundidades_clave = {k: calcular_profundidad(nodos[k]) for k in ["A", "F", "J", "L"]}
    altura_total_aristas = calcular_altura(raiz)
    altura_total_niveles = altura_total_aristas + 1

    # Clasificaciones
    # 1. ¿Es binario? Máximo 2 hijos por nodo
    es_binario = all(grado <= 2 for grado in grados.values())
    # 2. ¿Es completo? Todos los niveles llenos salvo posiblemente el último ordenado de izq a der
    es_completo = False  # El nodo A tiene grado 3, y los niveles no están balanceadamente llenos
    # 3. ¿Es balanceado? AVL balance (diferencia de alturas entre subárboles <= 1 en todo nodo)
    def es_balanceado_avl(n: TreeNode) -> bool:
        if n.is_leaf():
            return True
        alturas_hijos = [calcular_altura(h) for h in n.children]
        if max(alturas_hijos) - min(alturas_hijos) > 1:
            return False
        return all(es_balanceado_avl(h) for h in n.children)

    balanceado_avl = es_balanceado_avl(raiz)

    return {
        "raiz": raiz.value,
        "hojas": sorted(hojas),
        "internos": sorted(internos),
        "padre_j": padre_j,
        "ancestros_l": ancestros_l,
        "descendientes_b": sorted(descendientes_b),
        "hermanos_h": hermanos_h,
        "grados": grados,
        "grado_arbol": grado_arbol,
        "profundidades": profundidades_clave,
        "altura_aristas": altura_total_aristas,
        "altura_niveles": altura_total_niveles,
        "es_binario": es_binario,
        "es_completo": es_completo,
        "balanceado_avl": balanceado_avl,
        "diagrama_ascii": raiz.display()
    }


def reporte_punto1() -> str:
    """Genera el reporte en texto estructurado para el Punto 1."""
    data = analizar_arbol_punto1()
    lineas = [
        "=" * 70,
        "PUNTO 1: CONCEPTOS Y REPRESENTACIÓN DE ÁRBOLES",
        "=" * 70,
        "\n1. Representación visual del árbol:",
        data["diagrama_ascii"],
        "2. Identificación de elementos fundamentales:",
        f"   • Raíz: {data['raiz']}",
        f"   • Hojas: {', '.join(data['hojas'])}",
        f"   • Nodos internos: {', '.join(data['internos'])}",
        f"   • Padre del nodo J: {data['padre_j']}",
        f"   • Ancestros del nodo L (hacia la raíz): {' -> '.join(data['ancestros_l'])}",
        f"   • Descendientes del nodo B: {', '.join(data['descendientes_b'])}",
        f"   • Hermanos del nodo H: {', '.join(data['hermanos_h'])}",
        "\n3. Grados, profundidades y altura:",
        f"   • Grados por nodo: {data['grados']}",
        f"   • Grado total del árbol: {data['grado_arbol']} (determinado por el nodo A con 3 hijos)",
        f"   • Profundidades (en aristas / nivel base 0):",
        f"       - Nodo A: {data['profundidades']['A']}",
        f"       - Nodo F: {data['profundidades']['F']}",
        f"       - Nodo J: {data['profundidades']['J']}",
        f"       - Nodo L: {data['profundidades']['L']}",
        f"   • Altura total del árbol: {data['altura_aristas']} aristas ({data['altura_niveles']} niveles de nodos)",
        "\n4. Clasificación estructural y justificaciones:",
        f"   • ¿Es binario?: {'SÍ' if data['es_binario'] else 'NO'}",
        "     Justificación: Para ser binario, cada nodo debe poseer a lo sumo 2 hijos (grado <= 2).",
        "     El nodo raíz A tiene grado 3 (hijos B, C, D), por lo que es un árbol general (3-ario).",
        f"   • ¿Es completo?: {'SÍ' if data['es_completo'] else 'NO'}",
        "     Justificación: Un árbol completo exige que todos los niveles estén llenos al máximo,",
        "     excepto eventualmente el último, el cual debe llenarse estrictamente de izquierda a derecha.",
        "     En este árbol, nodos del nivel 2 como E y G no poseen hijos mientras que F y H sí tienen,",
        "     dejando 'huecos' en la distribución horizontal de la descendencia.",
        f"   • ¿Es balanceado?: {'SÍ (en altura)' if data['balanceado_avl'] else 'NO'}",
        "     Justificación: Bajo la definición formal de balance en altura (tipo AVL), para todo nodo",
        "     la diferencia de alturas entre cualquiera de sus subárboles es <= 1.",
        "     - En la raíz A: subárbol B (altura 2), subárbol C (altura 1), subárbol D (altura 2) -> max diff = 1.",
        "     - En el nodo B: subárbol E (altura 0), subárbol F (altura 1) -> diff = 1.",
        "     - En el nodo D: subárbol H (altura 1), subárbol I (altura 0) -> diff = 1.",
        "     Por tanto, el árbol está balanceado en altura, aunque no sea completo ni simétrico.",
        "\n5. Análisis de Complejidad Temporal:",
        "   Para contar hojas, calcular altura y buscar un valor no existente, el algoritmo debe visitar",
        "   exhaustivamente cada uno de los N nodos y examinar las (N - 1) aristas.",
        "   Complejidad temporal: O(N) (tiempo lineal en el número de nodos).",
        "=" * 70,
    ]
    return "\n".join(lineas)


if __name__ == "__main__":
    print(reporte_punto1())
