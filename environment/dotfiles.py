from pathlib import Path

from pyinfra.operations import git, server

home = str(Path.home())

git.repo(
    src="https://github.com/jvsonica/dotfiles.git",
    dest=f"{home}/.dotfiles",
    branch="main",
)

server.shell(f"cd {home}/.dotfiles && stow --adopt */ && git restore .")
