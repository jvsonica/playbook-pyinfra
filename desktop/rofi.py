from pathlib import Path

from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import files, git, server

home = str(Path.home())

if not host.get_fact(Which, command="rofi"):
    server.shell(commands=["brew install rofi"])

git.repo(
    src="https://github.com/lr-tech/rofi-themes-collection.git",
    dest="/tmp/rofi-themes-collection",
    pull=False,
)

files.directory(
    path=f"{home}/.local/share/rofi/themes",
    present=True,
)

server.shell(
    commands=[
        f"cp -r /tmp/rofi-themes-collection/themes/* {home}/.local/share/rofi/themes/"
    ]
)

files.directory(
    path="/tmp/rofi-themes-collection",
    present=False,
)
