"""
Suite de Pruebas Automatizadas (Unit Tests) para el Taller
Lenguajes de Programación y Traducción - Universidad Sergio Arboleda
Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona
"""

import unittest
from src.tree_node import TreeNode
from src.punto1_conceptos import (
    construir_arbol_punto1,
    analizar_arbol_punto1,
    obtener_ancestros,
    obtener_descendientes,
    obtener_hermanos,
    calcular_profundidad,
    calcular_altura
)
from src.punto2_expresiones import (
    construir_arbol_expresion,
    recorrido_preorden,
    recorrido_inorden,
    recorrido_postorden,
    evaluar_arbol_expresion
)
from src.punto3_dfs import (
    dfs_recursivo_preorden,
    dfs_iterativo_pila,
    dfs_buscar_valor,
    dfs_contar_hojas,
    dfs_calcular_altura
)
from src.punto4_bfs import (
    bfs_recorrido_completo,
    bfs_buscar_valor
)
from src.punto5_sintactico import (
    construir_arbol_sintactico_descendente,
    dfs_preorden_sintactico,
    dfs_postorden_sintactico,
    bfs_sintactico,
    analizar_metricas_arbol_sintactico
)
from src.comparacion_conclusion import (
    TABLA_COMPARATIVA,
    CONCLUSION_TEXTO,
    contar_palabras
)


class TestPunto1(unittest.TestCase):
    """Pruebas para el Punto 1: Propiedades del árbol general."""

    def setUp(self):
        self.raiz, self.nodos = construir_arbol_punto1()
        self.data = analizar_arbol_punto1()

    def test_identificacion_elementos(self):
        self.assertEqual(self.data["raiz"], "A")
        self.assertEqual(self.data["hojas"], ["E", "G", "I", "J", "K", "L"])
        self.assertEqual(self.data["internos"], ["A", "B", "C", "D", "F", "H"])
        self.assertEqual(self.data["padre_j"], "F")
        self.assertEqual(self.data["ancestros_l"], ["H", "D", "A"])
        self.assertEqual(self.data["descendientes_b"], ["E", "F", "J"])
        self.assertEqual(self.data["hermanos_h"], ["I"])

    def test_grados_profundidades_altura(self):
        self.assertEqual(self.data["grado_arbol"], 3)
        self.assertEqual(self.data["grados"]["A"], 3)
        self.assertEqual(self.data["grados"]["B"], 2)
        self.assertEqual(self.data["grados"]["C"], 1)
        self.assertEqual(self.data["grados"]["E"], 0)

        self.assertEqual(self.data["profundidades"]["A"], 0)
        self.assertEqual(self.data["profundidades"]["F"], 2)
        self.assertEqual(self.data["profundidades"]["J"], 3)
        self.assertEqual(self.data["profundidades"]["L"], 3)

        self.assertEqual(self.data["altura_aristas"], 3)
        self.assertEqual(self.data["altura_niveles"], 4)

    def test_clasificaciones(self):
        self.assertFalse(self.data["es_binario"])
        self.assertFalse(self.data["es_completo"])
        self.assertTrue(self.data["balanceado_avl"])


class TestPunto2(unittest.TestCase):
    """Pruebas para el Punto 2: Árbol de expresiones y recorridos."""

    def setUp(self):
        self.arbol = construir_arbol_expresion()

    def test_recorridos(self):
        pre = recorrido_preorden(self.arbol)
        self.assertEqual(pre, ["+", "*", "+", "a", "3", "-", "b", "2", "/", "c", "4"])

        ino = recorrido_inorden(self.arbol)
        self.assertEqual(ino, "(((a + 3) * (b - 2)) + (c / 4))")

        post = recorrido_postorden(self.arbol)
        self.assertEqual(post, ["a", "3", "+", "b", "2", "-", "*", "c", "4", "/", "+"])

    def test_evaluacion_numerica(self):
        variables = {"a": 5.0, "b": 8.0, "c": 12.0}
        resultado = evaluar_arbol_expresion(self.arbol, variables)
        self.assertEqual(resultado, 51.0)


