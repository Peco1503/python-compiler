# Compilador BabyDuck

Implementación de un compilador para el lenguaje BabyDuck utilizando Python y ANTLR.

## Estructura del proyecto

```
BabyDuck/
├── build.sh                    # Script para generar el lexer y parser
├── run.sh                      # Script para ejecutar el compilador
├── antlr-4.13.1-complete.jar   # JAR de ANTLR (se descarga automáticamente)
├── src/                        # Código fuente
│   ├── BabyDuck.g4             # Gramática ANTLR
│   └── babyduck_compiler.py    # Programa principal
├── generated/                  # Archivos generados por ANTLR
│   ├── BabyDuckLexer.py        # Scanner generado
│   ├── BabyDuckParser.py       # Parser generado
│   ├── BabyDuckListener.py     # Listener generado
│   └── BabyDuckVisitor.py      # Visitor generado
└── tests/                      # Programas de prueba
    └── programa1.bduck         # Programa de ejemplo
```