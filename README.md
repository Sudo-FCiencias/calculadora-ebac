# Calculadora EBAC

Una aplicación de calculadora tradicional desarrollada con Python y PySide6, 
creada como ejemplo de frontend para el Webinar "Python 360°" de EBAC.

## Requisitos del Sistema

- Python 3.8 o superior
- Se sugiere usar uv, pero se puede hacer con pip

## Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Sudo-FCiencias/calculadora-ebac.git
cd calculadora-ebac
```

### 2. Entorno Virtual y Dependencias (con pip)

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Si decides usar uv, el proceso es aún más rápido:

```bash
uv init
source .venv/bin/activate // o el equivalente de Windows
uv add -r requirements.txt
```

## Ejecución

```bash
python src/main.py
```

O alternativamente:

```bash
uv run src/main.py
```

La ventana de la calculadora aparecerá centrada en tu pantalla.

## Uso de la Calculadora

### Operaciones Básicas

1. **Ingresar números**: Haz clic en los botones numéricos (0-9)
2. **Agregar decimales**: Usa el botón "." para números con decimales
3. **Seleccionar operación**: Haz clic en +, -, * o /
4. **Calcular resultado**: Presiona el botón "=" (verde)
5. **Limpiar**: Usa el botón "C" para reiniciar


## Estructura del Proyecto

```
calculadora-ebac/
│
├── README.md                 # Este archivo - documentación del proyecto
├── requirements.txt          # Dependencias de Python
├── .gitignore               # Archivos a ignorar en Git
├── LICENSE                  # Licencia del proyecto
│
└── src/                     # Código fuente
    ├── __init__.py          # Inicialización del paquete
    ├── main.py              # Punto de entrada de la aplicación
    ├── calculadora_ui.py    # Interfaz gráfica (UI)
    └── calculadora_logica.py # Lógica de operaciones
```

### Descripción de Módulos

#### `main.py`
Punto de entrada de la aplicación. Inicializa Qt, crea la ventana principal y centra la aplicación en la pantalla.

#### `calculadora_ui.py`
Contiene la clase `CalculadoraUI` que:
- Construye la interfaz gráfica usando PySide6
- Crea el display digital y los botones
- Maneja eventos de clic en botones
- Aplica estilos visuales (colores, fuentes, efectos hover)

#### `calculadora_logica.py`
Contiene la clase `CalculadoraLogica` que:
- Gestiona el estado de la calculadora (operandos, operación)
- Implementa las operaciones matemáticas
- Valida entradas (previene errores)
- Maneja el flujo de cálculos

#### `__init__.py`
Define el paquete y sus metadatos (versión, autor, descripción).


## Recursos de Aprendizaje

- [Documentación oficial de PySide6](https://doc.qt.io/qtforpython/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [PEP 8 - Guía de Estilo](https://pep8.org/)
- [Qt Designer para diseño visual](https://doc.qt.io/qt-6/qtdesigner-manual.html)