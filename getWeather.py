"""
从腾讯天气获取气象信息

"http://weather.gtimg.cn/city/01010101.js" 返回数据格式：
sk_wd:对应wt_img.json中的数字，
以便确定图标地址，base url="http://mat1.gtimg.com/weather/2014gaiban/" + "TB_" + ico(wt_img.json中对应) + _baitian/_yejian + .png
背景的地址格式:"http://mat1.gtimg.com/weather/2014gaiban/"  + bg + _baitian/_yejian + .jpg

sk_tp:温度，单位 ℃

sk_wd:风向     sk_wp：风力     sk_hd：湿度 %

wInfo.wk['0']  一周预测

指数图片:http://mat1.gtimg.com/weather/2014gaiban/TB_shzs/zs(split_0/split_2中的key，取值对应接口中zs_xx).png


"""

import requests as rq
import json
import data_json.zhishu as zhishu


url = "http://weather.gtimg.cn/city/01010101.js"

r = rq.get(url).text

j = r.split("=")[1].lstrip().rstrip(";")

result = json.loads(j)

print("温度：", result["sk_tp"])
print("风向：", zhishu.windDir[int(result["sk_wd"])], end="")
print(result["sk_wp"] + "级")


# for i in result:
#     print(i, result[i])














# url = "http://weather.gtimg.cn/aqi/01010101.json"
#
# r = rq.get(url).text
#
# ws = []
# ws = r.split("[", 1)[1][:-2]
#
# ws = ws.replace("null", '\"\"')
# ws = ws.replace("}, {", "}*{")
#
# ws = ws.split("*")
#
# print(ws.__doc__)
#
# # w = json.loads(r.split("[", 1)[1][:-3])
# #
# for i in range(len(ws)):
#     w = json.loads(ws[i])
#     print(w)


