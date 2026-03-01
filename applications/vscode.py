from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import apt

if not host.get_fact(Which, command="code"):
    apt.deb(
        src="https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64",
        _sudo=True,
    )
