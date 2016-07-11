import json
import getImage
import time
import simpletest


def writefile():
    with open('out/SongimageUrl.json', 'a') as fp:
        json.dump(ImageList, fp, indent="\t", sort_keys=True)

musics = json.loads(open('out/out.json').read())
# print("**********获取完名字************")

ImageList = {}
for music in musics:
    temp_name = ""
    name = musics[music]["name"]
    try:
        print(music + " : " + name)
        ImageList[name] = simpletest.getlink(artist=name)
    except Exception:
        writefile()
        break

writefile()

# print(len(Alist))
# print(i)
# 保存图片地址及名称的json
#
# for i, n in enumerate(Alist):
#     print(str(i) + ":" + n, end='\n')
#     # ImageList[n] = getImage.getimageurl(n)
#     ImageList[n] = simpletest.getlink(artist=n)
#     time.sleep(1)

print("************获取完对应的图片地址**************")


