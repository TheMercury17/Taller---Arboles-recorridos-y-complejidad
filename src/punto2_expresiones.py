"""
Punto 2: Construcción y Evaluación de un Árbol de Expresiones
Lenguajes de Programación y Traducción - Universidad Sergio Arboleda
Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona
"""

from typing import Any, Dict, List, Tuple
from src.tree_node import TreeNode


def construir_arbol_expresion() -> TreeNode:
    """
    Construye manualmente el árbol de sintaxis abstracta para la expresión:
    (a + 3) * (b - 2) + (c / 4)
    
    Respetando la precedencia:
    - Nivel más bajo de precedencia: suma global '+'
    - Nivel medio: multiplicación '*' y división '/'
    - Nivel más alto (agrupados por paréntesis): sumas y restas internas '(a + 3)' y '(b - 2)'
    """
    # Nodos hoja (operandos)
    nodo_a = TreeNode("a")
    nodo_3 = TreeNode(3)
    nodo_b = TreeNode("b")
    nodo_2 = TreeNode(2)
    nodo_c = TreeNode("c")
    nodo_4 = TreeNode(4)

    # Subárbol izquierdo de la multiplicación: (a + 3)
    suma_izq = TreeNode("+")
    suma_izq.add_children(nodo_a, nodo_3)

    # Subárbol derecho de la multiplicación: (b - 2)
    resta_der = TreeNode("-")
    resta_der.add_children(nodo_b, nodo_2)

    # Multiplicación: (a + 3) * (b - 2)
    mult = TreeNode("*")
    mult.add_children(suma_izq, resta_der)

    # Subárbol derecho de la suma global: (c / 4)
    div = TreeNode("/")
    div.add_children(nodo_c, nodo_4)

    # Raíz: suma global
    raiz_mas = TreeNode("+")
    raiz_mas.add_children(mult, div)

    return raiz_mas


def recorrido_preorden(nodo: TreeNode) -> List[str]:
    """Recorrido Preorden: Raíz -> Subárbol Izquierdo -> Subárbol Derecho."""
    resultado = [str(nodo.value)]
    for hijo in nodo.children:
        resultado.extend(recorrido_preorden(hijo))
    return resultado


def recorrido_inorden(nodo: TreeNode, parentesis: bool = True) -> str:
    """Recorrido Inorden: Subárbol Izquierdo -> Raíz -> Subárbol Derecho con parentización."""
    if nodo.is_leaf():
        return str(nodo.value)
    
    izq = recorrido_inorden(nodo.children[0], parentesis)
    der = recorrido_inorden(nodo.children[1], parentesis)
    
    if parentesis:
        return f"({izq} {nodo.value} {der})"
    return f"{izq} {nodo.value} {der}"


def recorrido_postorden(nodo: TreeNode) -> List[str]:
    """Recorrido Postorden: Subárbol Izquierdo -> Subárbol Derecho -> Raíz."""
    resultado = []
    for hijo in nodo.children:
        resultado.extend(recorrido_postorden(hijo))
    resultado.append(str(nodo.value))
    return resultado


def evaluar_arbol_expresion(nodo: TreeNode, variables: Dict[str, float], pasos: List[str] = None) -> float:
    """
    Evalúa la expresión recorriendo el árbol en postorden (bottom-up),
    sustituyendo los valores de las variables en los nodos hoja y resolviendo
    las operaciones en los nodos internos.
    """
    if pasos is None:
        pasos = []

    # Caso base: hoja (operando)
    if nodo.is_leaf():
        if isinstance(nodo.value, (int, float)):
            return float(nodo.value)
        val = variables.get(str(nodo.value))
        if val is None:
            raise ValueError(f"Variable no definida: {nodo.value}")
        return float(val)

    # Caso recursivo: nodo interno (operador)
    val_izq = evaluar_arbol_expresion(nodo.children[0], variables, pasos)
    val_der = evaluar_arbol_expresion(nodo.children[1], variables, pasos)
    op = str(nodo.value)

    if op == "+":
        res = val_izq + val_der
    elif op == "-":
        res = val_izq - val_der
    elif op == "*":
        res = val_izq * val_der
    elif op == "/":
        if val_der == 0:
            raise ZeroDivisionError("División por cero en el árbol de expresión.")
        res = val_izq / val_der
    else:
        raise ValueError(f"Operador desconocido: {op}")

    pasos.append(f"Evaluando: {val_izq} {op} {val_der} = {res}")
    return res


