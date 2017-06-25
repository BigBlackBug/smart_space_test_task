from multiplier.errors import ApplicationError


def validate_input_matrices(first: list, second: list):
    if len(first) == 0:
        raise ApplicationError("First matrix is empty")
    if len(second) == 0:
        raise ApplicationError("Second matrix is empty")

    if len(first[0]) != len(second):
        raise ApplicationError(
            "Number of columns of first matrix must be equal "
            "to the number of rows of the second matrix")
