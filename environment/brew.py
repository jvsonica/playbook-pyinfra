from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import server

if not host.get_fact(Which, command="brew"):
    server.shell(
        commands=["curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh | bash"],
    )
