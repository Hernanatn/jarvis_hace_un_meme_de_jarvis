"""Librería jarvis: generador de memes.

Uso como librería::

    from jarvis import crear_meme
    crear_meme("foto.png", "arriba", "abajo", "salida.png")

Y como CLI::

    python -m jarvis "texto inferior"
"""

from jarvis.meme import crear_meme

__all__ = ["crear_meme"]
__version__ = "0.1.0"
