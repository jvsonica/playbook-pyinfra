from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import apt

if not host.get_fact(Which, command="obsidian"):
    apt.deb(
        src=(
            "https://github.com/obsidianmd/obsidian-releases/releases/download/"
            "v1.7.4/obsidian_1.7.4_amd64.deb"
        ),
        _sudo=True,
    )
