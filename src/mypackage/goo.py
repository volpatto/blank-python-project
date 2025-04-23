"""
Another dummy module to be use as an example.

This module provides:

* `calculate_something_big(x, dim)`: a function that performs a nice calculation.
"""


def calculate_something_big(x: float, slope: float = 1.0, y_intercept: float = 0.0) -> float:
    """
    This function calculates something big.

    In summary, this function calculates a linear relationship between x and y.
    This relationship is given as:

    $$
    y = m x + b,
    $$

    where `m` is the slope and `b` is the `y_intercept`, both are exposed as
    args to this function.

    :param x:
        The independent variable.

    :param slope:
        The slope of the linear function.

    :param y_intercept:
        The value that the linear function intercepts the y-axis.

    :return:
        The dependent variable of the linear function (y).
    """
    f = slope * x + y_intercept
    return f
