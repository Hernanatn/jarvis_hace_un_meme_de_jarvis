"""Motor de composición de memes.

Agarra una imagen, le compone texto superior e inferior (el clásico formato de
meme con letra tipo Impact con borde), y guarda el resultado.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# Fuente con la que componer el texto. Se busca en este orden:
#  1. la variable de entorno JARVIS_FUENTE (ruta a un .ttf)
#  2. un "arialbd.ttf" (Impact-like) razonable por plataforma
#  3. la fuente por defecto de PIL (serif básica) como último recurso
_CANDIDATOS_FUENTE = [
    "arialbd.ttf",
    "arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]

# Grosor del borde del texto, como fracción del alto del cuadro.
_GROSOR_BORDE = 0.006


def _normalizar_texto(texto: str) -> str:
    """Quita espacios de sobra del texto del meme (no toca los saltos)."""
    lineas = [l.strip() for l in texto.splitlines() if l.strip()]
    return "\n".join(lineas)


def _fuente(tamano: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    import os

    ruta_env = os.environ.get("JARVIS_FUENTE")
    candidatos = ([ruta_env] if ruta_env else []) + _CANDIDATOS_FUENTE
    for candidato in candidatos:
        if not candidato:
            continue
        try:
            return ImageFont.truetype(candidato, tamano)
        except OSError:
            continue
    return ImageFont.load_default()


def _ajustar_tamano(draw: ImageDraw.ImageDraw, texto: str, ancho_max: int,
                    tamano_inicial: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Devuelve la fuente más grande que no desborda el ancho disponible."""
    tamano = tamano_inicial
    while tamano > 8:
        fuente = _fuente(tamano)
        if draw.textbbox((0, 0), texto, font=fuente)[2] <= ancho_max:
            return fuente
        tamano = int(tamano * 0.9)
    return _fuente(tamano)


def _dibujar_texto(draw: ImageDraw.ImageDraw, texto: str, x: float, y: float,
                   ancho_max: int, alto: int, grosor_borde: float) -> None:
    """Dibuja el texto centrado horizontalmente en (x, y), con contorno."""
    tamano = int(alto * 0.14)
    fuente = _ajustar_tamano(draw, texto, ancho_max, tamano)

    # El texto puede ser multilínea: se divide en líneas y se apilan.
    ancho_caja = draw.textbbox((0, 0), texto, font=fuente)[2]
    lineas = texto.splitlines() if texto else [""]
    alto_linea = int(fuente.size * 1.2)
    y_linea = y
    for linea in lineas:
        ancho = draw.textlength(linea, font=fuente)
        x_ini = x + (ancho_caja - ancho) / 2
        grosor = max(1, int(grosor_borde * alto))
        draw.text((x_ini, y_linea), linea, font=fuente,
                  fill="white", stroke_width=grosor, stroke_fill="black")
        y_linea += alto_linea


def crear_meme(imagen: str | Path | Image.Image,
               texto_superior: str, texto_inferior: str,
               ruta_salida: str | Path) -> Path:
    """Compone un meme sobre `imagen` y lo guarda en `ruta_salida`.

    Parámetros
    ----------
    imagen:
        La imagen base: una ruta a un archivo o un objeto PIL ya abierto.
    texto_superior, texto_inferior:
        Los textos de arriba y abajo del meme.
    ruta_salida:
        Dónde guardar el resultado. El formato se deduce de la extensión; si
        la ruta no termina en una extensión reconocible se fuerza PNG.

    Devuelve la ruta al archivo guardado.
    """
    img = imagen if isinstance(imagen, Image.Image) else Image.open(imagen)
    img = img.convert("RGB")
    # La copiamos para no mutar la imagen base si venía ya abierta.
    salida = img.copy()

    draw = ImageDraw.Draw(salida)
    ancho, alto = salida.size
    margen = int(ancho * 0.04)
    ancho_util = ancho - 2 * margen
    grosor = _GROSOR_BORDE

    # Texto superior, anclado arriba; texto inferior, anclado abajo.
    sup = _normalizar_texto(texto_superior)
    inf = _normalizar_texto(texto_inferior)

    # Punto de partida del texto superior: un pequeño margen desde el techo.
    _dibujar_texto(draw, sup, margen, margen, ancho_util, alto, grosor)

    # Para el inferior, medimos su alto y lo anclamos al piso.
    tamano = int(alto * 0.14)
    fuente = _ajustar_tamano(draw, inf, ancho_util, tamano)
    alto_linea = int(fuente.size * 1.2)
    n_lineas = len(inf.splitlines()) if inf else 1
    alto_bloque = alto_linea * n_lineas
    y_inferior = alto - margen - alto_bloque
    _dibujar_texto(draw, inf, margen, y_inferior, ancho_util, alto, grosor)

    ruta = Path(ruta_salida)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    salida.save(ruta)
    return ruta
