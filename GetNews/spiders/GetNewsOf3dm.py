import scrapy
from ..items import GetnewsItem


class NewsSpider(scrapy.Spider):
    name = "3dm"
    start_urls = ["http://www.3dmgame.com/"]

    def parse(self, response):
        print(response)
        print("Start Crawling")
        GNI = GetnewsItem()
        title_list = response.xpath("//ul[@class='c-2']/li/a/text()").extract()
        url_list = response.xpath("//ul[@class='c-2']/li/a/@href").extract()
        time_list = response.xpath("//ul[@class='c-2']/li/span[1]/text()").extract()[:-1]  # [-1]为“下一页”，切片去除
        for i, j, k in zip(time_list, title_list, url_list):
            GNI["time"] = i
            GNI["title"] = j
            GNI["url"] = k
            yield GNI
        #     print(i,":",j,"url:",k)
