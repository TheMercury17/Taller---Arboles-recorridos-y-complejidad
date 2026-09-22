# Makefile - Taller de Árboles, Recorridos y Complejidad Computacional
# Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona
# Lenguajes de Programación y Traducción - Universidad Sergio Arboleda

PYTHON ?= python3

.PHONY: help all test run punto1 punto2 punto3 punto4 punto5 comparacion clean venv

help:
	@echo "=========================================================================="
	@echo " Taller: Árboles, Recorridos y Complejidad Computacional - Grupo 5"
	@echo "=========================================================================="
	@echo "Comandos disponibles:"
	@echo "  make test        - Ejecuta la suite de pruebas unitarias automatizadas"
	@echo "  make run         - Ejecuta la demostración completa del taller (main.py)"
	@echo "  make punto1      - Ejecuta el análisis y visualización del Punto 1"
	@echo "  make punto2      - Ejecuta el árbol de expresión y evaluación del Punto 2"
	@echo "  make punto3      - Ejecuta los algoritmos y pruebas DFS del Punto 3"
	@echo "  make punto4      - Ejecuta los algoritmos y pruebas BFS del Punto 4"
	@echo "  make punto5      - Ejecuta el análisis sintáctico LL(1) del Punto 5"
	@echo "  make comparacion - Muestra la tabla comparativa DFS vs BFS y conclusión"
	@echo "  make venv        - Crea un entorno virtual (.venv) en Linux"
	@echo "  make clean       - Elimina archivos temporales y cachés de Python"
	@echo "=========================================================================="

all: test run

test:
	$(PYTHON) -m unittest discover tests -v

run:
	$(PYTHON) main.py

punto1:
	$(PYTHON) main.py punto1

punto2:
	$(PYTHON) main.py punto2

punto3:
	$(PYTHON) main.py punto3

punto4:
	$(PYTHON) main.py punto4

punto5:
	$(PYTHON) main.py punto5

comparacion:
	$(PYTHON) main.py comparacion

venv:
	$(PYTHON) -m venv .venv
	@echo "Entorno virtual creado en .venv. Actívalo con: source .venv/bin/activate"

clean:
	rm -rf __pycache__ src/__pycache__ tests/__pycache__
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "Limpieza de caché completada."
