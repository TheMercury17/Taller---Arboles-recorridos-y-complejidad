"""
Ejecutor Maestro del Taller de Árboles, Recorridos y Complejidad Computacional
Lenguajes de Programación y Traducción - Universidad Sergio Arboleda
Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona
"""

import sys
import os

# Asegurar importación de src
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Asegurar codificación UTF-8 en terminales Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from src.punto1_conceptos import reporte_punto1
from src.punto2_expresiones import reporte_punto2
from src.punto3_dfs import ejecutar_pruebas_dfs
from src.punto4_bfs import ejecutar_pruebas_bfs
from src.punto5_sintactico import reporte_punto5
from src.comparacion_conclusion import reporte_comparacion_y_conclusion


def banner():
    print("=" * 80)
    print(" UNIVERSIDAD SERGIO ARBOLEDA - CIENCIAS DE LA COMPUTACIÓN E INTELIGENCIA ARTIFICIAL")
    print(" LENGUAJES DE PROGRAMACIÓN Y TRADUCCIÓN")
    print(" TALLER: ÁRBOLES, RECORRIDOS Y COMPLEJIDAD COMPUTACIONAL")
    print(" GRUPO 5: Andrés Sebastián Coral Vallejo & Carol Arenas Cardona")
    print("=" * 80)


def ejecutar_todo():
    banner()
    print("\n" + reporte_punto1() + "\n")
    print("\n" + reporte_punto2() + "\n")
    print("\n" + ejecutar_pruebas_dfs() + "\n")
    print("\n" + ejecutar_pruebas_bfs() + "\n")
    print("\n" + reporte_punto5() + "\n")
    print("\n" + reporte_comparacion_y_conclusion() + "\n")
    print("=" * 80)
    print(" EJECUCIÓN DEL TALLER COMPLETADA EXITOSAMENTE")
    print("=" * 80)


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "punto1":
            print(reporte_punto1())
        elif arg == "punto2":
            print(reporte_punto2())
        elif arg == "punto3":
            print(ejecutar_pruebas_dfs())
        elif arg == "punto4":
            print(ejecutar_pruebas_bfs())
        elif arg == "punto5":
            print(reporte_punto5())
        elif arg in ["comparacion", "conclusion"]:
            print(reporte_comparacion_y_conclusion())
        else:
            print(f"Opción no reconocida: {arg}. Ejecutando todo el taller...")
            ejecutar_todo()
    else:
        ejecutar_todo()


if __name__ == "__main__":
    main()
