from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import apt

if not host.get_fact(Which, command="wezterm"):
    apt.deb(
        src=(
            "https://github.com/wez/wezterm/releases/download/"
            "20240203-110809-5046fc22/wezterm-20240203-110809-5046fc22.Ubuntu22.04.deb"
        ),
        _sudo=True,
    )
