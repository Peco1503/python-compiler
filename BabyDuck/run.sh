#!/bin/bash

# Verificar si se ha proporcionado un archivo de entrada
if [ $# -eq 0 ]; then
    echo "Uso: $0 <archivo_de_entrada.bduck>"
    exit 1
fi

INPUT_FILE=$1

# Directorios del proyecto
PROJECT_DIR=$(dirname "$0")
SRC_DIR="$PROJECT_DIR/src"
GENERATED_DIR="$PROJECT_DIR/generated/src"  # Modificado para apuntar a generated/src

# Verificar que el archivo de entrada existe
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: El archivo '$INPUT_FILE' no existe."
    exit 1
fi

# Verificar que los archivos generados existen
if [ ! -f "$GENERATED_DIR/BabyDuckLexer.py" ] || [ ! -f "$GENERATED_DIR/BabyDuckParser.py" ]; then
    echo "Error: No se encuentran los archivos generados del compilador."
    echo "Ubicación esperada: $GENERATED_DIR"
    echo "Ejecuta primero el script de generación (build.sh)."
    exit 1
fi

# Ajustar PYTHONPATH para que Python pueda encontrar los módulos
export PYTHONPATH="$PROJECT_DIR:$GENERATED_DIR:$SRC_DIR:$PYTHONPATH"

# Ejecutar el compilador (usando python3 en lugar de python para macOS)
echo "Ejecutando el compilador BabyDuck en el archivo: $INPUT_FILE"
python3 "$SRC_DIR/babyduck_compiler.py" "$INPUT_FILE"