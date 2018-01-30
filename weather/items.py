# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class WeatherItemLoader(ItemLoader):
    #自定义itemLoader
    default_output_processor = TakeFirst()


def get_weather(value):
    ret = value.replace(' ', '').replace('\n', '')
    return ret.split('|')[0]

def get_wind_direction(value):
    ret = value.replace(' ', '').replace('\n', '')
    return ret.split('|')[1]

def get_humidity(value):
    ret = value.replace(' ', '').replace('\n', '')
    return ret.split('|')[2]


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    province = scrapy.Field()
    city = scrapy.Field()
    area = scrapy.Field()
    weather_condition = scrapy.Field(
        input_processor=MapCompose(get_weather),
    )
    wind_direction = scrapy.Field(
        input_processor=MapCompose(get_wind_direction),
    )
    temperature = scrapy.Field()
    air_quality = scrapy.Field()
    date = scrapy.Field()
    humidity = scrapy.Field(
        input_processor=MapCompose(get_humidity),
    )
    crawl_time = scrapy.Field()




    def get_insert_sql(self):
        insert_sql = """
            insert into weather_info(province, city, area, weather_condition, wind_direction, temperature, air_quality, `date`, humidity, crawl_time)
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        params = (
            self["province"], self["city"],self["area"],
            self["weather_condition"][0],self["wind_direction"][1],self["temperature"],self["air_quality"],self["date"],self["humidity"][2],
            self["crawl_time"].strftime('%Y-%m-%d %H:%M:%S')
        )

        return insert_sql, params