from pathlib import Path
from typing import Optional

import typer

from ..core import Version
from ..utils import filename_option

app = typer.Typer(help="Command to manage the version build")


@app.command(name="get", help="Get the version build")
def build_get(filename: Optional[Path] = filename_option):
    version = Version.get(str(filename))
    typer.echo(f"Build: {version.build}")
    typer.echo(f"Version: {version}")


@app.command(name="setup", help="Increase the version build to the next")
def build_set_up(filename: Optional[Path] = filename_option):
    version = Version.get(str(filename))
    version.set_build_up()
    version.set(str(filename))
    typer.echo(f"Version: {version}")


@app.command(name="set", help="Set the version build")
def build_set(
    number: int = typer.Argument(..., help="Version build"),
    filename: Optional[Path] = filename_option,
):
    version = Version.get(str(filename))
    version.set_build(number)
    version.set(str(filename))
    typer.echo(f"Version: {version}")
