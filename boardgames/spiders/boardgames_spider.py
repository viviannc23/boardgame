from scrapy import Spider, Request
from boardgames.items import BoardgamesItem
import re

class BoardgamesSpider(Spider):
	name = 'boardgames_spider'
	allowed_urls = ['https://boardgamegeek.com']
	start_urls = ['https://boardgamegeek.com/browse/boardgame/page/1']

	def parse(self, response):
		num_pages = int(response.xpath('//a[@title="last page"]/text()').extract_first()[1:-1])
		# num_pages = 5
		page_urls = [f'https://boardgamegeek.com/browse/boardgame/page/{i+1}' for i in range(num_pages)]

		# print(page_urls)
		# print("="*55)

		for url in page_urls:
			# print("="*55)
			# print("scraping page:"+ url)

			# yield Request(url=url, callback = self.parse_game_page)
			yield Request(url=url, callback = self.parse_results_page)

	# def parse_results_page(self, response):
	# 	# game_urls = response.xpath('//td[@class="collection_thumbnail"]/a/@href').extract()
	# 	# game_urls = ['https://boardgamegeek.com' + url for url in game_urls]

	# 	games = response.xpath('//div[@id="collection"]//tr[@id="row_"]')
	# 	for game in games:
	# 		url = game.xpath('.//td[@class="collection_thumbnail"]/a/@href').extract_first()
	# 		url = 'https://boardgamegeek.com' + url


	# 	print('='*55)
	# 	print(len(game_urls))	
	# 	for url in game_urls:
	# 		yield Request(url=url, callback = self.parse_game_page)

	# def parse_game_page(self, response):
	def parse_results_page(self, response):	

		games = response.xpath('//div[@id="collection"]//tr[@id="row_"]')

		for game in games:
			try:
				year = int(re.findall('\d+',game.xpath('.//div/span/text()').extract_first())[0])
			except:
				continue
			title = game.xpath('.//div/a/text()').extract_first()
			try:
				rank = int(game.xpath('.//td[@class="collection_rank"]/text()').extract()[1].strip())
			except:
				rank = game.xpath('.//td[@class="collection_rank"]//text()').extract_first().strip()
			try:
				geek_rating = float(game.xpath('.//td[@class="collection_bggrating"][1]/text()').extract_first().strip())
			except:
				geek_rating = game.xpath('.//td[@class="collection_bggrating"][1]/text()').extract_first().strip()
			try:
				avg_rating = float(game.xpath('.//td[@class="collection_bggrating"][2]/text()').extract_first().strip())
			except:
				avg_rating = game.xpath('.//td[@class="collection_bggrating"][2]/text()').extract_first().strip()
			try:
				num_rating = float(game.xpath('.//td[@class="collection_bggrating"][3]/text()').extract_first().strip())
			except:
				num_rating = game.xpath('.//td[@class="collection_bggrating"][2]/text()').extract_first().strip()
			try:
				description = game.xpath('.//p/text()').extract_first().strip()
			except:
				description = game.xpath('.//p/text()').extract_first()
			url = game.xpath('.//td[@class="collection_thumbnail"]/a/@href').extract_first()
			url = 'https://boardgamegeek.com' + url

			item = BoardgamesItem()
			item['title'] = title
			item['year'] = year
			item['rank'] = rank
			item['geek_rating'] = geek_rating
			item['avg_rating'] = avg_rating
			item['num_rating'] = num_rating
			item['description'] = description
			item['url'] = url

			yield item




