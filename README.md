# A generic blank Python project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests using conda](https://github.com/volpatto/blank-python-project/actions/workflows/tests-conda.yml/badge.svg)](https://github.com/volpatto/blank-python-project/actions/workflows/tests-conda.yml)
[![Tests using venv](https://github.com/volpatto/blank-python-project/actions/workflows/tests-venv.yml/badge.svg)](https://github.com/volpatto/blank-python-project/actions/workflows/tests-venv.yml)
[![Coverage badge](https://raw.githubusercontent.com/volpatto/blank-python-project/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/volpatto/blank-python-project/blob/python-coverage-comment-action-data/htmlcov/index.html)
[![Publish docs via GitHub Pages](https://github.com/volpatto/blank-python-project/actions/workflows/publish-docs.yml/badge.svg)](https://github.com/volpatto/blank-python-project/actions/workflows/publish-docs.yml)
[![CodeQL Analyzes](https://github.com/volpatto/blank-python-project/actions/workflows/codeql.yml/badge.svg)](https://github.com/volpatto/blank-python-project/actions/workflows/codeql.yml)

This repo provides a scratch of a Python project. Its purpose is to serve as starting point for the development of a Python project based on a minimal working structure.

## Covered features

* A Python package organized following the [src-layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/#src-layout-vs-flat-layout);
* A preconfigured `pyproject.toml` file following the suggestions from [the Official Python Packaging docs](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/);
* [GitHub Actions](https://github.com/features/actions) convenient workflows with minimal configurations for the latest Ubuntu, macOS, and Windows;
* Tests with [pytest](https://docs.pytest.org/en/latest/), integrating Python notebooks as tests together with the usual `test_*.py` files;
* Development environment with two options:
    * The classic [venv](https://docs.python.org/3.12/library/venv.html)
    * A [conda/miniconda](https://conda.io/en/latest/) environment with [conda-devenv](https://github.com/ESSS/conda-devenv) extension
* Hierarchical structure to a Python package inspired by [PyPA recommendations](https://github.com/pypa/sampleproject). See also the [Official Python docs](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/);
* A [MkDocs](https://www.mkdocs.org/) for nice-looking and modern docs (at least at the moment that you are reading this). A GH Actions workflow is provided to automatically update the docs after each PR based on docstrings and Jupyter Notebooks. See the [Docs website here](https://volpatto.github.io/blank-python-project/);
* [pre-commit](https://pre-commit.com/) to perform git hooks before commits. A GH Actions workflow is provided to check and update the hooks on a weekly basis, opening PRs by `github-actions[bot]`. The following plugins are being used as git hooks:
    * trailing-whitespace
    * end-of-file-fixer
    * ruff
    * blacken-docs
    * nb-clean
    * jupytext
* A free Coverage reporter using [this Action](https://github.com/py-cov-action/python-coverage-comment-action/tree/main). It comments on PR, annotates where there is a lack of coverage, and provides coverage badges in a dedicated branch after PRs;
* Type-checking with [mypy](https://mypy-lang.org/);
* A bunch of convenient tasks to improve productivity defined using [invoke](https://docs.pyinvoke.org/en/stable/);
* Automated Python Package releases to PyPI through Pre-Release PRs using git tags. The release is uploaded using [this official GH Action](https://github.com/pypa/gh-action-pypi-publish);
* A PR automerge workflow (based on [this GH Actions](https://github.com/pascalgn/automerge-action)) for when a PR is ready to go with all reviews, code changes, and checks done. Just label the PR with `automerge` and see the magic;
* Use [conda-lock](https://github.com/conda/conda-lock) when working with `conda` envs, assuring fully reproducible envs for Windows, Ubuntu, and MacOS. A GH Actions workflow is also provided to update conda-lock files on a weekly basis, opening PRs with updates whenever needed;
* Run [CodeQL](https://github.com/github/codeql) to analyze the code and report security issues;
* [Dependabot](https://docs.github.com/en/code-security/dependabot) is configured to watch and send PRs updating the GH Actions versions.

## Contributions

Contributions are VERY welcome. But please be aware of the purpose of the repo: **A minimal working structure.** If you want to add a feature that is very particular to your needs, please analyse if it fits the goals of this template.

Suggestions and advice are welcome; feel free to open an Issue or send me an email.

## Contact

My name is Diego. Feel free to contact me through the email <volpatto@lncc.br>.
