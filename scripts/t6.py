import requests
import pprint
import json

GITHUB_API_TOKEN = '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'

header = {
    'Authorization': 'token {}'.format(GITHUB_API_TOKEN),
    'Accept': 'application/vnd.github.v3+json'
}
class Release:

    def __init__(self, version: str, prelease: bool) -> bool:
        self.version = version
        self.prelease = prelease
    def __str__(self) -> str:
        return f'{self.version} ({self.prelease})'
def isPrelease(user: str, repo: str, tag_name: str) -> bool:
    r = requests.get(
        f'https://api.github.com/repos/{user}/{repo}/releases/tags/{tag_name}',
        headers=header)
    print(r.json())
    return r.json()['prerelease']
def get_versions_in_tags(user: str, repo: str):
    tag_url = f'https://api.github.com/repos/{user}/{repo}/tags'
    print(tag_url)
    print
    r = requests.get(tag_url, headers=header)
    versions = []
    for tag in r.json():
        version = tag['name']
        print(version)
        prelease = isPrelease(user, repo, version)
        print(prelease)
        versions.append(Release(version, prelease))
    return versions


# https://api.github.com/repos/alacritty/alacritty/releases/tags/v0.11.0-rc3
print(isPrelease('alacritty', 'alacritty', 'v0.11.0-rc3'))