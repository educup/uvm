from os.path import join

import typer

filename_option = typer.Argument(
    join(".", "ProjectSettings", "ProjectSettings.asset"),
    exists=True,
    file_okay=True,
    dir_okay=False,
    writable=True,
    readable=True,
    resolve_path=True,
    help="Path of ProjectSettings.asset file of the Unity project",
    envvar=["UVM_FILENAME"],
)
