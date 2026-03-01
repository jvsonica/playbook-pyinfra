from pyinfra import host
from pyinfra.facts.server import Which
from pyinfra.operations import server

if not host.get_fact(Which, command="fzf"):
    server.shell(commands=["brew install fzf"])
