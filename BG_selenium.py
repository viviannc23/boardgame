from selenium import webdriver
import time
import re
import csv
import pandas as pd

data = pd.read_csv('games_url.csv', index_col=0)
game_urls = data['url'].tolist()

csv_file = open('game_details.csv','w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(['title','age','complexity','time','min_player','max_player','category'])

for url in game_urls:
	driver = webdriver.Chrome()
	driver.get(url)

	title = driver.find_element_by_xpath('//h1/a').text
	age = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[3]/div/span').text
	complexity = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[4]/div/span[2]/span[1]').text
	min_player = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[1]/div/span/span').text
	try:
		max_player = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[1]/div/span/span[2]').text[1]
	except:
		max_player = min_player
	time = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[2]/div/span/span/span').text

	i=1
	category=[]
	while i<8:
		try:
			item = driver.find_element_by_xpath(f'//li[@class="feature"]/div[2]/span[{i}]/a').text
			category.append(item)
		except:
			break
		i+=1

	game = {}
	game['title'] = title
	game['age'] = int(re.findall('\d+',age)[0])
	game['complexity'] = float(complexity)
	game['min_player'] = int(min_player)
	game['max_player'] = int(max_player)
	game['time'] = int(time)
	game['category'] = category
	print(game)

	writer.writerow(game.values())

	driver.close()


