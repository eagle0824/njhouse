from copy import deepcopy

import scrapy

from njhouse.items import RentHouseItem


class RenthouseSpider(scrapy.Spider):
    name = 'renthouse'
    allowed_domains = ['recnt.cn']
    start_urls = ['http://house.njhouse.com.cn/rent/houselist']

    def parse(self, response):
        # filename = "data/stockhouses.html"
        # open(filename, 'wb').write(response.body)
        '获取总页数'
        lastIndex = int(response.xpath('//div[@class="pagination-container"]/a[14]/@data-index').extract_first())
        i = 1
        while i <= lastIndex:
            if (i == 1):
                url = "http://house.njhouse.com.cn/rent/houselist"
            else:
                url = "http://house.njhouse.com.cn/rent/houselist/p-" + str(i)
            #print(url)
            yield scrapy.Request(url, callback=self.parse_list, dont_filter=True)
            i = i + 1

    def parse_list(self, response):
        '获取列表项目'
        #count = 0
        for sel in response.xpath('//div[@class="list_main_lists"]/ul/li/a'):
            for i in sel.xpath('@href').extract():
                url = "http://house.njhouse.com.cn" + i
                #print(url)
                item = RentHouseItem()
                item["uri"] = url
                yield scrapy.Request(url, callback=self.parse_item, meta={'item': deepcopy(item)}, dont_filter=True)
                #break
            #count+=1
            #if (count > 1):
                #break

    def parse_item(self, response):
        '获取Stock House item'
        item = response.meta['item']
        item["unifiedCoding"] = str(response.xpath('//span[@class="house-code"]/text()').extract_first())
        item["name"] = response.xpath('//div[@class="house-name"]/text()').extract_first()
        item["price"] = response.xpath('//span[@class="price-val"]/text()').extract_first()
        # item["price"] = response.xpath('//span[@class="price-unit"]/text()').extract_first()
        item["rentway"] = response.xpath('//span[@class="parm-val"]')[0].xpath('text()').extract_first()
        item["paymethod"] = response.xpath('//span[@style="color: #333333"]/text()').extract_first()
        item["area"] = response.xpath('//span[@class="parm-val"]')[1].xpath('text()').extract_first().replace(u'\xa0',
                                                                                                              u'')
        item["decoration"] = response.xpath('//span[@class="parm-val"]')[2].xpath('text()').extract_first()
        item["floor"] = response.xpath('//span[@class="parm-val"]')[3].xpath('text()').extract_first().replace(u'\xa0',
                                                                                                               u'')
        item["residentialArea"] = response.xpath('//span[@class="parm-val"]')[4].xpath('text()').extract_first()
        item["address"] = response.xpath('//span[@class="parm-val"]')[5].xpath('text()').extract_first()
        item["listedTime"] = response.xpath('//span[@class="parm-val"]')[6].xpath('text()').extract_first()

        try:
            item["listedPersion"] = response.xpath('//table[@class="plain-table"]/tr[2]/td/a')[0].xpath(
                'text()').extract_first()
        except Exception as e:
            item["listedPersion"] = response.xpath('//table[@class="plain-table"]/tr[2]/td')[0].xpath(
                'text()').extract_first()

        item["listedPersionPhoneNumber"] = response.xpath('//table[@class="plain-table"]/tr[2]/td')[2].xpath(
            'text()').extract_first()

        try:
            item["listedSource"] = response.xpath('//table[@class="plain-table"]/tr[2]/td/a')[1].xpath(
                'text()').extract_first()
        except Exception as e:
            item["listedSource"] = response.xpath('//table[@class="plain-table"]/tr[2]/td')[1].xpath(
                'text()').extract_first()

        #家电信息
        housepacking = ""
        for sel in response.xpath('//div[@class="conf-name"]'):
            if(len(housepacking) > 0):
                housepacking = housepacking + "," + sel.xpath('text()').extract_first()
            else:
                housepacking = sel.xpath('text()').extract_first()

        item["housepacking"] = housepacking

        item["details"] = response.xpath('//div[@class="detail-cont"]/p')[0].xpath('text()').extract_first()
        yield item