'''
读取QQ音乐，包括获取音乐地址，专辑图片及专辑介绍等.
'''

import requests
import json


def get_song_mid():
    # 获取一人一首成名曲列表
    url = "http://radio.cloud.music.qq.com/fcgi-bin/qm_guessyoulike_cp.fcg?start=-1&num=20&uin=0&labelid=307&rnd=1468268072184&g_tk=938407465&loginUin=0&hostUin=0&format=jsonp&inCharset=GB2312&outCharset=utf-8&notice=0&platform=yqq&jsonpCallback=FmJsonpCallBack&needNewCode=1"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Cookie": "ptui_loginuin=779402401; ptcz=a39ccf059bb1717999cabdd6469a10450f23f8cfda96455ffa8d7bfc021e1af5; pt2gguin=o0779402401; qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30; pgv_info=ssid=s7655547528; pgv_pvid=5413406128; o_cookie=779402401",
        "Host": "radio.cloud.music.qq.com"
    }

    r = requests.get(url=url, headers=header)

    # r_json = {}
    # print(r.text.split("(", 1)[1])
    #
    # print(r.text.split("(", 1)[1][:-2])
    r_json = json.loads(r.text.split("(", 1)[1][:-2])

    # print(len(r_json))

    songs = r_json["songs"]

    # parse song

    mid = ""
    # key = get_key()  #获取数据流地址时组合使用

    # print(songs[0]["songmid"])
    # print("歌曲名", songs[0]["songname"])
    # albummid: 专辑图片id，地址格式为:
    for song in songs:
        # print(song)
        songmid = song["songmid"]
        print("歌手", song["singer"][0]["name"])
        print("歌曲名", song["songname"])
        stream = max(song["stream"], 1) + 10
        sid = str(song["songid"] + 30000000)
        mp3url = "http://stream" + str(stream) + ".qqmusic.qq.com/" + sid + ".mp3"
        print(mp3url)
        albummid = song["albummid"]
        get_ablum_pic(id=albummid, mid=albummid, type=90)
        # print("songmid", song["songmid"])
        # get_song(songmid=songmid, key=key)  #可获取数据流地址
        #     mid = song["songmid"]
        #     # print("专辑名", song["albumname"])
        # return songs[0]["songmid"]


def get_key():
    getkeyurl = "http://base.music.qq.com/fcgi-bin/fcg_musicexpress.fcg?json=3&guid=5413406128&g_tk=938407465&loginUin=0&hostUin=0&format=jsonp&inCharset=GB2312&outCharset=GB2312&notice=0&platform=yqq&jsonpCallback=jsonCallba"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Connection": "keep-alive",
        "Cookie": "PATH=/; ptui_loginuin=779402401; ptcz=a39ccf059bb1717999cabdd6469a10450f23f8cfda96455ffa8d7bfc021e1af5; pt2gguin=o0779402401; qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30; pgv_info=ssid=s7655547528; pgv_pvid=5413406128; o_cookie=779402401",
        "Host": "base.music.qq.com",
        "Referer": "ttp://y.qq.com/"
    }

    r = requests.get(url=getkeyurl, headers=header)
    # print(r.text.split("(", 1)[1][:-2])
    r_json = json.loads(r.text.split("(", 1)[1][:-2])
    print(r_json["key"])
    return r_json["key"]


def get_song(songmid, key):
    music_url = "http://dl.stream.qqmusic.qq.com/C200" + songmid + ".m4a?vkey=" + key + "&guid=5413406128&fromtag=30"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Cookie": "ptui_loginuin=779402401; ptcz=a39ccf059bb1717999cabdd6469a10450f23f8cfda96455ffa8d7bfc021e1af5; pt2gguin=o0779402401; qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30; pgv_info=ssid=s7655547528; pgv_pvid=5413406128; o_cookie=779402401",
        "Host": "i.y.qq.com",
        "Referer": "http://y.qq.com/"
    }

    print("song url: ", music_url)

    # r = requests.get(url=music_url, headers=header)

    # print(r)

#获取专辑图片
def get_ablum_pic(id, mid, type):
    picNomal = "http://i.gtimg.cn/music/photo/album/{0}/{1}_albumpic_{2}_0.jpg"
    pic300 = "http://i.gtimg.cn/music/photo/album_300/{0}/300_albumpic_{1}_0.jpg"
    picMid = "http://i.gtimg.cn/music/photo/mid_album_{picsize}/{s1}/{s2}/{mid}.jpg"
    picRtn = "http://i.gtimg.cn/mediastyle/y/img/cover_mine_130.jpg"

    try:
        picsize = type
    except NameError:
        picsize = 300
    parms = {
        "picsize": picsize,
        "s1": mid[-2],
        "s2": mid[-1],
        "mid": mid
    }

    picMid = picMid.format_map(parms)
    # picMid = picMid.format("0", "1", "2", "3")
    print("专辑图片", picMid)
    return picMid


# 获取专辑信息，包括介绍及歌曲
def get_ablum_info(albummid):
    url = "http://i.y.qq.com/v8/fcg-bin/fcg_v8_album_info_cp.fcg?albummid=" + albummid


# 获取歌词xml
def get_lyric(songid):
    xml_url = "http://music.qq.com/miniportal/static/lyric/" + str(songid % 100) + "/" + str(songid) + ".xml"


#读取播放次数
def get_count():
    url = "http://i.y.qq.com/s.plcloud/fcgi-bin/fcg_getsonglistenstatistic.fcg?utf8=1&songlist={id list by | }&_=random.random()"

get_song_mid()

# get_ablum_pic()
