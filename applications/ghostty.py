from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import apt

if not host.get_fact(Which, command="ghostty"):
    apt.deb(
        src=(
            "https://github.com/mkasberg/ghostty-ubuntu/releases/download/"
            "1.3.1-0-ppa2/ghostty_1.3.1-0.ppa2_amd64_24.04.deb"
        ),
        _sudo=True,
    )
