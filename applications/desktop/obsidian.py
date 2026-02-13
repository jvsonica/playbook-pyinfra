from pyinfra.operations import apt

apt.deb(
    src=(
        "https://github.com/obsidianmd/obsidian-releases/releases/download/"
        "v1.7.4/obsidian_1.7.4_amd64.deb"
    ),
)
