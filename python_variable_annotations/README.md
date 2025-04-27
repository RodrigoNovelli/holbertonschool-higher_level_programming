Cómo usar type annotations en funciones y variables

    Funciones: Se anotan los parámetros y el tipo de retorno.

def greet(name: str) -> str:
    return f"Hello, {name}!"

Variables: Se anotan los tipos al declarar.

counter: int = 0
price: float = 19.99

Colecciones: Usar List, Dict, etc. desde typing.

    from typing import List, Dict

    names: List[str] = ["Alice", "Bob"]
    person: Dict[str, int] = {"age": 30}

Duck Typing

    En Python, importa el comportamiento de un objeto, no su tipo exacto.

    Ejemplo:

    def print_all(elements):
        for element in elements:
            print(element)

    Si un objeto se puede iterar, no importa si es lista, tupla o set.

    "If it looks like a duck and quacks like a duck, it must be a duck."

Validar tu código con mypy

    mypy es una herramienta que chequea si los tipos anotados son correctos sin ejecutar el código.

    Instalar:

pip install mypy

Usar:

mypy my_script.py

Ejemplo de error detectado:

error: Argument 1 to "square" has incompatible type "str"; expected "int"