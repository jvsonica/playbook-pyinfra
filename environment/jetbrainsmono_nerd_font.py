from pathlib import Path

from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.operations import files, server

home = str(Path.home())

font_marker = f"{home}/.fonts/JetBrainsMonoNerdFont-Regular.ttf"

if not host.get_fact(File, path=font_marker):
    files.download(
        src="https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/JetBrainsMono.zip",
        dest="/tmp/JetBrainsMono.zip",
    )

    files.directory(
        path=f"{home}/.fonts",
        present=True,
    )

    server.shell(commands=f"unzip -o /tmp/JetBrainsMono.zip -d {home}/.fonts")

    server.shell(commands="fc-cache -fv")
