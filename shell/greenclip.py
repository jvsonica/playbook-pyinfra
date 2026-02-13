from pyinfra.operations import files

files.download(
    src="https://github.com/erebe/greenclip/releases/download/v4.2/greenclip",
    dest="/usr/local/bin/greenclip",
    mode="0755",
)