def reporte_punto2() -> str:
    """Genera el reporte conceptual y práctico completo del Punto 2."""
    arbol = construir_arbol_expresion()
    
    pre = " ".join(recorrido_preorden(arbol))
    ino = recorrido_inorden(arbol, parentesis=True)
    post = " ".join(recorrido_postorden(arbol))

    variables = {"a": 5.0, "b": 8.0, "c": 12.0}
    pasos_eval = []
    resultado_num = evaluar_arbol_expresion(arbol, variables, pasos_eval)

    lineas = [
        "=" * 70,
        "PUNTO 2: CONSTRUCCIÓN Y EVALUACIÓN DE UN ÁRBOL DE EXPRESIONES",
        "=" * 70,
        "Expresión algebraica: (a + 3) * (b - 2) + c / 4",
        "\n1. Operandos y Operadores identificados:",
        "   • Operandos: Variables [a, b, c] y Constantes numéricas [3, 2, 4]",
        "   • Operadores: Suma (+), Multiplicación (*), Resta (-), División (/)",
        "   • Símbolos de agrupación: Paréntesis (...) que alteran la precedencia natural",
        "\n2. Estructura visual del Árbol de Expresión:",
        arbol.display(),
        "3. Recorridos del Árbol:",
        f"   • Preorden (Prefija / Notación Polaca):     {pre}",
        f"   • Inorden  (Infija parentizada):           {ino}",
        f"   • Postorden (Postfija / Polaca Inversa):   {post}",
        "\n4. Correspondencia con Notaciones Formales:",
        "   • Preorden  -> Notación Prefija (símbolo operador precede a sus operandos)",
        "   • Inorden   -> Notación Infija (operador entre sus dos operandos)",
        "   • Postorden -> Notación Postfija (operador sucede inmediatamente a sus operandos)",
        f"\n5. Evaluación paso a paso con a = {variables['a']}, b = {variables['b']}, c = {variables['c']}:",
    ]
    for i, paso in enumerate(pasos_eval, 1):
        lineas.append(f"   Paso {i}: {paso}")
    lineas.extend([
        f"\n   -> RESULTADO FINAL DE LA EVALUACIÓN: {resultado_num}",
        "\n6. Respuestas a las Preguntas de Análisis:",
        "   • P1: ¿Por qué la evaluación de una expresión se realiza en postorden?",
        "     R: Porque en cualquier operación binaria es imprescindible disponer primero del",
        "        valor resuelto de ambos operandos (subárboles izquierdo y derecho) antes de poder",
        "        aplicar el operador. El recorrido postorden (Izquierda, Derecha, Raíz) materializa",
        "        exactamente el paradigma bottom-up (de abajo hacia arriba) y coincide de forma",
        "        isomorfa con el funcionamiento de las máquinas basadas en pila (Stack Machines / RPN).",
        "   • P2: ¿Cuál es la complejidad temporal de evaluar el árbol?",
        "     R: O(N), donde N es el número total de nodos (en este caso N = 11). Cada nodo se visita",
        "        un número constante de veces y cada cálculo aritmético primario se ejecuta en O(1).",
        "   • P3: ¿Cuál es la complejidad espacial del recorrido recursivo en función de h?",
        "     R: O(h), donde h es la altura del árbol. La memoria requerida proviene de la pila de",
        "        ejecución (call stack) del lenguaje, almacenando a lo sumo h marcos activos simultáneamente.",
        "   • P4: ¿Qué ocurre con el consumo de memoria si el árbol está completamente desbalanceado?",
        "     R: Si el árbol degenera en una estructura lineal tipo lista enlazada (peor caso), la",
        "        altura pasa a ser h = N. En consecuencia, el consumo de memoria espacial en la pila",
        "        se degrada de O(log N) a O(N), consumiendo drásticamente más memoria e induciendo el",
        "        riesgo inminente de un desbordamiento de pila (Stack Overflow / RecursionError).",
        "=" * 70,
    ])
    return "\n".join(lineas)


if __name__ == "__main__":
    print(reporte_punto2())
