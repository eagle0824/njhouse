import os

from scrapy import cmdline

path = './data/rent.csv'
if os.path.exists(path):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
    os.remove(path)
    #os.unlink(path)
cmdline.execute("scrapy crawl renthouse -o ./data/rent.csv".split())