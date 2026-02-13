from pyinfra.operations import apt

apt.deb(
    src="https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64",
)
