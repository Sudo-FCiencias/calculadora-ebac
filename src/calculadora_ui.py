"""
Módulo de interfaz gráfica para la Calculadora EBAC.

Este módulo contiene la clase CalculadoraUI que construye y maneja la interfaz
gráfica de usuario usando PySide6/Qt. Incluye el display, botones numéricos,
botones de operaciones y manejo de eventos.
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from calculadora_logica import CalculadoraLogica


class CalculadoraUI(QMainWindow):
    """
    Clase que maneja la interfaz gráfica de la calculadora.

    Crea una ventana con un display digital y un teclado numérico organizado
    en un grid layout. Los botones están organizados de manera intuitiva con
    números, operaciones, punto decimal y funciones especiales (limpiar, igual).

    Attributes:
        logica (CalculadoraLogica): Instancia de la lógica de negocio
        display (QLineEdit): Campo de texto para mostrar números y resultados
    """

    def __init__(self):
        """Inicializa la ventana de la calculadora y sus componentes."""
        super().__init__()

        # Instanciamos la lógica de negocio
        self.logica = CalculadoraLogica()

        # Configuramos la ventana principal
        self.setWindowTitle("Calculadora EBAC")
        self.setFixedSize(400, 500)

        # Creamos y configuramos la interfaz
        self._crear_interfaz()

    def _crear_interfaz(self):
        """
        Crea todos los elementos de la interfaz gráfica.

        Construye el display y el teclado numérico con todos sus botones,
        aplicando estilos y organizándolos en layouts apropiados.
        """
        # Widget central
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        # Layout principal vertical
        layout_principal = QVBoxLayout()
        widget_central.setLayout(layout_principal)

        # Creamos el display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setText("0")
        self.display.setMinimumHeight(80)

        # Estilo del display - fuente grande y clara
        fuente_display = QFont("Arial", 24, QFont.Bold)
        self.display.setFont(fuente_display)

        # Estilo visual del display
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #2b2b2b;
                color: #00ff00;
                border: 2px solid #555555;
                border-radius: 5px;
                padding: 10px;
            }
        """)

        layout_principal.addWidget(self.display)

        # Creamos el grid layout para los botones
        layout_botones = QGridLayout()
        layout_botones.setSpacing(5)

        # Definimos los botones en su posición (texto, fila, columna, ancho_cols)
        botones = [
            # Fila 1: Funciones especiales y operación
            ("C", 0, 0, 3, self._estilo_boton_especial),
            ("/", 0, 3, 1, self._estilo_boton_operacion),
            # Fila 2: Números 7-9 y multiplicación
            ("7", 1, 0, 1, self._estilo_boton_numero),
            ("8", 1, 1, 1, self._estilo_boton_numero),
            ("9", 1, 2, 1, self._estilo_boton_numero),
            ("*", 1, 3, 1, self._estilo_boton_operacion),
            # Fila 3: Números 4-6 y resta
            ("4", 2, 0, 1, self._estilo_boton_numero),
            ("5", 2, 1, 1, self._estilo_boton_numero),
            ("6", 2, 2, 1, self._estilo_boton_numero),
            ("-", 2, 3, 1, self._estilo_boton_operacion),
            # Fila 4: Números 1-3 y suma
            ("1", 3, 0, 1, self._estilo_boton_numero),
            ("2", 3, 1, 1, self._estilo_boton_numero),
            ("3", 3, 2, 1, self._estilo_boton_numero),
            ("+", 3, 3, 1, self._estilo_boton_operacion),
            # Fila 5: Cero, punto decimal e igual
            ("0", 4, 0, 2, self._estilo_boton_numero),
            (".", 4, 2, 1, self._estilo_boton_numero),
            ("=", 4, 3, 1, self._estilo_boton_igual),
        ]

        # Creamos y añadimos cada botón al layout
        for texto, fila, col, ancho, funcion_estilo in botones:
            boton = QPushButton(texto)
            boton.setMinimumHeight(70)

            # Aplicamos el estilo correspondiente
            funcion_estilo(boton)

            # Conectamos el evento de clic
            boton.clicked.connect(lambda checked, t=texto: self._boton_presionado(t))

            # Añadimos el botón al grid
            layout_botones.addWidget(boton, fila, col, 1, ancho)

        layout_principal.addLayout(layout_botones)

    def _estilo_boton_numero(self, boton: QPushButton):
        """
        Aplica el estilo a los botones numéricos y punto decimal.

        Args:
            boton (QPushButton): El botón a estilizar
        """
        fuente = QFont("Arial", 18, QFont.Bold)
        boton.setFont(fuente)
        boton.setStyleSheet("""
            QPushButton {
                background-color: #4a4a4a;
                color: white;
                border: 1px solid #666666;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #5a5a5a;
            }
            QPushButton:pressed {
                background-color: #3a3a3a;
            }
        """)

    def _estilo_boton_operacion(self, boton: QPushButton):
        """
        Aplica el estilo a los botones de operación (+, -, *, /).

        Args:
            boton (QPushButton): El botón a estilizar
        """
        fuente = QFont("Arial", 18, QFont.Bold)
        boton.setFont(fuente)
        boton.setStyleSheet("""
            QPushButton {
                background-color: #ff9500;
                color: white;
                border: 1px solid #cc7700;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #ffaa00;
            }
            QPushButton:pressed {
                background-color: #ee8400;
            }
        """)

    def _estilo_boton_especial(self, boton: QPushButton):
        """
        Aplica el estilo al botón de limpiar (C).

        Args:
            boton (QPushButton): El botón a estilizar
        """
        fuente = QFont("Arial", 18, QFont.Bold)
        boton.setFont(fuente)
        boton.setStyleSheet("""
            QPushButton {
                background-color: #d4d4d2;
                color: black;
                border: 1px solid #a8a8a6;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #e4e4e2;
            }
            QPushButton:pressed {
                background-color: #c4c4c2;
            }
        """)

    def _estilo_boton_igual(self, boton: QPushButton):
        """
        Aplica el estilo al botón de igual (=).

        Este botón tiene un color distintivo para resaltar su función especial.

        Args:
            boton (QPushButton): El botón a estilizar
        """
        fuente = QFont("Arial", 18, QFont.Bold)
        boton.setFont(fuente)
        boton.setStyleSheet("""
            QPushButton {
                background-color: #34c759;
                color: white;
                border: 1px solid #2a9e47;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #44d769;
            }
            QPushButton:pressed {
                background-color: #24b749;
            }
        """)

    def _boton_presionado(self, texto: str):
        """
        Maneja el evento cuando se presiona un botón.

        Determina qué acción tomar basándose en el texto del botón presionado:
        - Números y punto: agregar al operando actual
        - Operaciones: establecer la operación a realizar
        - Igual: calcular el resultado
        - C: limpiar la calculadora

        Args:
            texto (str): El texto del botón presionado
        """
        # Botón de limpiar
        if texto == "C":
            resultado = self.logica.limpiar()
            self.display.setText(resultado)

        # Botones numéricos y punto decimal
        elif texto in "0123456789.":
            resultado = self.logica.agregar_digito(texto)
            self.display.setText(resultado)

        # Botones de operación
        elif texto in "+-*/":
            resultado = self.logica.establecer_operacion(texto)
            self.display.setText(resultado)

        # Botón de igual
        elif texto == "=":
            resultado = self.logica.calcular()
            if resultado:
                self.display.setText(resultado)
