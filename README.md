# njhouse
scrapy抓取njhouse部分数据

环境(windows 7)
1 Anaconda
参考 https://mirror.tuna.tsinghua.edu.cn/help/anaconda/ 安装方式
可以下min版本 https://docs.conda.io/en/latest/miniconda.html
注意python版本, 我这里是3.6

2 scrapy
通过Anaconda promt安装
命令行执行
conda install scrapy
或者
python -m pip install --upgrade pip
pip -install scrapy

如果出现Successfully install scrapy字样，恭喜你，说明你顺利安装成功了

相关调试指令
Anaconda promt 中执行
创建项目
scrapy startproject tutorial

创建爬虫
scrapy genspider stockhouse njhouse.cn

执行爬虫
scrapy crawl stockhouse
执行爬虫并保存.csv文件


在Shell中尝试Selector选择器
scrapy shell http://house.njhouse.com.cn/stock/houselist/


其它
python开发工具
pycharm
