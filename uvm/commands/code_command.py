from pathlib import Path
from typing import Optional

import typer

from ..core import Version
from ..utils import filename_option

app = typer.Typer(help="Command to manage the version code")


@app.command(name="get", help="Get the version code")
def code_get(filename: Optional[Path] = filename_option):
    version = Version.get(str(filename))
    typer.echo(f"Code: {version.code}")
    typer.echo(f"Version: {version}")


@app.command(name="setup", help="Increase the version code to the next")
def code_set_up(filename: Optional[Path] = filename_option):
    version = Version.get(str(filename))
    version.set_code_up()
    version.set(str(filename))
    typer.echo(f"Version: {version}")


@app.command(name="set", help="Set the version code")
def code_set(
    number: int = typer.Argument(..., help="Version code"),
    filename: Optional[Path] = filename_option,
):
    version = Version.get(str(filename))
    version.set_code(number)
    version.set(str(filename))
    typer.echo(f"Version: {version}")
