import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.Linkextractors import Linkextractor
from scrapy.exceptions import CloseSpider
from tourinfo.items import TourinfoItem

class TourinfoSpider(CrawlSpider):
	name = 'tourinfo'
	item_count = 0
	allowed_domain = ['https://www.procyclingstats.com/es/race/tour-de-france/2018/startlist/']

 	rules = {
 		Rule(LinkEXtractor(allow=(),restrict_xpaths = ('//a[@class="rider blue"]')),
 			callback ='parse_item',follow = False)

 	}

 	def parse_item(self,response):
 		ml_item = TourinfoItem()
 		#info de los ciclistas
 		ml_item['nombre'] = response.xpath('normalize_space(/html/body/div[1]/div[3]/div[4]/div[2]/span/text()[2])').extract_first()
 		ml_item['fecha_nacimiento'] = response.xpath('normalize_space()').extract_first()
 		ml_item['nacionalidad'] = response.xpath('normalize_space()').extract_first()
 		ml_item['peso'] = response.xpath('normalize_space()').extract_first()
 		ml_item['altura'] = response.xpath('normalize_space()').extract_first()
 		ml_item['lugar_nacimiento'] = response.xpath('normalize_space()').extract_first()
 		ml_item['UCIRanking'] = response.xpath('normalize_space()').extract_first()
 		self.item_count += 1
		if self.item_count > 22:
			raise CloseSpider('item_exceeded')
		yield ml_item