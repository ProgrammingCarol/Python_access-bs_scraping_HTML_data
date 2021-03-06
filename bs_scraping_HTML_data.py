import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

#Retrieve data
tags = soup('span')
sum = 0
for tag in tags:
    print('TAG:', tag)
    print('URL:',tag.get('href',None))
    print('Contents:',tag.contents[0])
    print('Attrs:',tag.attrs)
    sum = int(tag.contents[0])+sum
print(sum)
