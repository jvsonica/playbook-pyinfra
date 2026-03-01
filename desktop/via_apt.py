from pyinfra.operations import apt

apt.packages(
    packages=[
        "i3",
        "feh",
        "dunst",
        "polybar",
        "dmenu",
        "imagemagick",
        "fontconfig",
    ],
    present=True,
    update=True,
    cache_time=3600,
    _sudo=True,
)
