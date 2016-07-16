import requests
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def error(self, message):
        pass

    def __init__(self, artist):
        super().__init__()
        self.img = False
        self.span = False
        self.artist = artist
        self.link = ""

    def handle_starttag(self, tag, attrs):
        if tag == "span" and self.link == "":
            # for name, value  in attrs:
            #     if name == "class":
            #         print("catch span class is: ",value)
            self.span = True
        if tag == "img" and self.span:
            src = ""
            alt = ""
            for name, value in attrs:
                if name == "src":
                    src = value
                if name == "alt":
                    alt = value
            self.link = src

    def handle_endtag(self, tag):
        if tag == "span":
            # print("Encountered a end tag:", tag)
            self.span = False
        if tag == "img":
            self.img = False

    def getlink(self):
        return self.link
# class MyHrmlParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         if tag == "span":
#             self.span = 1
#             print(attrs)
#         if tag == "img":
#             self.img = 1
#
#     def handle_endtag(self, tag):
#         if tag == "span":
#             self.span = 0
#         if tag == "img":
#             self.img = 0
#
#     def handle_data(self, data):
#
#         if self.span == 0 and self.img == 0:
#             print(data)


def getlink(artist):
    url = "https://www.discogs.com/search/?q=" + artist + "&type=all"

    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }

    r = requests.get(url=url, headers=header)
    parser = MyHTMLParser(artist=artist)

    parser.feed(r.text)
    return parser.getlink()


print(getlink("Andrea - I'm A Lover"))