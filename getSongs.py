import requests
from html.parser import HTMLParser
import json

import time


class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def __init__(self, artist):
        super().__init__()
        self.img = False
        self.span = False
        self.artist = artist
        self.weather = {}

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def getweather(self):
        return self.weather


def getcity(city=""):
    # url = "http://tianqi.2345.com/t/searchCity.php?q=0635&pType=local"
    # url = "http://mobilecdn.kugou.com/new/app/i/yueku.php?singer=陈奕迅&cmd=102"    //可获取歌手的图片

    # 获取一人一首成名曲列表
    url = "http://radio.cloud.music.qq.com/fcgi-bin/qm_guessyoulike_cp.fcg?start=-1&num=20&uin=0&labelid=307&loginUin=0&hostUin=0&format=jsonp&inCharset=GB2312&outCharset=utf-8&notice=0&platform=yqq&jsonpCallback=FmJsonpCallBack&needNewCode=1"

    #解析出每一个songmid供生成音乐地址
    songmid = ""

    t = str(round(time.time(), 3)).replace('.', '')  # 获取时间戳并格式化成字符串
    # 获取mid,需解析数据格式如下:b'getkgemid1468266117491({"code":0,"data":[{"id":101804789,"kmid":"001lRYxp3wU6Ra","mid":"001abixR3f8L59"}]
    getmidUrl = "http://proxy.music.qq.com/musichall/fcgi-bin/fcg_getkmid.fcg?jsonpCallback=getkgemid" + t + "&midlist=001abixR3f8L59&p=" + t + "&g_tk=938407465&loginUin=0&hostUin=0&format=jsonp&inCharset=GB2312&outCharset=utf-8&notice=0&platform=yqq&jsonpCallback=getkgemid" + t + "&needNewCode=0"

    # 获取key
    #
    #jsonCallback({"code":0,"sip":["http://cc.stream.qqmusic.qq.com/",
    # "http://ws.stream.qqmusic.qq.com/",
    # "http://163.177.63.142/streamoc.music.tc.qq.com/","
    # http://dl.stream.qqmusic.qq.com/"] ,
    # "thirdip":["http://112.90.148.214/abcd1234/",
    #  "http://180.153.100.233/abcd1234/"],
    # "key": "D2454534E825B5343067413F4D56CBB952AC72CD59B36D56C613A530896ABA5EEBF4644C7A7212B3C4218F72C6CF9821215F25A36863EB50"});
    #
    # getKeyUrl = "http://base.music.qq.com/fcgi-bin/fcg_musicexpress.fcg?json=3&g_tk=938407465&loginUin=0&hostUin=0&format=jsonp&inCharset=GB2312&outCharset=GB2312&notice=0&platform=yqq&jsonpCallback=jsonCallback&needNewCode="
    getKeyUrl = "http://base.music.qq.com/fcgi-bin/fcg_musicexpress.fcg?json=3&guid=5413406128&g_tk=938407465&loginUin=0&hostUin=0&format=jsonp&inCharset=GB2312&outCharset=GB2312&notice=0&platform=yqq&jsonpCallback=jsonCallba"

    key = ""
    #

    #音乐地址格式

    musicUrl = "http://dl.stream.qqmusic.qq.com/C200"+ songmid +".m4a?vkey="+ key +"&guid=5413406128&fromtag=30"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Connection":"keep-alive",
        "Cookie":"ptui_loginuin=779402401; ptcz=a39ccf059bb1717999cabdd6469a10450f23f8cfda96455ffa8d7bfc021e1af5; pt2gguin=o0779402401; qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30; pgv_info=ssid=s7655547528; pgv_pvid=5413406128; o_cookie=779402401",
        "Host":"dl.stream.qqmusic.qq.com",
        "Referer":"http://y.qq.com/"
    }

    r = requests.get(url=getmidUrl, headers=header)

    # j = json.loads(r.text)

    print(r.content)
    # for i in j:
    #     print("attr:", i)
    #     print(j[i])



    # print(r.text)
    # r.content.decode('ISO-8859-1', "replace").encode('utf-8', 'replace')
    # print(r.content.decode('ISO-8859-1', "replace").encode('utf-8', 'replace'))
    # parser = MyHTMLParser(artist=artist)
    #
    # parser.feed(r.text)
    # return parser.getlink()


getcity()
