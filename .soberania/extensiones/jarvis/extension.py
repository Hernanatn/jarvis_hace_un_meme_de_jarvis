"""La extensión jarvis: expone el comando slash `/jarvis` (soberania N4).

El motor de memes vive como librería con su propio entorno (`.venv` del
repo) y su CLI ya validada; el entorno del harness no trae Pillow. El
comando delega en la CLI como subproceso desde la raíz del proyecto y
devuelve la ruta del archivo generado — no duplica el motor ni ensucia el
entorno del harness.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from soberania.extensiones.api import (
    Aviso,
    ContextoDeExtension,
    ResultadoDeComando,
)

_CLI: str = "jarvis"
_AYUDA: str = "Genera un meme 'jarvis,' con el texto inferior indicado. Uso: /jarvis <texto>"


def _rutaDelMotor(raiz: Path) -> tuple[Path, list[str]]:
    """Devuelve (cwd, argumento CLI) para invocar el generador.

    Prefiere la consola instalada (`jarvis`); si no está en el PATH, cae a
    `python -m jarvis` dentro del venv del repo. La extensión busca su
    paquete y sus recursos desde la raíz del proyecto.
    """
    if shutil.which(_CLI):
        return raiz, [_CLI]
    python = raiz / ".venv" / "bin" / "python"
    if python.exists():
        return raiz, [str(python), "-m", "jarvis"]
    return raiz, ["python3", "-m", "jarvis"]


def _manejar(texto: str, raiz: Path) -> ResultadoDeComando:
    texto = texto.strip()
    if not texto:
        return ResultadoDeComando(
            presentacion=Aviso(_AYUDA),
        )
    cwd, comando = _rutaDelMotor(raiz)
    try:
        corrida = subprocess.run(
            [*comando, texto],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return ResultadoDeComando(
            presentacion=Aviso(f"jarvis: no se pudo invocar el generador: {error}"),
        )
    if corrida.returncode != 0:
        detalle = corrida.stderr.strip() or corrida.stdout.strip() or "error desconocido"
        return ResultadoDeComando(
            presentacion=Aviso(f"jarvis: falló al generar el meme ({detalle})"),
        )
    ruta = corrida.stdout.strip()
    return ResultadoDeComando(
        presentacion=Aviso(f"Meme generado en {ruta}"),
    )


def registrarEn(contexto: ContextoDeExtension) -> None:
    """Registra el comando `/jarvis` declarado en el manifiesto."""
    raiz: Path = contexto.raiz
    contexto.registrarComando(
        "jarvis",
        _AYUDA,
        lambda argumentos: _manejar(argumentos, raiz),
    )
