from urllib.parse import urlencode


def get_url(kw, max_page):
    base_url = "https://m.weibo.cn/api/container/getIndex?"
    search = "100103type=1&q=" + kw
    params = {
        "containerid": search,
        "page_type": "searchall"
    }
    for i in range(1, max_page):
        if i == 1:
            url = base_url + urlencode(params)
        else:
            url = base_url + urlencode(params) + "&page=" + str(i)
        yield url
