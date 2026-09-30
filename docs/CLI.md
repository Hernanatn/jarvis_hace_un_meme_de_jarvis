# CLI de jarvis — referencia

Genera un meme *jarvis,* con el texto inferior que se le pase, sobre la imagen
`recursos/tony.webp`. Siempre guarda en `.webp`.

## Uso

```
jarvis <texto> [-r RUTA]
```

También se corre como módulo:

```
python -m jarvis <texto> [-r RUTA]
```

## Argumentos

| Argumento | Descripción |
|---|---|
| `texto` | El texto inferior del meme. El texto superior es siempre `jarvis,`. |
| `-r`, `--ruta` | Ruta donde guardar el archivo. Por defecto: `./jarvis,-<texto_normalizado>.webp`. |

## Salida

- En éxito, imprime en la salida estándar la ruta del archivo generado y
  termina con código `0`.
- Si falta la imagen base `recursos/tony.webp`, o si no se puede guardar el
  archivo, imprime el motivo en la salida de error y termina con código `1`.

## Nombre de archivo por defecto

El nombre normaliza el texto: a minúsculas y todo lo que no sea alfanumérico
pasa a ser un guión; los guiones repetidos se colapsan y se recortan de los
extremos. Por ejemplo:

```
jarvis "no te puedo creer"        -> ./jarvis,-no-te-puedo-creer.webp
```

Si el texto queda vacío tras normalizar, se usa `meme` como nombre.

## Variables de entorno

| Variable | Efecto |
|---|---|
| `JARVIS_FUENTE` | Ruta a un archivo `.ttf` para cambiar la fuente del texto. |
