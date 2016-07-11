import urllib.request as request
from urllib.parse import urlparse
from os.path import splitext, basename, exists
import json, urllib

f = open("out/imageUrl.json").read()

images = json.loads(f)

keys = images.keys()

# link = "https://s.discogs.com/images/default-release-cd.png"
# # result = request.urlopen(link)
#
#
# filename, file_ext = splitext(basename(urlparse(link).path))
#
# savename = filename + file_ext
#
# # print(savename)
#
# with open("artistImg/" + savename, 'wb') as file:
#     with request.urlopen(link) as l:
#         file.write(l.read())

for name in keys:
    link = images.get(name)
    filename, file_ext = splitext(basename(urlparse(link).path))
    savename = name + file_ext
    if link != "" and not exists("artistImg/" + savename):
        with open("artistImg/" + savename, 'wb') as file:
            with request.urlopen(link) as l:
                file.write(l.read())
                print("saved", savename)
