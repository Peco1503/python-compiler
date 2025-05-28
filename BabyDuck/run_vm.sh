#!/bin/bash

# Verificar si se ha proporcionado un archivo de entrada
if [ $# -eq 0 ]; then
    echo "Uso: $0 <archivo.bdobj>"
    exit 1
fi

INPUT_FILE=$1

# Directorios del proyecto
PROJECT_DIR=$(dirname "$0")
SRC_DIR="$PROJECT_DIR/src"

# Verificar que el archivo de entrada existe
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: El archivo '$INPUT_FILE' no existe."
    exit 1
fi

# Verificar la extensión del archivo
if [[ "$INPUT_FILE" != *.bdobj ]]; then
    echo "Error: El archivo debe tener extensión .bdobj"
    exit 1
fi

# Verificar que existe el intérprete de la máquina virtual
VM_INTERPRETER="$SRC_DIR/vm_interpreter.py"
if [ ! -f "$VM_INTERPRETER" ]; then
    echo "Error: No se encuentra el intérprete de la máquina virtual ($VM_INTERPRETER)."
    exit 1
fi

# Ajustar PYTHONPATH para que Python pueda encontrar los módulos
export PYTHONPATH="$PROJECT_DIR:$SRC_DIR:$PYTHONPATH"

# Ejecutar la máquina virtual
echo "Ejecutando la máquina virtual BabyDuck en el archivo: $INPUT_FILE"
python3 "$VM_INTERPRETER" "$INPUT_FILE"