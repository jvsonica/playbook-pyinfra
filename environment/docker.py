from pyinfra import host
from pyinfra.facts.server import LsbRelease, User
from pyinfra.operations import apt, files, server

lsb = host.get_fact(LsbRelease) or {}
codename = lsb.get("codename") or lsb.get("release")

name = "ubuntu"

apt.packages(
    packages=["ca-certificates", "curl"],
    present=True,
    update=True,
    cache_time=3600,
)

files.directory(
    path="/etc/apt/keyrings",
    present=True,
    mode="0755",
)

files.download(
    src=f"https://download.docker.com/linux/{name}/gpg",
    dest="/etc/apt/keyrings/docker.asc",
    mode="0644",
)

apt.repo(
    src=(
        "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] "
        f"https://download.docker.com/linux/{name} {codename} stable"
    ),
    present=True,
)

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
    cache_time=3600,
)

server.group(
    group="docker",
    present=True,
)

server.user(
    user=host.get_fact(User),
    groups=["docker"],
    append=True,
)
