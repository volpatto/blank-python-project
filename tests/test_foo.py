import pytest
import numpy as np

from mypackage import foo


@pytest.mark.parametrize("dim", [3, 4, 5])
def test_a_function(dim):
    """
    Checks if foo.a_function is consistent when x = 0.
    """
    output = foo.a_function(x=0.0, dim=dim)
    assert output == pytest.approx(np.ones(dim))
