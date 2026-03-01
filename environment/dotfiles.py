from pathlib import Path

from pyinfra.operations import git

home = str(Path.home())

git.repo(
    src="https://github.com/jvsonica/dotfiles.git",
    dest=f"{home}/Documents/projects/dotfiles",
    branch="master",
)

# server.shell(f"cd {home}/.dotfiles && stow --adopt */ && git restore .")
