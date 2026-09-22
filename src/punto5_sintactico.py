"""
Punto 5: Aplicación al Análisis Sintáctico Descendente
Lenguajes de Programación y Traducción - Universidad Sergio Arboleda
Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona
"""

from collections import deque
from typing import Any, Dict, List, Optional, Tuple
from src.tree_node import TreeNode


def construir_arbol_sintactico_descendente() -> Tuple[TreeNode, List[Tuple[int, str, str]]]:
    """
    Simula paso a paso la construcción del árbol sintáctico por un analizador descendente
    (Recursive Descent Parser / LL(1)) para la cadena:
    id + id * id

    Gramática:
    E  -> T E'
    E' -> + T E' | ε
    T  -> F T'
    T' -> * F T' | ε
    F  -> ( E ) | id

    Retorna la raíz del árbol con cada nodo etiquetado con su orden de creación (1-indexed)
    y un registro detallado de los pasos de derivación.
    """
    contador_orden = 0
    pasos_creacion: List[Tuple[int, str, str]] = []

    def crear_nodo(simbolo: str, tipo: str, accion: str) -> TreeNode:
        nonlocal contador_orden
        contador_orden += 1
        es_term = (tipo == "terminal")
        es_eps = (simbolo == "ε")
        nodo = TreeNode(simbolo, is_terminal=es_term, is_epsilon=es_eps)
        nodo.creation_order = contador_orden
        pasos_creacion.append((contador_orden, simbolo, accion))
        return nodo

    # 1. Inicio en símbolo inicial E
    nodo_E = crear_nodo("E", "no_terminal", "Llamada a parse_E() -> Aplica E -> T E'")

    # Subárbol T
    nodo_T1 = crear_nodo("T", "no_terminal", "Llamada a parse_T() -> Aplica T -> F T'")
    nodo_F1 = crear_nodo("F", "no_terminal", "Llamada a parse_F() -> Aplica F -> id")
    nodo_id1 = crear_nodo("id", "terminal", "Match terminal 'id' (primer operando)")
    nodo_F1.add_child(nodo_id1)

    nodo_Tp1 = crear_nodo("T'", "no_terminal", "Llamada a parse_T'() -> Siguiente token es '+', aplica T' -> ε")
    nodo_eps1 = crear_nodo("ε", "terminal", "Expansión producción vacía ε")
    nodo_Tp1.add_child(nodo_eps1)

    nodo_T1.add_children(nodo_F1, nodo_Tp1)

    # Subárbol E'
    nodo_Ep1 = crear_nodo("E'", "no_terminal", "Llamada a parse_E'() -> Siguiente token es '+', aplica E' -> + T E'")
    nodo_mas = crear_nodo("+", "terminal", "Match terminal '+'")

    nodo_T2 = crear_nodo("T", "no_terminal", "Llamada a parse_T() -> Aplica T -> F T'")
    nodo_F2 = crear_nodo("F", "no_terminal", "Llamada a parse_F() -> Aplica F -> id")
    nodo_id2 = crear_nodo("id", "terminal", "Match terminal 'id' (segundo operando)")
    nodo_F2.add_child(nodo_id2)

    nodo_Tp2 = crear_nodo("T'", "no_terminal", "Llamada a parse_T'() -> Siguiente token es '*', aplica T' -> * F T'")
    nodo_por = crear_nodo("*", "terminal", "Match terminal '*'")

    nodo_F3 = crear_nodo("F", "no_terminal", "Llamada a parse_F() -> Aplica F -> id")
    nodo_id3 = crear_nodo("id", "terminal", "Match terminal 'id' (tercer operando)")
    nodo_F3.add_child(nodo_id3)

    nodo_Tp3 = crear_nodo("T'", "no_terminal", "Llamada a parse_T'() -> Fin de cadena $, aplica T' -> ε")
    nodo_eps2 = crear_nodo("ε", "terminal", "Expansión producción vacía ε")
    nodo_Tp3.add_child(nodo_eps2)

    nodo_Tp2.add_children(nodo_por, nodo_F3, nodo_Tp3)
    nodo_T2.add_children(nodo_F2, nodo_Tp2)

    nodo_Ep2 = crear_nodo("E'", "no_terminal", "Llamada a parse_E'() -> Fin de cadena $, aplica E' -> ε")
    nodo_eps3 = crear_nodo("ε", "terminal", "Expansión producción vacía ε")
    nodo_Ep2.add_child(nodo_eps3)

    nodo_Ep1.add_children(nodo_mas, nodo_T2, nodo_Ep2)
    nodo_E.add_children(nodo_T1, nodo_Ep1)

    return nodo_E, pasos_creacion


def dfs_preorden_sintactico(nodo: TreeNode) -> List[str]:
    """Recorrido DFS Preorden: Raíz -> Hijos (izq a der)."""
    resultado = [f"{nodo.value}(#{nodo.creation_order})"]
    for hijo in nodo.children:
        resultado.extend(dfs_preorden_sintactico(hijo))
    return resultado


def dfs_postorden_sintactico(nodo: TreeNode) -> List[str]:
    """Recorrido DFS Postorden: Hijos (izq a der) -> Raíz."""
    resultado = []
    for hijo in nodo.children:
        resultado.extend(dfs_postorden_sintactico(hijo))
    resultado.append(f"{nodo.value}(#{nodo.creation_order})")
    return resultado


def bfs_sintactico(raiz: TreeNode) -> List[str]:
    """Recorrido BFS por niveles."""
    resultado = []
    cola = deque([raiz])
    while cola:
        actual = cola.popleft()
        resultado.append(f"{actual.value}(#{actual.creation_order})")
        for hijo in actual.children:
            cola.append(hijo)
    return resultado


