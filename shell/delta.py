from pyinfra.operations import apt

apt.deb(
    src="https://github.com/dandavison/delta/releases/download/0.18.2/git-delta_0.18.2_amd64.deb",
)
