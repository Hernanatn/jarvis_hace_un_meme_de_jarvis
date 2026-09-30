---
name: jarvis
description: Generar un meme "jarvis," con el texto inferior que se le indique, usando la CLI de este repositorio.
---

# jarvis — generá un meme "jarvis,"

Este skill te permite generar un meme al estilo "jarvis," (texto superior fijo
"jarvis,") con el texto inferior que quieras, usando el generador de este
repositorio.

## Cuándo usarlo

Cuando la persona te pida "hacer un meme de jarvis", "un meme subtitle", o
"jarvis haciendo tal cosa" con un texto concreto.

## Cómo se hace

1. Activa el entorno virtual del repo (si no está creado, crealo con
   `python3 -m venv .venv` e instalá el paquete con `pip install -e .`):

   ```
   .venv/bin/python -m jarvis "TEXTO INFERIOR"
   ```

   Reemplazá `TEXTO INFERIOR` por el texto que quieras en el meme.

2. El archivo se genera en `./jarvis,-<texto normalizado>.webp` (o en la ruta
   que se pase con `-r RUTA`). El texto superior del meme es siempre
   "jarvis,".

3. Si la imagen base `recursos/tony.webp` no existe, el comando falla con un
   mensaje claro a stderr y el código de salida es 1.

## Ejemplos

- `.venv/bin/python -m jarvis "no te puedo creer"` → genera
  `./jarvis,-no-te-puedo-creer.webp`.
- `.venv/bin/python -m jarvis "hola" -r salida/meme.webp` → guarda el meme en
  `salida/meme.webp`.

## Notas

- La opción `-r` o `--ruta` elige dónde guardar el archivo; el formato se
  deduce de la extensión del nombre (webp por defecto, png si la ruta
  termina en `.png`).
- Solo depende de Pillow como dependencia de runtime.
