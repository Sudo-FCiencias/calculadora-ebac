"""
Módulo de lógica de negocio para la Calculadora EBAC.

Este módulo contiene la clase CalculadoraLogica que maneja todas las operaciones
matemáticas y el estado interno de la calculadora, separado de la interfaz gráfica.
"""

from typing import Optional


class CalculadoraLogica:
    """
    Clase que maneja la lógica de operaciones de la calculadora.

    Esta clase mantiene el estado de la calculadora incluyendo el operando actual,
    el operando anterior, y la operación seleccionada. Maneja todas las operaciones
    matemáticas básicas: suma, resta, multiplicación y división.

    Attributes:
        operando_actual (str): El número que se está ingresando actualmente
        operando_anterior (str): El número ingresado antes de seleccionar una operación
        operacion (Optional[str]): La operación seleccionada (+, -, *, /)
        resultado_mostrado (bool): Indica si se está mostrando un resultado
    """

    def __init__(self):
        """Inicializa la calculadora con valores por defecto."""
        self.operando_actual: str = "0"
        self.operando_anterior: str = ""
        self.operacion: Optional[str] = None
        self.resultado_mostrado: bool = False

    def agregar_digito(self, digito: str) -> str:
        """
        Agrega un dígito al operando actual.

        Si se acaba de mostrar un resultado, inicia un nuevo número.
        Evita que se agreguen múltiples puntos decimales.

        Args:
            digito (str): El dígito a agregar ('0'-'9' o '.')

        Returns:
            str: El operando actual actualizado
        """
        # Si acabamos de mostrar un resultado, empezamos un número nuevo
        if self.resultado_mostrado:
            self.operando_actual = "0"
            self.resultado_mostrado = False

        # Si el operando actual es "0", lo reemplazamos (excepto si agregamos un punto)
        if self.operando_actual == "0" and digito != ".":
            self.operando_actual = digito
        # Si ya existe un punto decimal, no permitimos agregar otro
        elif digito == "." and "." in self.operando_actual:
            pass  # No hacemos nada
        # Si es el primer carácter y es un punto, agregamos "0."
        elif digito == "." and self.operando_actual == "0":
            self.operando_actual = "0."
        else:
            self.operando_actual += digito

        return self.operando_actual

    def establecer_operacion(self, operacion: str) -> str:
        """
        Establece la operación a realizar.

        Si ya existe una operación pendiente, primero calcula el resultado
        de esa operación antes de establecer la nueva.

        Args:
            operacion (str): La operación a realizar (+, -, *, /)

        Returns:
            str: El valor a mostrar en el display
        """
        # Si acabamos de mostrar un resultado, usamos ese valor como operando anterior
        if self.resultado_mostrado:
            self.resultado_mostrado = False

        # Si ya tenemos una operación pendiente, calculamos primero
        if self.operacion and self.operando_anterior and not self.resultado_mostrado:
            resultado = self.calcular()
            if resultado:
                self.operando_anterior = resultado
                self.operando_actual = "0"
        else:
            # Guardamos el operando actual como el anterior
            self.operando_anterior = self.operando_actual
            self.operando_actual = "0"

        # Establecemos la nueva operación
        self.operacion = operacion

        return self.operando_anterior

    def calcular(self) -> Optional[str]:
        """
        Calcula el resultado de la operación pendiente.

        Realiza la operación matemática entre el operando anterior y el actual
        usando la operación establecida. Maneja errores como división por cero.

        Returns:
            Optional[str]: El resultado del cálculo o "Error" si hay un problema,
                          None si no hay suficientes datos para calcular
        """
        # Verificamos que tenemos todo lo necesario para calcular
        if not self.operacion or not self.operando_anterior:
            return None

        try:
            # Convertimos los operandos a números flotantes
            num1 = float(self.operando_anterior)
            num2 = float(self.operando_actual)

            # Realizamos la operación correspondiente
            if self.operacion == "+":
                resultado = num1 + num2
            elif self.operacion == "-":
                resultado = num1 - num2
            elif self.operacion == "*":
                resultado = num1 * num2
            elif self.operacion == "/":
                # Verificamos división por cero
                if num2 == 0:
                    self.limpiar()
                    return "Error"
                resultado = num1 / num2
            else:
                return None

            # Formateamos el resultado
            # Si es un número entero, lo mostramos sin decimales
            if resultado == int(resultado):
                resultado_str = str(int(resultado))
            else:
                # Limitamos a 8 decimales para evitar problemas de precisión
                resultado_str = f"{resultado:.8f}".rstrip("0").rstrip(".")

            # Actualizamos el estado
            self.operando_actual = resultado_str
            self.operando_anterior = ""
            self.operacion = None
            self.resultado_mostrado = True

            return resultado_str

        except (ValueError, OverflowError):
            # En caso de error de conversión o desbordamiento
            self.limpiar()
            return "Error"

    def limpiar(self) -> str:
        """
        Limpia todos los valores y reinicia la calculadora.

        Returns:
            str: "0" para mostrar en el display
        """
        self.operando_actual = "0"
        self.operando_anterior = ""
        self.operacion = None
        self.resultado_mostrado = False
        return "0"

    def obtener_display(self) -> str:
        """
        Obtiene el valor que debe mostrarse en el display.

        Returns:
            str: El valor actual del operando a mostrar
        """
        return self.operando_actual
