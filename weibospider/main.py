import create_url
import parse
import re


'''
需求：
1.自定义搜索关键词，搜索所有翻页内容；
2.输出字段：博主id、微博正文、评论数、转发数、点赞数、发布时间；
2.输出为表格；
'''

# 拿到目标url
urls = create_url.get_url("特朗普", 5)
for i in urls:
    response = parse.parse(i)
    # 提取数据
    for i in response:
        print(i)
        item = {}
        item["博主ID"] = re.findall("screen_name....(.*?)....profile", i)
        item["微博正文"] = re.findall("longTextContent....(.*?)....url_objects", i)
        item["评论数"] = re.findall("comments_count...(.*?)...attitudes_count", i)
        item["转发数"] = re.findall("reposts_count...(.*?)...comments_count", i)
        item["点赞数"] = re.findall("attitudes_count...(.*?)...pending_approval_count", i)
        item["发布时间"] = re.findall("created_at....(.*?)....[a-zA-Z]", i)
        # 保存数据
        name = ["博主ID", "微博正文", "评论数", "转发数", "点赞数", "发布时间"]
        content = "博主ID：" + "," + str(item["博主ID"]) + "\n" +\
                  "评论数：" + "," + str(item["评论数"]) + "\n" +\
                  "点赞数：" + "," + str(item["点赞数"]) + "\n" +\
                  "转发数：" + "," + str(item["转发数"]) + "\n" +\
                  "发布时间：" + "," + str(item["发布时间"]) + "\n"
        with open("data.txt", "a", encoding="utf8") as f:
            f.write(content)