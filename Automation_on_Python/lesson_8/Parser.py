import requests
import lxml.html
from lxml import etree
# pip3 install lxml

html = requests.get('https://www.python.org/').content

tree = lxml.html.document_fromstring(html)
title = tree.xpath('/html/head/title/text()')

print(title)

tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())
ul = tree.findall('//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li')

for li in ul:
    a = li.find('a')
    print(a.text)
