from pathlib import Path
from typing import Optional

import typer

from ..core import Version
from ..utils import filename_option

app = typer.Typer(help="Command to manage the version patch")


@app.command(name="get", help="Get the version patch")
def patch_get(filename: Optional[Path] = filename_option):
    version = Version.get(str(filename))
    typer.echo(f"Patch: {version.patch}")
    typer.echo(f"Version: {version}")


@app.command(name="setup", help="Increase the version patch to the next")
def patch_set_up(filename: Optional[Path] = filename_option):
    version = Version.get(str(filename))
    version.set_patch_up()
    version.set(str(filename))
    typer.echo(f"Version: {version}")


@app.command(name="set", help="Set the version patch")
def patch_set(
    number: int = typer.Argument(..., help="Version patch"),
    filename: Optional[Path] = filename_option,
):
    version = Version.get(str(filename))
    version.set_patch(number)
    version.set(str(filename))
    typer.echo(f"Version: {version}")
