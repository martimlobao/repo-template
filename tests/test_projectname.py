import tomllib
from pathlib import Path
from typing import TYPE_CHECKING, Any

from projectname import __version__

if TYPE_CHECKING:
    import io


def test_version() -> None:
    file_: io.BufferedReader
    with Path("pyproject.toml").open("rb") as file_:
        project_meta: dict[str, Any] = tomllib.load(file_)

    assert __version__ == project_meta["tool"]["poetry"]["version"]
