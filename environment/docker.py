from pathlib import Path

from pyinfra import host
from pyinfra.facts.server import Users, Which
from pyinfra.operations import apt, server

user = Path.home().name

if not host.get_fact(Which, command="docker"):
    server.shell(
        commands=[
            "install -m 0755 -d /etc/apt/keyrings",
            "curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc",
            "chmod a+r /etc/apt/keyrings/docker.asc",
        ],
        _sudo=True,
    )

    server.shell(
        commands=[
            'echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo ${UBUNTU_CODENAME:-$(echo $VERSION_CODENAME)}) stable" > /etc/apt/sources.list.d/docker.list',
        ],
        _sudo=True,
    )

    apt.update(_sudo=True)

    apt.packages(
        packages=[
            "docker-ce",
            "docker-ce-cli",
            "containerd.io",
            "docker-buildx-plugin",
            "docker-compose-plugin",
        ],
        present=True,
        update=True,
        _sudo=True,
    )

users = host.get_fact(Users)
if users and user in users:
    user_groups = users[user].get("groups", [])
    if "docker" not in user_groups:
        server.shell(commands=[f"usermod -aG docker {user}"], _sudo=True)
