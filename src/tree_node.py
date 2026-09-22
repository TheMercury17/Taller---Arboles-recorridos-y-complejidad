"""
Módulo de definición del nodo de árbol general (N-ario).
Lenguajes de Programación y Traducción - Universidad Sergio Arboleda
Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona
"""

from typing import Any, List, Optional


class TreeNode:
    """
    Representa un nodo en un árbol general (n-ario).
    Cada nodo almacena un valor y una lista dinámica de referencias a sus hijos.
    """

    def __init__(self, value: Any, is_terminal: bool = False, is_epsilon: bool = False):
        self.value: Any = value
        self.children: List["TreeNode"] = []
        self.parent: Optional["TreeNode"] = None
        
        # Metadatos para análisis sintáctico y numeración
        self.is_terminal: bool = is_terminal
        self.is_epsilon: bool = is_epsilon
        self.creation_order: Optional[int] = None

    def add_child(self, child: "TreeNode") -> "TreeNode":
        """Agrega un hijo al nodo actual y establece la relación de paternidad."""
        child.parent = self
        self.children.append(child)
        return child

    def add_children(self, *children: "TreeNode") -> List["TreeNode"]:
        """Agrega múltiples hijos al nodo actual."""
        for child in children:
            self.add_child(child)
        return list(children)

    def is_leaf(self) -> bool:
        """Determina si el nodo es una hoja (no tiene hijos)."""
        return len(self.children) == 0

    def degree(self) -> int:
        """Retorna el grado del nodo (número de hijos directos)."""
        return len(self.children)

    def __repr__(self) -> str:
        return f"TreeNode({self.value})"

    def display(self, prefix: str = "", is_last: bool = True) -> str:
        """Genera una representación visual en formato árbol ASCII/Unicode."""
        connector = "└── " if is_last else "├── "
        order_tag = f" [#{self.creation_order}]" if self.creation_order is not None else ""
        res = prefix + connector + str(self.value) + order_tag + "\n"
        
        new_prefix = prefix + ("    " if is_last else "│   ")
        for i, child in enumerate(self.children):
            res += child.display(new_prefix, i == len(self.children) - 1)
        return res
