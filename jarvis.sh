#!/usr/bin/env sh
# Wrapper de jarvis: ejecuta la CLI con el python que tenga el paquete instalado.
# Prefiere python3; usa el módulo si la consola "jarvis" no está en el PATH.
set -e

if command -v jarvis >/dev/null 2>&1; then
    exec jarvis "$@"
fi

if command -v python3 >/dev/null 2>&1; then
    exec python3 -m jarvis "$@"
fi

echo "jarvis: no se encontró ni la consola 'jarvis' ni python3" >&2
exit 127
