# %% [markdown]
# # A WIP notebook
#
# This is an example of a notebook that could be a WIP, a PoC (proof-of-concept), or some kind of draft that is not ready to be tested or checked. Thus, both docs and tests have to skip this file.

# %% [markdown]
# ## Loading dependencies

# %%
import numpy as np

from mypackage import foo, goo

# %% [markdown]
# ## Innovative and risky calculation
#
# This representing something we are still figuring out, not ready for production.

# %%
def calculate_crazy_quantity(x: float, m: float, b: float) -> np.ndarray:
    """
    Disruptive and innovative calculation

    :param x:
        Independent variable.

    :param m:
        The rate constant associated with the independent variable.

    :param b:
        The constant displacement associated with the independent variable.

    :return:
        Some crazy quantity that nobody thought of before.
    """
    crazy_quantity = foo.a_function(x, 3) / goo.calculate_something_big(x, m, b)
    return crazy_quantity

# %% [markdown]
# A result that is really hard to understand:

# %%
breakthrough_result = calculate_crazy_quantity(2, 0.5, 1)

breakthrough_result
