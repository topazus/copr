from urllib.parse import urljoin
import posixpath

ls = [
    "scala3",
    "alacritty",
    "zoxide",
    "nushell",
    "flameshot",
    "bottom",
    "wezterm",
    "exa",
    "dua-cli",
    "opam",
    "bat",
    "xplr",
]
for i in ls:
    url_path = posixpath.join(f"{i}", f"{i}.spec")
    url = urljoin(
        "https://raw.githubusercontent.com/topazus/fedora-copr/main/", url_path
    )
    print(url)
print()
for i in ls:
    url = urljoin(
        "https://raw.githubusercontent.com/topazus/fedora-copr/main/", f"{i}/{i}.spec"
    )
    print(url)
print()
for i in ls:
    url = (
        "https://raw.githubusercontent.com/topazus/fedora-copr/main/" + f"{i}/{i}.spec"
    )

    print(url)
