import time
import requests
from lxml import html
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("西安二手房数据.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)
header = ["名称", "地址", "细节", "单价(元/m^2)"]
csvwriter.writerow(header)


def get_one_page(url):
    # 获取网页
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44 "
    }
    resp = requests.get(url=url, headers=header)

    # 解析语法树
    hl = html.etree.HTML(resp.text)
    con_1 = hl.xpath("/html/body/div[4]/div[1]/ul/li")
    for t in con_1:
        name = t.xpath("./div[1]/div[2]/div/a[1]/text()")
        local = t.xpath("./div[1]/div[2]/div/a[2]/text()")
        detail = t.xpath("./div[1]/div[3]/div/text()")
        price = t.xpath("./div[1]/div[6]/div[2]/span/text()")
        # 存入数据
        csvwriter.writerows(zip(name, local, detail, price))
    time.sleep(1)


if __name__ == '__main__':
    with ThreadPoolExecutor(5) as t:
        for i in range(1, 101):
            t.submit(get_one_page, f"https://xa.lianjia.com/ershoufang/pg{i}/")
