import random

# UA池，总共19个user_agent
ua_pool = [
    '"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) '
    'Version/5.1 Safari/534.50"',
    '"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 '
    'Safari/534.50"',
    '"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"',
    '"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"',
    '"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"',
    '"User-Agent": "M"ozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"',
    '"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"',
    '"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"',
    '"User-Agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"',
    '"User-Agent":"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"',
    '"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) '
    'Chrome/17.0.963.56 Safari/535.11"',
    '"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"',
    '"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"',
    '"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"',
    '"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)"',
    '"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr '
    '1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"',
    '"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"',
    '"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)"',
    '"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"'
]


def get_ua():
    ua = ua_pool[random.randint(0, 18)]
    return ua


# 设置请求超时，单位秒
TIMEOUT = 5
# 设置请求间隔，单位秒
SLEEP = 5
# 设置proxy_catch模块中的代理IP.最好是同时支持http、https协议。协议类型不匹配，会拿不到数据
PROXIES = ''


if __name__ == '__main__':
    print(get_ua())
