# jarvis

Generador de memes **jarvis,** en Python. Una librería pequeña que agarra una
imagen, le compone texto superior e inferior (formato clásico de meme, letra
con borde) y la guarda. Incluye una CLI que produce el meme con el texto
inferior que se le pase.

Sólo depende de **Pillow**.

## Como librería

```python
from jarvis import crear_meme

crear_meme("recursos/tony.webp", "jarvis,", "no te puedo creer", "salida.webp")
```

`crear_meme` acepta una ruta o un objeto `PIL.Image`, y el formato de salida
se deduce de la extensión de `ruta_salida` (se fuerza PNG si la extensión no
es reconocible).

## Como CLI

```sh
jarvis "no te puedo creer"                  # genera ./jarvis,-no-te-puedo-creer.webp
jarvis "texto" -r salida/archivo.webp       # guarda donde se le diga
```

- El **texto inferior** es el primer argumento.
- El **texto superior** es siempre `jarvis,`.
- Con `-r/--ruta` se define dónde guardar; sin él, el archivo se guarda en
  `./jarvis,-<texto_normalizado>.webp`.
- Siempre se guarda en `.webp`.
- La imagen base es siempre `recursos/tony.webp` (relativa al directorio de
  trabajo). El nombre del archivo normaliza el texto: minúsculas y guiones.

También se puede correr como módulo: `python -m jarvis "texto"`.

La fuente del texto se puede cambiar con la variable de entorno `JARVIS_FUENTE`
apuntando a un archivo `.ttf`.

## Instalación

```sh
pip install .
```

## Wrappers

`jarvis.sh` y `jarvis.ps1` son envolturas que llaman a la CLI con el Python
que tenga el paquete instalado (prefieren la consola `jarvis`; si no está en
el `PATH`, usan `python -m jarvis`).
