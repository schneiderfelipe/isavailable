from functools import reduce
from typing import List, Optional


import requests
import typer


__version__ = "0.1.0"


def isavailable(name: str) -> bool:
    url = f"https://pypi.org/project/{name}/"
    response = requests.get(url)
    if response.status_code == 404:
        return True
    elif response.status_code == 200:
        return False
    else:
        typer.secho(
            f"An error occurred: {response.status_code}", fg=typer.colors.BRIGHT_RED
        )
        raise typer.Exit(response.status_code)


def echo_name(name: str, width: Optional[int] = None, nl: bool = True):
    if not width:
        typer.secho(name, nl=nl, fg=typer.colors.BRIGHT_MAGENTA)
    else:
        typer.secho(name, nl=False, fg=typer.colors.BRIGHT_MAGENTA)
        typer.echo(" " * (width - len(name)), nl=nl)


def app(names: List[str]):
    width = reduce(max, map(len, names))
    for name in sorted(names, key=len):
        echo_name(name, width=width, nl=False)
        typer.echo(" is… ", nl=False)
        if isavailable(name):
            typer.secho("    available 🎉", nl=False, fg=typer.colors.BRIGHT_GREEN)
        else:
            typer.secho("not available 😭", nl=False, fg=typer.colors.BRIGHT_RED)
        typer.echo(" on PyPI.")


def main():
    typer.run(app)


if __name__ == "__main__":
    main()
