from pathlib import Path

from pyinfra.operations import files, server

home = str(Path.home())

files.download(
    src="https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Hack.zip",
    dest="/tmp/Hack.zip",
)

files.directory(
    path=f"{home}/.fonts",
    present=True,
)

server.shell(f"unzip -o /tmp/Hack.zip -d {home}/.fonts")

server.shell("fc-cache -fv")
