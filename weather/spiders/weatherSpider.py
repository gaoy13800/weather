# -*- coding: utf-8 -*-
import scrapy
from weather.tools import request_header
from weather.items import WeatherItemLoader, WeatherItem
from datetime import datetime
from scrapy.http import Request

class WeatherspiderSpider(scrapy.Spider):
    name = 'weatherSpider'
    allowed_domains = ['weather.sina.com.cn']
    start_urls = ['http://weather.sina.com.cn/']

    headers = {
        'Host':"weather.sina.com.cn",
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        'Referer':"http://weather.sina.com.cn/china/hebeisheng/"
    }


    def parse(self, response):
        wnbc_list = response.xpath('//div[@class="wnbc_piC"]//a')

        for i in wnbc_list:
            provice = i.xpath('text()').extract_first()
            province_href = i.xpath('@href').extract_first()

            #提取每一个省份url交给scrapy下载并回调给parse_province
            if province_href:
                yield Request(
                    province_href, headers=self.headers, cookies=request_header.get_cookie(),
                    meta={"province_name": provice}, callback=self.parse_province)


    def parse_province(self, response):

        city_list = response.xpath('//div[@class="wd_cmain"]')

        for city_item in city_list:
            area_url = city_item.xpath('.//@href').extract()

            city_name = city_item.xpath('.//div[@class="wd_cmh"]/text()').extract_first().replace(' ', '').replace('\n', '')

            meta = {
                'province':response.meta['province_name'],
                'city':city_name
            }

            for url in area_url:
                yield Request(
                    url=url, headers=self.headers, cookies=request_header.get_cookie(), meta=meta,
                    callback=self.parse_area)


    def parse_area(self, response):

        item_loader = WeatherItemLoader(item=WeatherItem(), response=response)

        item_loader.add_value('province', response.meta['province'])
        item_loader.add_value('city', response.meta['city'])
        item_loader.add_css('area', '#slider_ct_name::text')
        item_loader.add_css('weather_condition', '.slider_detail::text')
        item_loader.add_css("wind_direction", '.slider_detail::text')
        item_loader.add_css("humidity", '.slider_detail::text')

        air_quality = response.xpath('//p[@class="slider_warn_val slider_warn_val3"]/text()')

        if air_quality is None:
            item_loader.add_value("air_quality", air_quality)
        else:
            item_loader.add_value("air_quality", '无')


        item_loader.add_xpath('date', '//p[@class="slider_ct_date"]/text()')
        item_loader.add_xpath('temperature', '//div[@class="slider_degree"]/text()')
        item_loader.add_value('crawl_time', datetime.now())

        weather_item = item_loader.load_item()

        yield weather_item



