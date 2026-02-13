from pathlib import Path

from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.operations import server

home = str(Path.home())
local_starship = f"{home}/.local/bin/starship"
global_starship = "/usr/local/bin/starship"

if not host.get_fact(File, path=local_starship) and not host.get_fact(
    File, path=global_starship
):
    server.shell("curl -sS https://starship.rs/install.sh | sh -s -- -y")
