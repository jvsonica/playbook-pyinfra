from pathlib import Path

from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.operations import server

home = str(Path.home())
local_zoxide = f"{home}/.local/bin/zoxide"
global_zoxide = "/usr/local/bin/zoxide"

if not host.get_fact(File, path=local_zoxide) and not host.get_fact(
    File, path=global_zoxide
):
    server.shell(
        "curl -sSfL https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh "
        "| sh -s -- --bin-dir /usr/local/bin"
    )
