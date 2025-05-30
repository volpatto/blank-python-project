import shlex
import glob
import shutil
from invoke import task, exceptions
from rich import print

import platform

from pathlib import Path


_HOST_SYSTEM = platform.system()
_SUPPORTED_SYSTEMS = (
    "Windows",
    "Linux",
    "Darwin",
)
_PACKAGE_NAME = "mypackage"


def _task_screen_log(message: str, bold: bool = True, color: str = "blue") -> None:
    """
    Convenient function to display a message on terminal during task executions.
    """
    rich_delimiters = f"bold {color}" if bold else f"{color}"
    print(f"[{rich_delimiters}]{message}[/{rich_delimiters}]")


@task(
    help={
        "verbose": "Run pytest in verbose mode",
        "color": "Colorize pytest output",
        "check_coverage": "Display coverage summary table after running the tests",
        "generate_report": "Generate pytest report and save it as a xml file (named pytest.xml)",
        "generate_cov_xml": "Generate coverage report and save it as a xml file (named coverage.xml)",
        "cov_append": "Append coverage output to existing coverage file",
    },
)
def tests_ipynb(
    ctx,
    verbose=True,
    color=True,
    check_coverage=False,
    generate_cov_xml=False,
    generate_report=False,
    cov_append=False,
):
    """
    Run notebooks as regression tests for each cell.
    """
    task_output_message = "Running notebooks as tests"
    _task_screen_log(task_output_message)

    base_command = "pytest -ra -q --nbval notebooks/supported"

    if verbose:
        base_command += " -v"

    if color:
        base_command += " --color=yes"

    check_coverage_msg = ""
    if check_coverage:
        check_coverage_msg += f"--cov={_PACKAGE_NAME}"
        base_command += f" {check_coverage_msg}"

    generate_report_cmd = ""
    if generate_report:
        generate_report_cmd = "--junitxml=pytest.xml"
        if check_coverage:
            base_command += f" {generate_report_cmd}"
        else:
            base_command += f" --cov={_PACKAGE_NAME} {generate_report_cmd}"

    generate_cov_xml_cmd = ""
    if generate_cov_xml:
        generate_cov_xml_cmd = "--cov-report xml:coverage.xml"
        base_command += f" {generate_cov_xml_cmd}"

    if generate_report or generate_cov_xml:
        base_command += " --cov-report=term-missing:skip-covered"

    if cov_append:
        base_command += " --cov-append"

    host_system = _HOST_SYSTEM
    if host_system not in _SUPPORTED_SYSTEMS:
        raise exceptions.Exit(f"{_PACKAGE_NAME} is running on unsupported operating system", code=1)

    _task_screen_log(f"Running: {base_command}", color="yellow", bold=False)
    pty_flag = True if host_system != "Windows" else False
    ctx.run(base_command, pty=pty_flag)