class TestPunto3(unittest.TestCase):
    """Pruebas para el Punto 3: Algoritmos DFS."""

    def setUp(self):
        self.raiz, _ = construir_arbol_punto1()

    def test_dfs_recursivo_vs_iterativo(self):
        rec = dfs_recursivo_preorden(self.raiz)
        it = dfs_iterativo_pila(self.raiz)
        esperado = ["A", "B", "E", "F", "J", "C", "G", "D", "H", "K", "L", "I"]
        self.assertEqual(rec, esperado)
        self.assertEqual(it, esperado)

    def test_dfs_hojas_y_altura(self):
        self.assertEqual(dfs_contar_hojas(self.raiz), 6)
        self.assertEqual(dfs_calcular_altura(self.raiz), 3)

    def test_dfs_busqueda(self):
        # 1. Cercano a la raíz
        res_b = dfs_buscar_valor(self.raiz, "B")
        self.assertTrue(res_b["encontrado"])
        self.assertEqual(res_b["nodos_visitados"], ["A", "B"])
        self.assertEqual(res_b["cantidad_visitados"], 2)

        # 2. Último nivel
        res_l = dfs_buscar_valor(self.raiz, "L")
        self.assertTrue(res_l["encontrado"])
        self.assertIn("L", res_l["nodos_visitados"])

        # 3. Inexistente
        res_z = dfs_buscar_valor(self.raiz, "Z")
        self.assertFalse(res_z["encontrado"])
        self.assertEqual(res_z["cantidad_visitados"], 12)


class TestPunto4(unittest.TestCase):
    """Pruebas para el Punto 4: Algoritmos BFS."""

    def setUp(self):
        self.raiz, _ = construir_arbol_punto1()

    def test_bfs_orden_y_niveles(self):
        orden, niveles = bfs_recorrido_completo(self.raiz)
        esperado_orden = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        self.assertEqual(orden, esperado_orden)

        self.assertEqual(niveles[0], ["A"])
        self.assertEqual(niveles[1], ["B", "C", "D"])
        self.assertEqual(niveles[2], ["E", "F", "G", "H", "I"])
        self.assertEqual(niveles[3], ["J", "K", "L"])

    def test_bfs_busqueda(self):
        # 1. Cercano a raíz
        res_b = bfs_buscar_valor(self.raiz, "B")
        self.assertTrue(res_b["encontrado"])
        self.assertEqual(res_b["nivel_encontrado"], 1)

        # 2. Último nivel
        res_l = bfs_buscar_valor(self.raiz, "L")
        self.assertTrue(res_l["encontrado"])
        self.assertEqual(res_l["nivel_encontrado"], 3)

        # 3. Inexistente
        res_z = bfs_buscar_valor(self.raiz, "Z")
        self.assertFalse(res_z["encontrado"])
        self.assertIsNone(res_z["nivel_encontrado"])
        self.assertEqual(res_z["cantidad_visitados"], 12)


class TestPunto5(unittest.TestCase):
    """Pruebas para el Punto 5: Árbol sintáctico descendente."""

    def setUp(self):
        self.arbol, self.pasos = construir_arbol_sintactico_descendente()
        self.metricas = analizar_metricas_arbol_sintactico(self.arbol)

    def test_metricas_arbol_sintactico(self):
        self.assertEqual(self.metricas["total_nodos"], 19)
        self.assertEqual(self.metricas["nodos_terminales"], 5)  # id, +, id, *, id
        self.assertEqual(self.metricas["producciones_vacias_epsilon"], 3)  # 3 epsilons
        self.assertEqual(self.metricas["nodos_no_terminales"], 11)
        self.assertEqual(self.metricas["altura_aristas"], 5)

    def test_correspondencia_creacion_preorden(self):
        # Comprueba que el orden de creación coincida 1 a 1 con el preorden
        pre = dfs_preorden_sintactico(self.arbol)
        orden_creacion_preorden = [int(token.split("#")[1][:-1]) for token in pre]
        self.assertEqual(orden_creacion_preorden, list(range(1, 20)))


class TestComparacionConclusion(unittest.TestCase):
    """Pruebas para los entregables de conclusión y comparación."""

    def test_conteo_palabras_conclusion(self):
        palabras = contar_palabras(CONCLUSION_TEXTO)
        self.assertGreaterEqual(palabras, 150, "La conclusión debe tener al menos 150 palabras")
        self.assertLessEqual(palabras, 200, "La conclusión no debe exceder las 200 palabras")

    def test_tabla_comparativa_criterios(self):
        self.assertEqual(len(TABLA_COMPARATIVA), 8)


if __name__ == "__main__":
    unittest.main()
