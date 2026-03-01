from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import apt, files, server

if not host.get_fact(Which, command="i3lock"):
    apt.packages(
        packages=[
            "autoconf",
            "gcc",
            "make",
            "pkg-config",
            "libpam0g-dev",
            "libcairo2-dev",
            "libfontconfig1-dev",
            "libxcb-composite0-dev",
            "libev-dev",
            "libx11-xcb-dev",
            "libxcb-xkb-dev",
            "libxcb-xinerama0-dev",
            "libxcb-image0-dev",
            "libxcb-util-dev",
            "libxcb-xrm-dev",
            "libxkbcommon-dev",
            "libxkbcommon-x11-dev",
            "libjpeg-dev",
            "libgif-dev",
        ],
        present=True,
        update=True,
        _sudo=True,
    )

    server.shell(
        commands=[
            "git clone https://github.com/Raymo111/i3lock-color.git /tmp/i3lock-color"
        ],
    )

    server.shell(
        commands=["cd /tmp/i3lock-color && ./install-i3lock-color.sh"],
        _sudo=True,
    )

    files.directory(
        path="/tmp/i3lock-color",
        present=False,
    )
