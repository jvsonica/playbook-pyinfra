from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.operations import files, server

if not host.get_fact(File, path="/usr/local/bin/smug"):
    files.download(
        src="https://github.com/ivaaaan/smug/releases/download/v0.3.5/smug.0.3.5._Linux_x86_64.tar.gz",
        dest="/tmp/smug.tar.gz",
    )

    files.directory(
        path="/tmp/smug",
        present=True,
    )

    server.shell("tar -xzf /tmp/smug.tar.gz -C /tmp/smug")

    server.shell("mv /tmp/smug/smug /usr/local/bin/smug")

    files.directory(
        path="/tmp/smug",
        present=False,
    )

    files.file(
        path="/tmp/smug.tar.gz",
        present=False,
    )
