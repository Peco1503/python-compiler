#!/bin/bash

# Directorios del proyecto
PROJECT_DIR=$(dirname "$0")
SRC_DIR="$PROJECT_DIR/src"
GENERATED_DIR="$PROJECT_DIR/generated"

# Verificar si existe Java
if ! command -v java &> /dev/null; then
    echo "Error: Java no está instalado o no está en el PATH."
    exit 1
fi

# Verificar si existe el archivo de gramática
if [ ! -f "$SRC_DIR/BabyDuck.g4" ]; then
    echo "Error: No se encuentra el archivo de gramática ($SRC_DIR/BabyDuck.g4)."
    exit 1
fi

# Verificar si existe el archivo JAR de ANTLR
ANTLR_JAR="antlr-4.13.1-complete.jar"
if [ ! -f "$PROJECT_DIR/$ANTLR_JAR" ]; then
    echo "Descargando ANTLR..."
    # Usar curl en lugar de wget (más común en macOS)
    curl -o "$PROJECT_DIR/$ANTLR_JAR" "https://www.antlr.org/download/$ANTLR_JAR"
    if [ $? -ne 0 ]; then
        echo "Error al descargar ANTLR."
        exit 1
    fi
fi

# Crear directorio para archivos generados si no existe
mkdir -p "$GENERATED_DIR"

# Generar lexer y parser con la opción visitor
echo "Generando el lexer y parser con ANTLR..."
java -jar "$PROJECT_DIR/$ANTLR_JAR" -Dlanguage=Python3 -visitor -o "$GENERATED_DIR" "$SRC_DIR/BabyDuck.g4"

if [ $? -eq 0 ]; then
    echo "Generación exitosa del lexer y parser."
    echo "Ahora puedes ejecutar el compilador con ./run.sh <archivo_de_entrada.bduck>"
else
    echo "Error al generar el lexer y parser."
    exit 1
fi

# Verificar instalación de dependencias Python
echo "Verificando dependencias de Python..."
if ! python -c "import antlr4" &> /dev/null; then
    echo "Instalando dependencias de Python..."
    pip install antlr4-python3-runtime==4.13.1
    if [ $? -ne 0 ]; then
        echo "Error al instalar las dependencias de Python."
        exit 1
    fi
fi

echo "Todo listo para compilar programas BabyDuck."