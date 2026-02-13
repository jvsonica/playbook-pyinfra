from pyinfra.operations import apt

apt.deb(
    src=(
        "https://github.com/wez/wezterm/releases/download/"
        "20240203-110809-5046fc22/wezterm-20240203-110809-5046fc22.Ubuntu22.04.deb"
    ),
)
