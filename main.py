import requests
from html.parser import HTMLParser
import json

Url = 'http://italo-disco.net/3.%20Player%20Menu32.html'

r = requests.get(Url)


# print(r.text)


class parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.finda = False
        self.find_li = False
        self.findb = False
        self.num = 0
        self.data = {}
        self.tempson = {}

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'li':
            self.find_li = True

        if tag == 'a' and self.find_li:
            self.finda = True
            for (attr, value) in attrs:
                # self.num += 1
                self.tempson['link'] = value

        if tag == 'b':
            self.findb = True

    def handle_endtag(self, tag):

        if tag == 'b':
            if self.finda and self.find_li:
                self.num += 1
                self.data[str(self.num)] = self.tempson
                print('Link IS:' + str(self.num) + ' ' + self.tempson['link'])

            self.findb = False
        if tag == 'li':
            self.find_li = False

        if tag == 'a':
            self.finda = False

    def handle_data(self, data):
        if self.find_li and self.finda and self.findb:
            self.tempson['name'] = data
            # print('演唱者:' + data)

    def return_data(self):
        return self.data


par = parser()

par.feed(r.text)

with open('out/out.json', 'w') as fp:
    json.dump(par.return_data(), fp, indent="\t")


# f = open('out/out.json', 'w')
# json.dump(par.return_data(), fp=f)

# f.write(str(par.return_data()))
# f.close()


# print(par.return_data())