@task(
    help={
        "numprocess": "Num of processes to run pytest in parallel",
        "verbose": "Run pytest in verbose mode",
        "color": "Colorize pytest output",
        "check_coverage": "Display coverage summary table after running the tests",
        "generate_report": "Generate pytest report and save it as a xml file (named pytest.xml)",
        "generate_cov_xml": "Generate coverage report and save it as a xml file (named coverage.xml)",
        "record_output": "Record all the pytest CLI output to pytest-coverage.txt file",
    },
    optional=["numprocess"],
)
def tests(
    ctx,
    numprocess=-1,
    verbose=True,
    color=True,
    check_coverage=False,
    generate_cov_xml=False,
    generate_report=False,
    record_output=False,
    # ipynb=True,
):
    """
    Run tests with pytest.
    """
    task_output_message = "Running the tests"
    _task_screen_log(task_output_message)

    base_command = "pytest -ra -q"
    if verbose:
        base_command += " -v"

    if color:
        base_command += " --color=yes"

    if numprocess != 1:
        base_command += " -n"
        if numprocess == -1:
            base_command += " auto"
        elif numprocess > 1:
            base_command += f" {int(numprocess)}"
        else:
            _task_screen_log(
                "Warning: there is no negative number of processes. Setting to 1 (serial).",
                color="yellow",
            )
            base_command += " 1"

    check_coverage_msg = ""
    if check_coverage:
        check_coverage_msg += f"--cov={_PACKAGE_NAME}"
        base_command += f" {check_coverage_msg}"

    generate_report_cmd = ""
    if generate_report:
        generate_report_cmd = "--junitxml=pytest.xml"
        if check_coverage:
            base_command += f" {generate_report_cmd}"
        else:
            base_command += f" --cov={_PACKAGE_NAME} {generate_report_cmd}"

    generate_cov_xml_cmd = ""
    if generate_cov_xml:
        generate_cov_xml_cmd = "--cov-report xml:coverage.xml"
        base_command += f" {generate_cov_xml_cmd}"

    if generate_report or generate_cov_xml:
        base_command += " --cov-report=term-missing:skip-covered"

    if record_output:
        base_command += " | tee pytest-coverage.txt"

    host_system = _HOST_SYSTEM
    if host_system not in _SUPPORTED_SYSTEMS:
        raise exceptions.Exit(f"{_PACKAGE_NAME} is running on unsupported operating system", code=1)

    _task_screen_log(f"Running: {base_command}", color="yellow", bold=False)
    pty_flag = True if host_system != "Windows" else False
    ctx.run(base_command, pty=pty_flag)


@task
def diff_coverage(ctx):
    """
    Run diff_cover to verify if all new code is covered. Needs a coverage.xml file.
    """
    task_output_message = "Check if diff code is covered"
    _task_screen_log(task_output_message)

    base_command = "diff-cover coverage.xml --config-file pyproject.toml"
    _task_screen_log(f"Running: {base_command}", color="yellow", bold=False)

    host_system = _HOST_SYSTEM
    if host_system not in _SUPPORTED_SYSTEMS:
        raise exceptions.Exit(f"{_PACKAGE_NAME} is running on unsupported operating system", code=1)
    pty_flag = True if host_system != "Windows" else False
    ctx.run(base_command, pty=pty_flag)


@task(
    help={
        "color": "Display output with colors",
        "pretty": "Enable better and colorful mypy output",
        "verbose": "Run mypy in verbose mode",
        "files": "Files to be checked with mypy",
    }
)
def type_check(ctx, pretty=False, verbose=False, color=True, files=""):
    """
    Run mypy on mypackage to check for typing issues.
    """
    task_output_message = f"Running typing check on {_PACKAGE_NAME}"
    _task_screen_log(task_output_message)

    base_command = "mypy"
    if pretty:
        base_command += " --pretty"

    if verbose:
        base_command += " --verbose"

    if color:
        base_command += " --color-output"

    if files != "":
        base_command += f" {files}"

    _task_screen_log(f"Running: {base_command}", color="yellow", bold=False)

    host_system = _HOST_SYSTEM
    if host_system not in _SUPPORTED_SYSTEMS:
        raise exceptions.Exit(f"{_PACKAGE_NAME} is running on unsupported operating system", code=1)
    pty_flag = True if host_system != "Windows" else False
    ctx.run(base_command, pty=pty_flag)


@task(help={"overwrite": "Reinstall git hooks overwriting the previous installation."})
def hooks(ctx, overwrite=False):
    """
    Configure pre-commit in the local git.
    """
    task_output_message = "Installing pre-commit hooks"
    _task_screen_log(task_output_message)
    base_command = "pre-commit install"

    if overwrite:
        base_command += " --overwrite"

    _task_screen_log(f"Running: {base_command}", color="yellow", bold=False)
    ctx.run(base_command)


