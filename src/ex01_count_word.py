"""
EX01 (Texto) · Buscar una palabra en un fichero

Objetivo:
- Practicar la lectura de ficheros de texto usando `open(...)`.
- Normalizar el contenido (minúsculas) y contar coincidencias.

Consejo:
- No hace falta una solución "perfecta" de NLP.
  Con que cuentes palabras separadas por espacios y elimines puntuación básica es suficiente.
"""

from __future__ import annotations

from pathlib import Path
import string


def count_word_in_file(path: str | Path, word: str) -> int:
    """
    Devuelve el número de apariciones de `word` dentro del fichero de texto `path`.

    Reglas:
    - Búsqueda NO sensible a mayúsculas/minúsculas.
      Ej: "Hola" cuenta como "hola".
    - Cuenta por palabra (no por subcadena).
      Ej: si word="sol", NO debe contar dentro de "solución".
    - Considera puntuación básica como separador (.,;:!? etc.)
      Pista: puedes traducir la puntuación a espacios.

    Errores:
    - Si el fichero no existe, lanza FileNotFoundError.
    - Si word está vacía o solo espacios, lanza ValueError.

    Ejemplo:
    Fichero: "Hola hola mundo"
    word="hola" -> 2
    """
    if not word or word.strip() == "":
        raise ValueError("La palabra no puede estar vacía ni contener solo espacios.")
    try: 
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"El fichero {path} no existe.")
    text = text.lower()
    word = word.lower()
    text = text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    words = text.split()
    count = sum(1 for w in words if w == word)
    return count