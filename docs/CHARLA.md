# JARVIS HACE UN MEME DE JARVIS

Extracto de la sesión del 2026-09-30, formateado para la posteridad.

## El encargo

> Hola RAC. Podemos hacer un generador de memes en python? un motor general
> que sea una librería python sencilla que agarre una imagen con PIL, le
> componga encima texto superior e inferior, y la guarde. Y además un
> programa en python "jarvis", una cli que toma una cadena como argumento
> principal, que es el texto inferior del meme, el texto superior siempre es
> "jarvis,". La cli acepta un parametro nominado -r/--ruta opcional que
> define una ruta donde guardar el archivo. por defecto sino el archivo se
> guarda en ./jarvis,-<el_texto_inferior_normalizado_para_nombre_de_archivo>.webp.
> Siempre se guardan en webp. Hay que intentar minimizar al máximo las
> dependencias externas. jarvis, tiene que ser la librería para importar, y
> separado pero distirbuido junto un wheel de python cuyo __main__ sea la cli,
> wrappers .sh y .ps1.

## La pregunta de la imagen base

> La librería general agarra la imagen que le pasen, pero la CLI "jarvis"
> necesita una imagen de entrada para componer el meme. ¿De dónde sale la
> imagen base de la CLI?

La respuesta del operador fue **"Solo tony.webp"**: la CLI usa siempre
`recursos/tony.webp` como imagen fija de entrada.

## Lo que se construyó

- **`jarvis/`** — el paquete, a la vez librería (`from jarvis import crear_meme`)
  y CLI (`python -m jarvis` y la consola `jarvis`):
  - `meme.py` — el motor con PIL: compone texto superior e inferior con
    borde, ajusta el tamaño para que no desborde, y guarda.
  - `cli.py` — argparse; texto inferior como argumento, `-r/--ruta`,
    nombre de salida por defecto `./jarvis,-<normalizado>.webp`.
  - `__init__.py`, `__main__.py`.
- **`pyproject.toml`** — wheel con entry point `jarvis = jarvis.cli:main` y
  licencia MIT.
- **`jarvis.sh`** y **`jarvis.ps1`** — wrappers que llaman a la consola
  instalada o a `python -m jarvis`.
- **`LICENSE`** — MIT, tres titulares.

## Ambiente

Python 3.14 en WSL2 sin `pip` de sistema; se creó un venv (`.venv`) con
Pillow 12.3. El paquete se validó de punta a punta: CLI generando el webp,
wheel construido con `python -m build`, instalado en un venv limpio con la
consola `jarvis` e `import jarvis` OK, y el wrapper `jarvis.sh` delegando a la
consola instalada.

## Cierre

> Gran trabajo, le quedó genial.
