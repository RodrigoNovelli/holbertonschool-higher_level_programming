#!/usr/bin/python3


"""
    Clase MyList que extiende la funcionalidad de la clase list.

    Esta clase hereda de la clase base list y proporciona un método adicional
    para imprimir los elementos de la lista en orden ascendente.
    """


class MyList(list):

    """
        Imprime los elementos de la lista en orden ascendente.

        Utiliza la función sorted para obtener una lista ordenada de los
        elementos y los imprime.

        Ejemplo:
            >>> my_list = MyList([3, 1, 2])
            >>> my_list.print_sorted()
            [1, 2, 3]
        """

    def print_sorted(self):
        print(sorted(self))
