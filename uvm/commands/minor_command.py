from pathlib import Path
from typing import Optional

import typer

from ..core import Version
from ..utils import filename_option

app = typer.Typer(help="Command to manage the version minor")


@app.command(name="get", help="Get the version minor")
def minor_get(filename: Optional[Path] = filename_option):
    version = Version.get(str(filename))
    typer.echo(f"Minor: {version.minor}")
    typer.echo(f"Version: {version}")


@app.command(name="setup", help="Increase the version minor to the next")
def minor_set_up(filename: Optional[Path] = filename_option):
    version = Version.get(str(filename))
    version.set_minor_up()
    version.set(str(filename))
    typer.echo(f"Version: {version}")


@app.command(name="set", help="Set the version minor")
def minor_set(
    number: int = typer.Argument(..., help="Version minor"),
    filename: Optional[Path] = filename_option,
):
    version = Version.get(str(filename))
    version.set_minor(number)
    version.set(str(filename))
    typer.echo(f"Version: {version}")
