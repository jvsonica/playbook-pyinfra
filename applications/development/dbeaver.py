from pyinfra.operations import apt

apt.deb(
    src="https://dbeaver.io/files/24.2.3/dbeaver-ce_24.2.3_amd64.deb",
)
