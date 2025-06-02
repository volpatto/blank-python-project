# %% [markdown]
# # A fancy demonstration
#
# This notebook demonstrates how to incorporate ipynb files both as tests and docs. Just imagine that we have a bunch of important and fancy calculations and explanations.

# %% [markdown]
# ## Loading the dependencies
#
# This is all the packages that we will need to solve the _amazing_ problems considered in this study.

# %%
from mypackage import foo, goo

# %% [markdown]
# ## Solving fancy problems with `foo`
#
# Note that `foo` is already covered in test files.

# %%
important_output = foo.a_function(1, 3)

print(f"The output is {important_output}")

# %% [markdown]
# ## Solving challenging problems with `goo`
#
# The `goo` module is not covered by usual `pytest` test files. So, if this notebooks works properly, the cell below should works as a test and the coverage should be extended considering the usage of `goo` here.

# %%
hard_solution = goo.calculate_something_big(2, 1, 5)

print(f"The Nobel prize worthy solution is {hard_solution}")
