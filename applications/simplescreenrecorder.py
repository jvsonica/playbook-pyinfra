from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import apt

if not host.get_fact(Which, command="simplescreenrecorder"):
    apt.packages(
        packages=["simplescreenrecorder"],
        present=True,
        update=True,
        _sudo=True,
    )
