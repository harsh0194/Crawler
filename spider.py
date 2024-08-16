#!usr/bin/env python

import requests
import re
import urllib.parse as urlparse

target_url = "http://192.168.10.145/mutillidae/"
target_links = []
def extract_links_from(url):
    response = requests.get(target_url)
    return re.findall(r'(?:href=")(.*?)"', response.content.decode('utf-8'))

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)


