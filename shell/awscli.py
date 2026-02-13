from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.operations import files, server

if not host.get_fact(File, path="/usr/local/bin/aws"):
    files.download(
        src="https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip",
        dest="/tmp/awscliv2.zip",
    )

    server.shell("unzip -o /tmp/awscliv2.zip -d /tmp")

    server.shell("/tmp/aws/install")

    files.file(
        path="/tmp/awscliv2.zip",
        present=False,
    )

    files.directory(
        path="/tmp/aws",
        present=False,
    )
