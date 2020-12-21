from pathlib import Path
from typing import Optional

import typer

from ..core import Version
from ..utils import filename_option

app = typer.Typer(help="Command to manage the version major")


@app.command(name="get", help="Get the version major")
def major_get(filename: Optional[Path] = filename_option):
    version = Version.get(str(filename))
    typer.echo(f"Major: {version.major}")
    typer.echo(f"Version: {version}")


@app.command(name="setup", help="Increase the version major to the next")
def major_set_up(filename: Optional[Path] = filename_option):
    version = Version.get(str(filename))
    version.set_major_up()
    version.set(str(filename))
    typer.echo(f"Version: {version}")


@app.command(name="set", help="Set the version major")
def major_set(
    number: int = typer.Argument(..., help="Version major"),
    filename: Optional[Path] = filename_option,
):
    version = Version.get(str(filename))
    version.set_major(number)
    version.set(str(filename))
    typer.echo(f"Version: {version}")
