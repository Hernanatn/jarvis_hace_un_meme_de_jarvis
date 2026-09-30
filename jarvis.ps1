# Wrapper de jarvis (PowerShell): ejecuta la CLI con el python que tenga el
# paquete instalado. Prefiere la consola "jarvis"; si no está en el PATH,
# usa el módulo con python.
param()

$ErrorActionPreference = "Stop"

if (Get-Command jarvis -ErrorAction SilentlyContinue) {
    & jarvis @args
    exit $LASTEXITCODE
}

if (Get-Command python -ErrorAction SilentlyContinue) {
    & python -m jarvis @args
    exit $LASTEXITCODE
}

Write-Error "jarvis: no se encontró ni la consola 'jarvis' ni python"
exit 127
