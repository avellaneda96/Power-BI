"""Simple calculator module with command-line interface."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict


@dataclass
class Operation:
    name: str
    function: Callable[[float, float], float]


class Calculadora:
    """A basic calculator supporting addition, subtraction, multiplication, and division."""

    def __init__(self) -> None:
        self._operaciones: Dict[str, Operation] = {
            "1": Operation("suma", lambda x, y: x + y),
            "2": Operation("resta", lambda x, y: x - y),
            "3": Operation("multiplicación", lambda x, y: x * y),
            "4": Operation("división", self._division),
        }

    @staticmethod
    def _division(x: float, y: float) -> float:
        if y == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return x / y

    def calcular(self, opcion: str, x: float, y: float) -> float:
        if opcion not in self._operaciones:
            raise ValueError("Opción de operación inválida")
        operacion = self._operaciones[opcion]
        return operacion.function(x, y)

    def menu(self) -> str:
        lineas = ["Seleccione la operación:"]
        for clave, operacion in sorted(self._operaciones.items()):
            lineas.append(f"{clave}. {operacion.name.title()}")
        return "\n".join(lineas)


def solicitar_numero(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Intente de nuevo con un número válido.")


def main() -> None:
    calculadora = Calculadora()
    print(calculadora.menu())
    opcion = input("Ingrese la opción deseada: ")

    try:
        numero1 = solicitar_numero("Ingrese el primer número: ")
        numero2 = solicitar_numero("Ingrese el segundo número: ")
        resultado = calculadora.calcular(opcion, numero1, numero2)
    except (ValueError, ZeroDivisionError) as error:
        print(f"Error: {error}")
    else:
        print(f"El resultado es: {resultado}")


if __name__ == "__main__":
    main()
