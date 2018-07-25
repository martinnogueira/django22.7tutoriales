# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TourinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #info ciclista
    nombre = scrapy.Field()
    fecha_nacimiento = scrapy.Field()
    nacionalidad = scrapy.Field()
    peso = scrapy.Field()
    altura = scrapy.Field()
    lugar_nacimiento = scrapy.Field()
    UCIRanking = scrapy.Field()


