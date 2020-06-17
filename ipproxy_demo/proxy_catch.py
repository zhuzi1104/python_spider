import requests
from lxml import etree
import setting


class BaseSpider:
    def __init__(self, url):
        self.url = url
        self.proxies = setting.PROXIES
        self.headers = {"User-Agent": setting.get_ua()[14:-1]}

    def get_element(self):
        response = requests.get(url=self.url, headers=self.headers, timeout=setting.TIMEOUT)
        response = response.content.decode()
        html = etree.HTML(response)
        return html


def qiyun_spider(total_page=500):
    for page in range(1, total_page):
        # 实例化爬虫类，调用get_element方法，拿到返回结果
        qiyun = BaseSpider("https://www.7yip.cn/free/?action=china&page={}".format(page))
        element = qiyun.get_element()
        # Xpath提取数据
        ip = element.xpath('//*[@id="content"]/section/div[2]/table/tbody/tr/td[1]/text()')
        port = element.xpath('//*[@id="content"]/section/div[2]/table/tbody/tr/td[2]/text()')
        for i in range(10):
            proxy = ip[i] + ":" + port[i]
            print("抛出一个齐云的代理")
            yield proxy
        print("齐云第{}页爬取完毕".format(page))


def bajiu_spider(total_page=50):
    for page in range(1, total_page):
        # 实例化爬虫类，调用get_element方法，拿到返回结果
        bajiu = BaseSpider("http://www.89ip.cn/index_{}.html".format(page))
        element = bajiu.get_element()
        # Xpath提取数据
        for i in range(1, 16):
            ip = element.xpath('normalize-space(//table[@class="layui-table"]/tbody/tr[{}]/td[1])'.format(i))
            port = element.xpath('normalize-space(/html/body//table[@class="layui-table"]/tbody/tr[{}]/td[2]/text())'.format(i))
            proxy = ip + ":" + port
            print("抛出一个89的代理")
            yield proxy
        print("89第{}页爬取完毕".format(page))


def xici_spider(total_page=3500):
    for page in range(1, total_page):
        # 实例化爬虫类，调用get_element方法，拿到返回结果
        xici = BaseSpider("https://www.xicidaili.com/nn/{}".format(page))
        element = xici.get_element()
        # Xpath提取数据
        ip = element.xpath('//table[@id="ip_list"]//tr[@class="odd"]/td[2]/text()')
        port = element.xpath('//table[@id="ip_list"]//tr[@class="odd"]/td[3]/text()')
        for i in range(50):
            proxy = ip[i] + ":" + port[i]
            print("抛出一个西次的代理")
            yield proxy
        print("西次第{}页爬取完毕".format(page))


if __name__ == '__main__':
    x = qiyun_spider(total_page=2)
    for i in x:
        print(i)

