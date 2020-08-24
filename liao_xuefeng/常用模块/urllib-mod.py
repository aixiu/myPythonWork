from urllib import request, parse

if __name__ == '__main__':
    # 定义基本搜索地址
    baseUrl = "http://www.baidu.com/s?"

    # 用户输入关键字搜索
    wd = input("Input your keWord: ")

    # 使用data构造字典，此参数必须是dict形式
    data = {
        "wd" : wd
    }

    # 将输入的关键字数据进行转码，这样服务器才能识别
    data = parse.urlencode(data)

    # 最终发送请求的URL，将基本地址和关键字级联起来
    url = baseUrl + data

    print("最终发送请求的URL：{0}".format(url))

    # 打开URL
    # rsp = request.urlopen(url)

    # 读取网页内容
    # html = rsp.read()

    # 将tytes类型内容转换为str类型内容
    # html = html.decode("utf - 8")

    # 打印最终网页内容
    # print(html)