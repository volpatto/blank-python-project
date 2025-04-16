"""
A generic module to use as example.
"""

import numpy as np


def a_function(x: float, dim: int) -> np.ndarray:
    """
    Define a generic function.

    :param x:
        The function's argument array.

    :param dim:
        Number of dimensions to expand.

    :return:
        The evaluated function at the given input array.
    """
    f = np.ones(dim) + x
    return f
