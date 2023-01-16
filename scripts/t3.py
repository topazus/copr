import requests
import packaging.version
from bs4 import BeautifulSoup

repo_names=['lampepfl/dotty','apache/groovy','rakudo/rakudo','bazelbuild/bazel','nim-lang/Nim']
package_version=''
for x in repo_names:
    resp=requests.get(f'https://api.github.com/repos/{x}/releases/latest')
    status=resp.status_code
    if status!=404:
        content=resp.json()
        print(content['tag_name'])
    else:
        content=requests.get(f'https://api.github.com/repos/{x}/tags').json()
        print(content[0]['name'])

class JetabinsProduct:
    def __init__(self,name,codename,version,download_url) -> None:
        self.name=name
        self.codename=codename
        self.version=version
        self.download_url=download_url
    def __str__(self) -> str:
        return f'{ name: {self.name}, codename: {self.codename}, version: {self.version}, download url: {self.download_url} }'

r=requests.get('https://www.jetbrains.com/updates/updates.xml')
soup=BeautifulSoup(r.content,'lxml-xml')
names_map=[]
jetbrains_products=[]
for x in soup.find_all('product'):
    name=x.get('name')
    codename=x.find('code').contents
    version=x.find('channel').find('build')['version']
    url=f'https://download.jetbrains.com/idea/{codename}-{version}.tar.gz'
    jp=JetabinsProduct(name,codename,version,url)
    jetbrains_products.append(jp)
print(jetbrains_products)

