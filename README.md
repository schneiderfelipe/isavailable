# 😻 isavailable

> Can I haz this Python package on [PyPI][pypi]?

![Can I haz this Python package on PyPI?](i-can-haz-please.jpg)

Check if Python package names are available on [PyPI][pypi].

[pypi]: https://pypi.org/

## Usage

```bash
$ isavailable checks whether your desired package name is available on pypi
is        is… not available 😭 on PyPI.
on        is… not available 😭 on PyPI.
your      is… not available 😭 on PyPI.
name      is…     available 🎉 on PyPI.
pypi      is… not available 😭 on PyPI.
checks    is… not available 😭 on PyPI.
whether   is…     available 🎉 on PyPI.
desired   is…     available 🎉 on PyPI.
package   is… not available 😭 on PyPI.
available is…     available 🎉 on PyPI.
```

## Installation

```bash
$ pip install isavailable
```

## Help

```bash
$ isavailable --help
Usage: isavailable [OPTIONS] NAMES...

  Check if a list of package names are available on PyPI.

Arguments:
  NAMES...  [required]

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```
