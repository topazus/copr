import requests
import os
import random
import lxml.etree
import lxml.html
import re
import time

user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
]

header = {"User-Agent": random.choice(user_agent)}
url = 'https://wallhaven.cc/latest'


def make_request(url):
    return requests.get(url=url, headers=header, timeout=3)


def requests_text(url):
    return requests.get(url=url, headers=header, timeout=3).text


for i in range(1, 5):
    if not os.path.exists(f'page{i}'):
        os.mkdir(f'page{i}')
    url = 'https://wallhaven.cc/latest?page={}'.format(i)
    html_text = requests_text(url)
    tree = lxml.html.fromstring(html_text)
    image_urls = tree.xpath('//a[@class="preview"]//@href')
    for url in image_urls:
        if (resp := make_request(url)).status_code != 200:  #判断，如果响应失败跳过这次数据抓取
            continue
        else:
            html_text = resp.text
            tree = lxml.html.fromstring(html_text)
            real_image_url = tree.xpath('//img[@id="wallpaper"]//@src')[0]
            image_width = tree.xpath(
                '//img[@id="wallpaper"]//@data-wallpaper-width')[0]
            image_height = tree.xpath(
                '//img[@id="wallpaper"]//@data-wallpaper-height')[0]

            name_match = re.match(r'.*/(.+)\.(.*)', real_image_url)
            image_name = '{name}-{width}x{height}.{image_format}'.format(
                name=name_match.group(1),
                width=image_width,
                height=image_height,
                image_format=name_match.group(2))
            file_path = f'page{i}/{image_name}'
            with open(file_path, 'wb') as f:
                if (resp := make_request(real_image_url)
                    ).status_code != 200:  #判断，如果响应失败跳过这次数据抓取
                    print(f'{real_image_url} error')
                    continue
                else:
                    print(
                        f'download from {real_image_url} save as {file_path}')
                    f.write(resp.content)
                    time.sleep(random.randint(1, 3))