@task(
    pre=[hooks],
    help={
        "all_files": "Run git hooks in all files (may take some time)",
        "files": "Run git hooks in a given set of files",
        "verbose": "Run git hooks in verbose mode",
        "from_ref": "(for usage with `--to-ref`) -- this option represents the original ref in a `from_ref...to_ref` diff expression. For `pre-push` hooks, this represents the branch you are pushing to. For `post-checkout` hooks, this represents the branch that was previously checked out.",
        "to_ref": "(for usage with `--from-ref`) -- this option represents the destination ref in a `from_ref...to_ref` diff expression. For `pre-push` hooks, this represents the branch being pushed. For `post-checkout` hooks, this represents the branch that is now checked out.",
    },
)
def run_hooks(ctx, all_files=False, verbose=False, files="", from_ref="", to_ref=""):
    """
    Run all the installed git hooks in all.
    """
    task_output_message = "Run installed git hooks"
    _task_screen_log(task_output_message)
    base_command = "pre-commit run"
    if all_files:
        base_command += " --all-files"

    if verbose:
        base_command += " --verbose"

    if files != "":
        base_command += f" --files '{files}'"

    if from_ref != "":
        base_command += f" --from-ref {from_ref}"

    if to_ref != "":
        base_command += f" --to-ref {to_ref}"

    _task_screen_log(f"Running: {base_command}", color="yellow", bold=False)
    host_system = _HOST_SYSTEM
    if host_system not in _SUPPORTED_SYSTEMS:
        raise exceptions.Exit(f"{_PACKAGE_NAME} is running on unsupported operating system", code=1)
    pty_flag = True if host_system != "Windows" else False
    ctx.run(base_command, pty=pty_flag)


@task
def dev_install(ctx):
    """
    Install the package in the environment. Warning: use when developing with virtualenv only.
    """
    task_output_message = "Installing the package in the active environment"
    _task_screen_log(task_output_message)
    base_command = 'pip install -e ".[dev]"'
    host_system = _HOST_SYSTEM
    if host_system not in _SUPPORTED_SYSTEMS:
        raise exceptions.Exit(f"{_PACKAGE_NAME} is running on unsupported operating system", code=1)
    pty_flag = True if host_system != "Windows" else False
    ctx.run(base_command, pty=pty_flag)


@task
def docs_install(ctx):
    """
    Install the docs dependencies in the venv. Warning: use when developing with virtualenv only.
    """
    task_output_message = "Installing the docs dependencies in the active environment"
    _task_screen_log(task_output_message)
    base_command = 'pip install -e ".[docs]"'
    host_system = _HOST_SYSTEM
    if host_system not in _SUPPORTED_SYSTEMS:
        raise exceptions.Exit(f"{_PACKAGE_NAME} is running on unsupported operating system", code=1)
    pty_flag = True if host_system != "Windows" else False
    ctx.run(base_command, pty=pty_flag)


@task(
    help={
        "dry": "Show what would be removed without actually deleting",
    }
)
def clean(ctx, dry=False):
    """
    Remove build/config dirs:
      - mypackage.egg-info
      - dist
      - build
      - *_cache
      - site
    """
    patterns = [
        "*.egg-info",
        "dist",
        "build",
        "*_cache",
        "site",
    ]

    # Collect all matching dirs
    exclude_root = ".venv"  # we need to skip changes in .venv
    to_remove = []
    for pat in patterns:
        for d in Path(".").rglob(pat):
            if not d.is_dir():
                continue
            # skip .venv
            if exclude_root in d.parts:
                continue
            to_remove.append(d)

    if not to_remove:
        _task_screen_log("Nothing to clean.", color="yellow")
        return

    for d in to_remove:
        _task_screen_log(f"{'Would remove:' if dry else 'Removing:  '}{d}", color="yellow")
        if not dry:
            shutil.rmtree(d)

    _task_screen_log(
        f"\n{len(to_remove)} director{'y' if len(to_remove) == 1 else 'ies'} {'would be removed' if dry else 'removed'}.",
        color="yellow",
    )


