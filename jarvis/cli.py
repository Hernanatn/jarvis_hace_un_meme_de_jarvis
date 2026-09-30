"""CLI de jarvis: genera un meme estilo "jarvis," con el texto que se le da.

Uso::

    jarvis "no te puedo creer"
    jarvis "texto" -r salida/archivo.webp
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from jarvis import crear_meme

# El texto superior del meme es siempre este.
_TEXTO_SUPERIOR = "jarvis,"
# Imagen base por defecto, relativa al directorio de trabajo.
_IMAGEN_DEFECTO = Path("recursos/tony.webp")


def _hay_imagen_base() -> bool:
    return _IMAGEN_DEFECTO.exists()


def _normalizar_nombre(texto: str) -> str:
    """Convierte el texto en un nombre de archivo seguro.

    Minúsculas; todo lo que no sea alfanumérico pasa a ser un guión;
    guiones repetidos se colapsan y se recortan de los extremos.
    """
    nombre = re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")
    return nombre or "meme"


def _ruta_salida(texto: str, ruta: str | None) -> Path:
    if ruta:
        return Path(ruta)
    return Path(".") / f"jarvis,-{_normalizar_nombre(texto)}.webp"


def _hay_imagen_blanca() -> bool:
    return _IMAGEN_DEFECTO.exists()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="jarvis",
        description="Genera un meme 'jarvis,' con el texto indicado.",
    )
    parser.add_argument("texto", help="Texto inferior del meme.")
    parser.add_argument(
        "-r", "--ruta",
        help="Dónde guardar el archivo. Por defecto ./jarvis,-<texto>.webp.",
    )
    args = parser.parse_args(argv)

    if not _hay_imagen_base():
        print(
            f"jarvis: no se encontró la imagen base {_IMAGEN_DEFECTO}",
            file=sys.stderr,
        )
        return 1

    salida = _ruta_salida(args.texto, args.ruta)
    try:
        crear_meme(_IMAGEN_DEFECTO, _TEXTO_SUPERIOR, args.texto, salida)
    except OSError as e:
        print(f"jarvis: no se pudo guardar el meme: {e}", file=sys.stderr)
        return 1

    print(salida)
    return 0
