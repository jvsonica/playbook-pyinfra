from pathlib import Path

from pyinfra import host
from pyinfra.facts.files import Directory
from pyinfra.operations import apt, git, server

home = str(Path.home())
user = Path.home().name
oh_my_zsh_dir = f"{home}/.oh-my-zsh"

apt.packages(
    packages=["zsh"],
    present=True,
    update=True,
    cache_time=3600,
    _sudo=True,
)

if not host.get_fact(Directory, path=oh_my_zsh_dir):
    server.shell(commands=["curl -sL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh | bash -"])

git.repo(
    src="https://github.com/zsh-users/zsh-autosuggestions",
    dest=f"{home}/.oh-my-zsh/custom/plugins/zsh-autosuggestions",
)

git.repo(
    src="https://github.com/zsh-users/zsh-syntax-highlighting",
    dest=f"{home}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting",
)

git.repo(
    src="https://github.com/joshskidmore/zsh-fzf-history-search",
    dest=f"{home}/.oh-my-zsh/custom/plugins/zsh-fzf-history-search",
)

server.shell(commands=[f"chsh -s /bin/zsh {user}"], _sudo=True)
