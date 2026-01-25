#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
        """
            Divides all elements of a matrix.

                Args:
                        matrix: A list of lists of integers or floats.
                                div: A number (integer or float) to divide by.

                                    Returns:
                                            A new matrix with result of division rounded to 2 decimal places.

                                                Raises:
                                                        TypeError: If matrix is not a list of lists of integers/floats.
                                                                TypeError: If each row of the matrix must have the same size.
                                                                        TypeError: If div is not a number.
                                                                                ZeroDivisionError: If div is equal to 0.
                                                                                    """
                                                                                        msg_type = "matrix must be a matrix (list of lists) of integers/floats"
                                                                                            msg_size = "Each row of the matrix must have the same size"

                                                                                                if not isinstance(div, (int, float)):
                                                                                                            raise TypeError("div must be a number")
                                                                                                            if div == 0:
                                                                                                                        raise ZeroDivisionError("division by zero")

                                                                                                                        if not isinstance(matrix, list) or len(matrix) == 0:
                                                                                                                                    raise TypeError(msg_type)

                                                                                                                                    new_matrix = []
                                                                                                                                        row_length = 0

                                                                                                                                            for i, row in enumerate(matrix):
                                                                                                                                                        if not isinstance(row, list):
                                                                                                                                                                        raise TypeError(msg_type)
                                                                                                                                                                            
                                                                                                                                                                            if i == 0:
                                                                                                                                                                                            row_length = len(row)
                                                                                                                                                                                                    elif len(row) != row_length:
                                                                                                                                                                                                                    raise TypeError(msg_size)

                                                                                                                                                                                                                        new_row = []
                                                                                                                                                                                                                                for x in row:
                                                                                                                                                                                                                                                if not isinstance(x, (int, float)):
                                                                                                                                                                                                                                                                    raise TypeError(msg_type)
                                                                                                                                                                                                                                                                            new_row.append(round(x / div, 2))
                                                                                                                                                                                                                                                                                    new_matrix.append(new_row)

                                                                                                                                                                                                                                                                                        return new_matrix
