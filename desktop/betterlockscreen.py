from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.operations import files, server

if not host.get_fact(File, path="/usr/local/bin/betterlockscreen"):
    files.download(
        src="https://github.com/betterlockscreen/betterlockscreen/archive/refs/heads/main.zip",
        dest="/tmp/betterlockscreen.zip",
    )

    server.shell("unzip -o /tmp/betterlockscreen.zip -d /tmp")

    server.shell("chmod +x /tmp/betterlockscreen-main/betterlockscreen")

    server.shell(
        "mv /tmp/betterlockscreen-main/betterlockscreen /usr/local/bin/betterlockscreen"
    )

    files.file(
        path="/tmp/betterlockscreen.zip",
        present=False,
    )

    files.directory(
        path="/tmp/betterlockscreen-main",
        present=False,
    )
