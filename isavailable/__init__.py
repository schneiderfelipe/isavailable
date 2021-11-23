"""Check Python package distribution name availability on PyPI."""


from functools import reduce
from typing import List, Optional


import requests
import typer


__version__ = "0.1.2"


def isavailable(name: str) -> bool:
    """Check if a package is available on PyPI."""
    url = f"https://pypi.org/project/{name}/"
    response = requests.get(url)
    if response.status_code == 404:
        return False
    elif response.status_code == 200:
        return True
    else:
        typer.secho(
            f"An error occurred: {response.status_code}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(response.status_code)


def echo_name(name: str, width: Optional[int] = None, nl: bool = True):
    """Echo a name with a given width and possibly newline."""
    if not width:
        typer.secho(name, nl=nl, fg=typer.colors.BRIGHT_MAGENTA)
    else:
        typer.secho(name, nl=False, fg=typer.colors.BRIGHT_MAGENTA)
        typer.echo(" " * (width - len(name)), nl=nl)


def app(names: List[str]):
    """Check if a list of package names are available on PyPI."""
    width = reduce(max, map(len, names))
    for name in sorted(names, key=len):
        echo_name(name, width=width, nl=False)
        typer.echo(" is… ", nl=False)
        if isavailable(name):
            typer.secho("    available 🎉", nl=False, fg=typer.colors.GREEN)
        else:
            typer.secho("not available 😭", nl=False, fg=typer.colors.RED)
        typer.echo(" on PyPI.")


def main():
    """Run the app."""
    typer.run(app)


if __name__ == "__main__":
    main()
