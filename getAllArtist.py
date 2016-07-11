import json
import getImage
import time
import simpletest


def writefile():
    with open('out/imageUrl.json', 'a') as fp:
        json.dump(ImageList, fp, indent="\t", sort_keys=True)

musics = json.loads(open('out/out.json').read())

Alist = []
for music in musics:
    temp_name = ""
    name = musics[music]["name"]
    split_name = name.split(" - ")
    len_split_name = len(split_name)
    if len_split_name > 2:
        for z in range(len_split_name - 1):
            if z == len_split_name - 2:
                temp_name = temp_name + split_name[z]
            else:
                temp_name = temp_name + split_name[z] + '-'

    else:
        temp_name = split_name[0]

    if not (temp_name in Alist):
        Alist.append(temp_name)
print("**********获取完名字************")

# 保存图片地址及名称的json
ImageList = {}
for i, n in enumerate(Alist):
    print(str(i) + ":" + n, end='\n')
    # ImageList[n] = getImage.getimageurl(n)
    if n not in ImageList:
        try:
            ImageList[n] = simpletest.getlink(artist=n)
        except Exception:
            writeFile()
            break

    writeFile()
    # time.sleep(1)

print("************获取完对应的图片地址**************")


