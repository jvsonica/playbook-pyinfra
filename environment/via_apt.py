from pyinfra.operations import apt

apt.packages(
    packages=[
        "build-essential",
        "curl",
        "git",
        "python3-apt",
        "python3-pip",
        "python3-virtualenv",
        "python3-venv",
        "zsh",
        "tmux",
        "ripgrep",
        "stow",
        "fd-find",
        "unzip",
        "htop",
        "sshfs",
        "pavucontrol"
    ],
    present=True,
    update=True,
    cache_time=3600,
    _sudo=True,
)
