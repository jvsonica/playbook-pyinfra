from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import apt, server

if not host.get_fact(Which, command="spotify"):
    server.shell(
        commands="curl -sS https://download.spotify.com/debian/pubkey_5384CE82BA52C83A.asc | gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg",
        _sudo=True,
    )

    server.shell(
        commands="echo 'deb https://repository.spotify.com stable non-free' > /etc/apt/sources.list.d/spotify.list",
        _sudo=True,
    )

    apt.update(_sudo=True)

    apt.packages(
        packages=["spotify-client"],
        present=True,
        update=True,
        _sudo=True,
    )
