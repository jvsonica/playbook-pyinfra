from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.operations import apt, files, git, server

if not host.get_fact(File, path="/usr/local/bin/nvim"):
    apt.packages(
        packages=["ninja-build", "gettext", "cmake", "unzip"],
        present=True,
        update=True,
        cache_time=3600,
    )

    git.repo(
        src="https://github.com/neovim/neovim.git",
        dest="/tmp/neovim",
        branch="stable",
    )

    server.shell(
        commands=[
            "cd /tmp/neovim && make CMAKE_BUILD_TYPE=RelWithDebInfo",
            "cd /tmp/neovim && make install",
        ]
    )

    files.directory(
        path="/tmp/neovim",
        present=False,
    )
