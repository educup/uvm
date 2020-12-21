from pathlib import Path
from typing import Optional

import typer

from .commands.build_command import app as build_app
from .commands.code_command import app as code_app
from .commands.major_command import app as major_app
from .commands.minor_command import app as minor_app
from .commands.patch_command import app as patch_app
from .core import Version
from .utils import filename_option

app = typer.Typer(help="Unity Version Manager CLI implemented with Python and Typer")

app.add_typer(code_app, name="code")
app.add_typer(build_app, name="build")
app.add_typer(patch_app, name="patch")
app.add_typer(minor_app, name="minor")
app.add_typer(major_app, name="major")


@app.command(name="get", help="Get the version")
def get(filename: Optional[Path] = filename_option):
    version = Version.get(str(filename))
    typer.echo(f"Version: {version}")


@app.command(name="set", help="Set the version")
def set(
    arg: str = typer.Argument(
        ...,
        help='The format must be "*.*.*b*(*)" where * is the major, minor, patch, '
        + "build and code respectively and all integers.",
    ),
    filename: Optional[Path] = filename_option,
):
    version = Version.parse(arg)
    if version is None:
        typer.echo(
            "Version format is invalid.\n"
            + 'The format must be "*.*.*b*(*)" where * is the major,\n'
            + "minor, patch, build and code respectively and all integers.",
            err=True,
        )
    else:
        version.set(str(filename))
        typer.echo(f"Version: {version}")
