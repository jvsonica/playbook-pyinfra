from pathlib import Path

from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.operations import server

home = str(Path.home())
local_mise = f"{home}/.local/bin/mise"
global_mise = "/usr/local/bin/mise"

if not host.get_fact(File, path=local_mise) and not host.get_fact(
    File, path=global_mise
):
    server.shell("curl -sSf https://mise.run | sh")
