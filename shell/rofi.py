from pathlib import Path

from pyinfra.operations import apt, files, git, server

home = str(Path.home())

apt.packages(
    packages=["rofi"],
    present=True,
    update=True,
    cache_time=3600,
)

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
    f"cp -r /tmp/rofi-themes-collection/themes/* {home}/.local/share/rofi/themes/"
)

files.directory(
    path="/tmp/rofi-themes-collection",
    present=False,
)
