from selenium import webdriver
import time
import re
import csv
import pandas as pd

data = pd.read_csv('games_url.csv', index_col=0)
game_urls = data['url'].tolist()[3962:]
# game_urls = data['url'].tolist()
# test_urls = ["https://boardgamegeek.com/boardgame/221107/pandemic-legacy-season-2",game_urls[950],game_urls[1000]]

csv_file = open('game_details1.csv','w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(['title','age','complexity','min_player','max_player','min_time','max_time','category','subcategory'])

for url in game_urls:
	driver = webdriver.Chrome()
	driver.get(url)

	title = driver.find_element_by_xpath('//h1/a').text
	age = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[3]/div/span').text
	try:
		age = int(re.findall('\d+',age)[0])
	except:
		age = None
	try:
		complexity = float(driver.find_element_by_xpath('//ul[@class="gameplay"]/li[4]/div/span[2]/span[1]').text)
	except:
		complexity = None
	try:
		min_player = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[1]/div/span/span').text
		try:
			max_player = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[1]/div/span/span[2]').text[1]
		except:
			max_player = min_player
	except:
		continue
	try:
		min_time = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[2]/div/span/span/span').text
		try:
			max_time = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[2]/div//span[@ng-if="max>0 && min != max"]').text[1:]
		except:
			max_time = min_time
	except:
		continue
	i=1
	category=[]
	while i<6:
		try:
			item_i = driver.find_element_by_xpath(f'//li[@class="feature"]/div[2]/span[{i}]/a').text
			category.append(item_i)
		except:
			break
		i+=1

	j=1
	subcategory=[]
	while i<7:
		try:
			item_j = driver.find_element_by_xpath(f'//li[@class="feature"][2]//span[@class="text-block ng-scope"][{j}]/a').text
			subcategory.append(item_j)
		except:
			break
		j+=1

	game = {}
	game['title'] = title
	game['age'] = age
	game['complexity'] = complexity
	game['min_player'] = int(min_player)
	game['max_player'] = int(max_player)
	game['min_time'] = int(min_time)
	game['max_time'] = int(max_time)
	game['category'] = category
	game['subcategory'] = subcategory
	print(game)

	writer.writerow(game.values())

	driver.close()
