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

## Requisitos

- Python 3.6 o superior
- Java Runtime Environment (JRE) para ejecutar ANTLR
- pip (para instalar dependencias de Python)

## Instalación

1. Clona el repositorio o descarga los archivos.

2. Ejecuta el script de construcción para generar el lexer y parser y descargar las dependencias:

```bash
chmod +x build.sh
./build.sh
```

Este script:
- Descarga el JAR de ANTLR si no está presente
- Genera el lexer y parser a partir de la gramática
- Instala la dependencia `antlr4-python3-runtime` si no está instalada

## Uso

Para compilar un programa BabyDuck, utiliza el script `run.sh`:

```bash
chmod +x run.sh
./run.sh tests/programa1.bduck
```

## Formato del lenguaje BabyDuck

El lenguaje BabyDuck es un lenguaje de programación simple con la siguiente sintaxis:

- **Estructura de un programa**:
  ```
  program nombre;
  [declaración de variables]
  [declaración de funciones]
  main 
  {
     [statements]
  }
  end
  ```

- **Declaración de variables**:
  ```
  var
    id1, id2, ...: tipo;
    id3, id4, ...: tipo;
  ```
  donde tipo puede ser `int` o `float`.

- **Asignación**:
  ```
  id = expresion;
  ```

- **Condicionales**:
  ```
  if (expresion) {
    [statements]
  };
  
  if (expresion) {
    [statements]
  } else {
    [statements]
  };
  ```

- **Ciclos**:
  ```
  while (expresion) do {
    [statements]
  };
  ```

- **Impresión**:
  ```
  print(expresion1, expresion2, ...);
  print("texto");
  ```

- **Funciones**:
  ```
  void nombre;
  [declaración de variables]
  {
    [statements]
  }
  ```

- **Llamada a funciones**:
  ```
  nombre;
  ```

## Contribuir

Si deseas contribuir a este proyecto, no dudes en crear un fork y enviar tus pull requests.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.