@task(
    help={
        "verbose": "Build docs with verbose mode",
        "clean": "Clean build of the docs, rebuilding the files",
        "quiet": "Silence warnings",
        "include-ipynb": "Collect and add supported notebooks as docs",
    }
)
def build_docs(ctx, verbose=False, clean=True, quiet=False, include_ipynb=False):
    """
    Builds the docs file to be deployed.

    Warning: use when developing with virtualenv only.
    """
    task_output_message = "Building the docs file"
    _task_screen_log(task_output_message)
    base_command = "mkdocs build"

    if clean:
        base_command += " --clean"
    else:
        base_command += " --dirty"

    if verbose:
        base_command += " --verbose"

    if quiet:
        base_command += " --quiet"

    # We need to move or create symlinks to ipynbs files, moving them to
    # docs, otherwise mkdocs will be unable to reach them
    if include_ipynb:
        ipynbs_path = Path("notebooks/supported")
        target_ipynbs_dir = Path("docs/notebooks")

        if not ipynbs_path.exists():
            raise exceptions.Exit(f"Notebook source not found: {ipynbs_path}", 1)

        # Ensure parent exists
        target_ipynbs_dir.parent.mkdir(parents=True, exist_ok=True)

        # Blow away any old copy
        if target_ipynbs_dir.exists():
            shutil.rmtree(target_ipynbs_dir)

        # Copy everything under notebooks/supported → docs/notebooks
        shutil.copytree(ipynbs_path, target_ipynbs_dir)

        _task_screen_log(
            f"Included notebooks from {ipynbs_path} → {target_ipynbs_dir}", color="yellow"
        )

    host_system = _HOST_SYSTEM
    if host_system not in _SUPPORTED_SYSTEMS:
        raise exceptions.Exit(f"{_PACKAGE_NAME} is running on unsupported operating system", code=1)
    pty_flag = True if host_system != "Windows" else False
    ctx.run(base_command, pty=pty_flag)


@task
def deploy_docs_local(ctx):
    """
    Deploy MkDocs pages locally.
    """
    task_output_message = "Deploying Docs locally"
    _task_screen_log(task_output_message)
    base_command = "mkdocs serve"
    host_system = _HOST_SYSTEM
    if host_system not in _SUPPORTED_SYSTEMS:
        raise exceptions.Exit(f"{_PACKAGE_NAME} is running on unsupported operating system", code=1)
    pty_flag = True if host_system != "Windows" else False
    ctx.run(base_command, pty=pty_flag, echo=True)


@task(pre=[docs_install])
def deploy_docs_gh(ctx):
    """
    Deploy MkDocs pages to Github.
    """
    task_output_message = "Deploying Docs to Github"
    _task_screen_log(task_output_message)
    base_command = "mkdocs gh-deploy"
    host_system = _HOST_SYSTEM
    if host_system not in _SUPPORTED_SYSTEMS:
        raise exceptions.Exit(f"{_PACKAGE_NAME} is running on unsupported operating system", code=1)
    pty_flag = True if host_system != "Windows" else False
    ctx.run(base_command, pty=pty_flag, echo=True)


@task(
    help={
        "src": "Glob pattern(s) or list of .ipynb paths to pair (default: notebooks/*.ipynb)",
        "dry": "Preview only (no files will be changed)",
    }
)
def pair_ipynbs(ctx, src="notebooks/**/*.ipynb", dry=False):
    """
    Pair Jupyter notebooks with Python scripts (percent‐format).
    """
    _task_screen_log("Pairing notebooks with Python scripts")

    # Gather files
    if isinstance(src, str):
        raw = glob.glob(src, recursive=True)
    else:
        raw = list(src)
    notebooks = [Path(p) for p in raw if Path(p).suffix == ".ipynb"]
    if not notebooks:
        raise exceptions.Exit(f"No notebooks found for {src}", 1)

    # Run pairing
    for nb in notebooks:
        print(f"{'Would pair:' if dry else 'Pairing:'} {nb}")
        if not dry:
            cmd = ["jupytext", "--set-formats", "ipynb,py:percent", str(nb)]
            ctx.run(" ".join(shlex.quote(x) for x in cmd), pty=(_HOST_SYSTEM != "Windows"))

    print(f"{len(notebooks)} notebook(s) {'would be paired' if dry else 'paired'}.")
