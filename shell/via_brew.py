from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import server

BREW_PACKAGES = [
    "jq",
    "awscli",
    "fzf",
    "zoxide",
]


def _is_installed(cmd: str) -> bool:
    return host.get_fact(Which, command=cmd)


for pkg in BREW_PACKAGES:
    if not _is_installed(pkg):
        server.shell(commands=[f"brew install {pkg}"])
