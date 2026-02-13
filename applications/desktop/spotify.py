from pyinfra.operations import apt

apt.key(
    src="https://download.spotify.com/debian/pubkey_6224F9941A8AA6D1.gpg",
)

apt.repo(
    src="deb http://repository.spotify.com stable non-free",
    present=True,
)

apt.packages(
    packages=["spotify-client"],
    present=True,
    update=True,
    cache_time=3600,
)
