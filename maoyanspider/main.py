import requests
import function
import re
"""
程序爬取猫眼排名前100的电影数据
"""

start_url = "https://maoyan.com/board/4?offset="
offset_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# offset_list = [0]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
           "Cookie": '__mta=209097005.1586438311617.1586445333969.1586445390546.48; uuid_n_v=v1; uuid=9A4DF5207A6411EA8EA6852B3999D85B5DE230EC34544A38A0E50FDD0137DA81; _csrf=ab4485c597690c4a2713adaa4915b81bae9943250597356e80c0a34765c82d20; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1715f178e24c8-02c8dba8a7ec27-5313f6f-144000-1715f178e24c8; _lxsdk=9A4DF5207A6411EA8EA6852B3999D85B5DE230EC34544A38A0E50FDD0137DA81; mojo-uuid=a74150d6b51252a0205a98949df4bf91; mojo-session-id={"id":"c1782f4359552b2266d1de74d6d51cd3","time":1586444647963}; __mta=209097005.1586438311617.1586444796534.1586445074051.47; lt=qvdVOI_XsiQs6egIYhcSTW0xd4YAAAAAXAoAAOkOMWtG88v3SJmzqgaSJjxz6nsaePHxDjBZ7fee2tgxYWtJ1KS3qiaVkWGqVeUoCw; lt.sig=dx6moSpjCf_RMVQTAV2OyBi-zIs; mojo-trace-id=22; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1586438311,1586445390; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1586445390; _lxsdk_s=1715f178e25-b73-a23-380%7C%7C140'
           }
item = {}
urls = function.get_url(start_url=start_url, offset_list=offset_list)
for url in urls:
    response = requests.get(url, headers=headers)
    response = response.content.decode()
    item["No."] = re.findall('<i class="board-index board-index-.*?>(.*?)</i>', response)
    item["name"] = re.findall('<a href=.*?="(.*?)" data-act="boarditem-click" .*</a>', response)
    item["star"] = re.findall('<p class="star">\s+(.*?)\s+</p>', response,re.S)
    item["time"] = re.findall('<p class="releasetime">(.*?)</p>', response)
    content = "排名：" + "," + str(item["No."]) + "\n" + \
              "电影名称：" + "," + str(item["name"]) + "\n" + \
              "主演：" + "," + str(item["star"]) + "\n" + \
              "上映时间：" + "," + str(item["time"]) + "\n"
    with open("data.txt", "a", encoding="utf8") as f:
        f.write(content)
        f.close()