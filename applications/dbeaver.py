from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import apt

if not host.get_fact(Which, command="dbeaver"):
    apt.deb(
        # src="https://dbeaver.io/files/24.2.3/dbeaver-ce_24.2.3_amd64.deb",
        src="https://dbeaver.io/files/dbeaver-ce_latest_amd64.deb",
        _sudo=True,
    )
