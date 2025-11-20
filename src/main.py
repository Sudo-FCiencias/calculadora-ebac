"""
Punto de entrada principal para la Calculadora EBAC.

Este módulo inicializa la aplicación Qt y crea la ventana principal de la calculadora.
Se encarga de configurar el sistema de aplicación y mostrar la interfaz gráfica.
"""

import sys
from PySide6.QtWidgets import QApplication

from calculadora_ui import CalculadoraUI


def main():
    """
    Función principal que inicia la aplicación.

    Crea la instancia de QApplication, inicializa la ventana de la calculadora,
    la centra en la pantalla y entra en el loop de eventos de la aplicación.
    """
    # Creamos la aplicación Qt
    app = QApplication(sys.argv)

    # Configuramos el estilo de la aplicación
    app.setStyle("Fusion")

    # Creamos la ventana de la calculadora
    calculadora = CalculadoraUI()

    # Centramos la ventana en la pantalla
    calculadora.show()

    # Ajustamos la posición para centrar la ventana
    # Esto asegura que la ventana aparezca en el centro de la pantalla
    screen = app.primaryScreen().geometry()
    x = (screen.width() - calculadora.width()) // 2
    y = (screen.height() - calculadora.height()) // 2
    calculadora.move(x, y)

    # Entramos en el loop de eventos de la aplicación
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
