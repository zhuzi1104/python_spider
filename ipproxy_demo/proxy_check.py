import setting
from proxy_catch import qiyun_spider
from proxy_catch import bajiu_spider
from proxy_catch import xici_spider
import threading
import requests
import time
import pymongo


def check(proxies):
    # 配置请求信息
    headers = {"User-Agent": setting.get_ua()[14:-1]}
    # 链接数据库,准备备份TXT
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient["spider"]
    mycol = mydb["proxy_pool"]
    f = open("result.txt", "a")
    http = 0
    https = 0
    print(proxies)
    try:
        # 检测IP是否支持http协议
        url = "http://httpbin.org/ip"
        response = requests.get(url=url, headers=headers, proxies=proxies, timeout=setting.TIMEOUT)
        if response.status_code == 200:
            print("http可用")
            http = 1
        else:
            print("http状态码错误")
    except:
        print("http  fail")
    try:
        # 检测IP是否支持https协议
        urls = "https://httpbin.org/ip"
        response = requests.get(url=urls, headers=headers, proxies=proxies, timeout=setting.TIMEOUT)
        if response.status_code == 200:
            print("https可用")
            https = 1
        else:
            print("https状态码错误")
    except:
        print("https  fail")
    # 把塞选出来可用的ip存入数据库
    if http == 1 or https == 1:
        # 满足条件的数据，备份进txt文件
        f.write(str(proxies) + ",http={}".format(http) + ",https={}".format(https) + "\n")
        # 满足条件的数据，保存进mongodb数据库
        if mycol.find_one({'ip': '{}'.format(proxies)}) is None:
            data = {'ip': '{}'.format(proxies), "http": 'http={}'.format(http), 'https': 'https={}'.format(https)}
            mycol.insert_one(data)
    f.close()


def qiyun_data():
    proxies = qiyun_spider()
    for i in proxies:
        proxies = {
            'http': 'http://{}'.format(i),
            'https': 'https://{}'.format(i)
        }
        check(proxies)
        time.sleep(setting.SLEEP)


def bajiu_data():
    proxies = bajiu_spider()
    for i in proxies:
        proxies = {
            'http': 'http://{}'.format(i),
            'https': 'https://{}'.format(i)
        }
        check(proxies)
        time.sleep(setting.SLEEP)


def xici_data():
    proxies = xici_spider()
    for i in proxies:
        proxies = {
            'http': 'http://{}'.format(i),
            'https': 'https://{}'.format(i)
        }
        check(proxies)
        time.sleep(setting.SLEEP)


def main():
    while True:
        t1 = threading.Thread(target=qiyun_data)
        t2 = threading.Thread(target=bajiu_data)
        t3 = threading.Thread(target=xici_data)
        t1.start()
        t2.start()
        t3.start()
        time.sleep(700000)


if __name__ == '__main__':
    main()