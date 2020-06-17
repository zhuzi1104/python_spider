def get_url(start_url, offset_list):
    for i in offset_list:
        url = start_url + str(i)
        yield url

