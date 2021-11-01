from typing import List


import requests
import typer


__version__ = "0.1.0"


def app(names: List[str]):
    for name in names:
        url = f"https://pypi.org/project/{name}/"

        response = requests.get(url)
        if response.status_code == 404:
            typer.secho(name, nl=False, fg=typer.colors.BRIGHT_MAGENTA)
            typer.echo(" is available on PyPI 🎉")
        elif response.status_code == 200:
            typer.secho(name, nl=False, fg=typer.colors.BRIGHT_MAGENTA)
            typer.echo(" is ", nl=False)
            typer.secho("not available", nl=False, fg=typer.colors.BRIGHT_RED)
            typer.echo(" on PyPI")
        else:
            typer.secho(
                f"An error occurred: {response.status_code}",
                fg=typer.colors.BRIGHT_RED,
            )


def main():
    typer.run(app)


if __name__ == "__main__":
    main()
