import pymongo
import requests
import re


def get_proxy(url):
    print(url)
    # 通过URL解析出需求的协议类型
    agreement = re.findall("(.*?)://", url)[0]
    print(agreement)
    # 配置请求头
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
    # 链接数据库
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient["spider"]
    mycol = mydb["proxy_pool"]
    # 数据库取出代理ip
    proxy = mycol.find({"{}".format(agreement): "{}=1".format(agreement)})
    for i in proxy:
        proxy = eval(i["ip"])
        print(proxy)
        try:
            response = requests.get(url=url, headers=headers, proxies=proxy, timeout=3)
            if response.status_code == 200:
                return proxy
                break
        except:
            try:
                check_url = "http://httpbin.org/ip"
                result1 = requests.get(url=check_url, headers=headers, proxies=proxy, timeout=3)
            except:
                pass
            try:
                check_urls = "https://httpbin.org/ip"
                result2 = requests.get(url=check_urls, headers=headers, proxies=proxy, timeout=3)
            except:
                pass
            if result1.status_code == 200 or result2.status_code == 200:
                pass
            else:
                mycol.delete_one({"ip": "{}".format(proxy)})


if __name__ == '__main__':
    x = get_proxy(url="https://www.runoob.com/")
    print("找到匹配IP：{}".format(x))