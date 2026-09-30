# jarvis — cómo correr

`jarvis` es un generador de memes que agarra una imagen (`recursos/tony.webp`),
le escribe *jarvis,* arriba y el texto que le pases abajo, y guarda el
resultado en `.webp`. Sólo depende de Pillow.

## Correr

```sh
# desde la raíz del repositorio, con el paquete importable
python -m jarvis "texto inferior"

# con la consola instalada
jarvis "texto inferior"
jarvis "texto" -r ruta/de/salida.webp
```

- El **texto inferior** es el primer argumento.
- El **texto superior** es siempre *jarvis,*.
- Sin `-r`, guarda en `./jarvis,-<texto_normalizado>.webp`. Siempre `.webp`.

Instalación del paquete:

```sh
pip install .
```

## Dejar el wrapper en el path

Los wrappers (`jarvis.sh` en bash, `jarvis.ps1` en PowerShell) llaman a la
consola `jarvis` instalada o, si no está en el `PATH`, a `python -m jarvis`.
Para dejarlos siempre disponibles hay que poner el directorio del repositorio
en el `PATH`.

### Linux / macOS (bash)

```sh
echo 'export PATH="$PATH:/mnt/c/Users/Hernán/github/hernanatn/jarvis_hace_un_meme_de_jarvis"' >> ~/.bashrc
source ~/.bashrc
# el wrapper se llama con:
jarvis.sh "texto"
```

### Windows (PowerShell)

```powershell
# agrega el directorio al PATH del usuario (persistente)
[Environment]::SetEnvironmentVariable(
  "Path",
  [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\ruta\al\repositorio",
  "User"
)
# en la sesión actual:
$env:Path += ";C:\ruta\al\repositorio"
```

Tras esto, `jarvis.ps1 "texto"` queda disponible desde cualquier directorio.