def analizar_metricas_arbol_sintactico(raiz: Optional[TreeNode]) -> Dict[str, Any]:
    """
    7. Algoritmo propuesto que cuenta recursivamente:
       - Nodos terminales (excluyendo ε)
       - Producciones vacías (ε)
       - Nodos no terminales
       - Altura del árbol sintáctico (en aristas)
    """
    conteo = {
        "nodos_terminales": 0,
        "nodos_no_terminales": 0,
        "producciones_vacias_epsilon": 0,
        "total_nodos": 0
    }

    def recorrer(nodo: Optional[TreeNode]):
        if nodo is None:
            return
        conteo["total_nodos"] += 1
        if nodo.is_epsilon:
            conteo["producciones_vacias_epsilon"] += 1
        elif nodo.is_terminal:
            conteo["nodos_terminales"] += 1
        else:
            conteo["nodos_no_terminales"] += 1

        for hijo in nodo.children:
            recorrer(hijo)

    def altura(nodo: Optional[TreeNode]) -> int:
        if nodo is None:
            return -1
        if nodo.is_leaf():
            return 0
        return 1 + max(altura(hijo) for hijo in nodo.children)

    recorrer(raiz)
    conteo["altura_aristas"] = altura(raiz)
    conteo["altura_niveles"] = conteo["altura_aristas"] + 1
    return conteo


def reporte_punto5() -> str:
    """Genera el reporte conceptual y técnico detallado para el Punto 5."""
    arbol, pasos = construir_arbol_sintactico_descendente()
    pre = dfs_preorden_sintactico(arbol)
    post = dfs_postorden_sintactico(arbol)
    anchura = bfs_sintactico(arbol)
    metricas = analizar_metricas_arbol_sintactico(arbol)

    lineas = [
        "=" * 70,
        "PUNTO 5: APLICACIÓN AL ANÁLISIS SINTÁCTICO DESCENDENTE",
        "=" * 70,
        "Cadena de entrada analizada: id + id * id",
        "Gramática formal LL(1):",
        "   E  -> T E'",
        "   E' -> + T E' | ε",
        "   T  -> F T'",
        "   T' -> * F T' | ε",
        "   F  -> ( E ) | id",
        "\n1 y 2. Orden de creación de los nodos por el analizador descendente:",
    ]

    for orden, simbolo, accion in pasos:
        lineas.append(f"   [{orden:02d}] Símbolo: {simbolo:<3} | Acción: {accion}")

    lineas.extend([
        "\nDiagrama del Árbol Sintáctico (con etiquetas de orden de creación [#n]):",
        arbol.display(),
        "3. Recorridos ejecutados sobre el árbol sintáctico:",
        f"   • DFS Preorden:  {' -> '.join(pre)}",
        f"   • DFS Postorden: {' -> '.join(post)}",
        f"   • BFS (Niveles): {' -> '.join(anchura)}",
        "\n4. Información proporcionada por cada recorrido en compilación:",
        "   • DFS Preorden:",
        "     Refleja el orden exacto de activación y derivación top-down del analizador",
        "     sintáctico. Corresponde al flujo de llamadas recursivas de cada procedimiento.",
        "   • DFS Postorden:",
        "     Modela la síntesis de atributos y la evaluación semántica (bottom-up). Es la fase",
        "     donde se sintetizan tipos, se generan cuádruplos/código intermedio y se verifica",
        "     la consistencia semántica una vez resueltos todos los hijos.",
        "   • BFS (Anchura):",
        "     Estratifica la estructura gramatical por niveles de derivación o distancia jerárquica",
        "     respecto al axioma inicial E. Es útil para visualizaciones e inspecciones por capas.",
        "\n5. Comparación entre el orden de creación y el recorrido en Preorden:",
        "   -> ¡Coincidencia Exacta (Isomorfismo Total)! <-",
        "   En un analizador descendente recursivo (LL), cada subrutina crea primero el nodo padre",
        "   asociado al no terminal antes de llamar a las subrutinas de sus símbolos del lado derecho.",
        "   Por definición, visitar la raíz antes de descender recursivamente a los subárboles de",
        "   izquierda a derecha es exactamente la definición de un recorrido en PREORDEN.",
        "\n6. Representación de la Precedencia del operador '*' sobre '+':",
        "   En el árbol sintáctico, la subexpresión 'id * id' se encuentra alojada en el subárbol T',",
        "   el cual es descendiente de T, ubicado a mayor profundidad (nivel 4-5) que el operador '+'",
        "   ubicado en E' (nivel 2).",
        "   Dado que la reducción y síntesis semántica se efectúa de abajo hacia arriba (bottom-up),",
        "   el operador '*' debe ser evaluado obligatoriamente antes de que su resultado pueda sumarse",
        "   a través del '+'. La mayor profundidad en la gramática equivale a mayor precedencia.",
        "\n7. Métricas y Conteo del Árbol Sintáctico (Algoritmo propuesto):",
        f"   • Nodos terminales (id, +, *):         {metricas['nodos_terminales']}",
        f"   • Producciones vacías (ε):             {metricas['producciones_vacias_epsilon']}",
        f"   • Nodos no terminales (E, E', T, T', F): {metricas['nodos_no_terminales']}",
        f"   • Total absoluto de nodos:             {metricas['total_nodos']}",
        f"   • Altura del árbol sintáctico:         {metricas['altura_aristas']} aristas ({metricas['altura_niveles']} niveles)",
        "=" * 70,
    ])

    return "\n".join(lineas)


if __name__ == "__main__":
    print(reporte_punto5())
