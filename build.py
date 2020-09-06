from time import sleep
import urllib.request
# create /build/ folder
# build .html files
#   for page in templates/pages build page
# build css files
# build js files (no js files right now...)
# copy /images/favicon.ico to /favicon.ico
# create a sitemap.xml file for the website.


def build():
    sleep(3)
    with urllib.request.urlopen('http://127.0.0.1:5000/') as response:
        html = response.read()
        print(html)
    print('Files have been built!')


build()
