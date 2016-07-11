import requests
import json



def getimageurl(q):
    # q = "Modern Talking"
    # print(q.encode())

  # Url = "https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=8bdfc79787aa2b2b1ac464140255872c&searchtype=image&cx=004275229428061124871:ur0hs7fg8d4&q=" + q + "&googlehost=www.google.com"
    Url = "https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=8bdfc79787aa2b2b1ac464140255872c&searchtype=image&cx=004275229428061124871:ur0hs7fg8d4&q=" + q

    try:
        print("get :" + q)
        r = requests.get(Url)
        print(r)
        allresult = json.JSONDecoder().decode(r.text)
        results = allresult["results"]
        imgurl = ""
        for test in results:
            if 'Discography' in test['title']:
                # print("名称：" + test["title"])
                # print("地址：" + test["url"])
                imgurl = test["url"]

        if imgurl == "" and len(results) > 0:
            imgurl = results[0]["url"]
        return imgurl
    except(RuntimeError, ValueError):
        print("错误：" + q, end='\n')
        return "发生错误..."

