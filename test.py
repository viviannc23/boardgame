from selenium import webdriver
import time
import re
import csv
import pandas as pd

# url = "https://boardgamegeek.com/boardgame/221107/pandemic-legacy-season-2"
# url = "https://boardgamegeek.com/boardgame/285774/marvel-champions-card-game"
# url = "https://boardgamegeek.com/boardgame/233078/twilight-imperium-fourth-edition" #7 subcategories
# url = "https://boardgamegeek.com/boardgame/115746/war-ring-second-edition" #6 subcategories
url = "https://boardgamegeek.com/boardgame/115746/war-ring-second-edition" #7 subcategories

driver = webdriver.Chrome()
driver.get(url)

more_button = driver.find_element_by_xpath('//li[@class="feature"][2]/div[2]//a[@class="text-block ng-binding"]')
more_button.click()

# test = driver.find_element_by_xpath('//li[@class="outline-item ng-scope"][7]/div[2]//div[@ng-repeat="link in creditsctrl.geekitem.data.item.links[info.keyname]"][6]/a').text()
# test = driver.find_element_by_xpath('.//li[@class="outline-item ng-scope"][7]/div[2]//div[@ng-repeat="link in creditsctrl.geekitem.data.item.links[info.keyname]"]/a').text()
# test = driver.find_element_by_xpath('.//div[@class="panel-body"]//li[@class="outline-item ng-scope"][7]/div[2]//a').text()
# test= driver.find_element_by_xpath('.//li[@class="outline-item ng-scope"][7]//div[@class="ng-scope"]/a').text()
# test = driver.find_element_by_xpath('.//h1/a').text 
test = driver.find_element_by_xpath('.//li[@class="outline-item ng-scope"][5]/div[2]//a').text

print(test)

# print(more_button)

# title = driver.find_element_by_xpath('//h1/a').text
# age = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[3]/div/span').text
# complexity = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[4]/div/span[2]/span[1]').text
# min_player = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[1]/div/span/span').text
# try:
# 	max_player = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[1]/div/span/span[2]').text[1]
# except:
# 	max_player = min_player
# min_time = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[2]/div/span/span/span').text
# try:
# 	max_time = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[2]/div//span[@ng-if="max>0 && min != max"]').text[1:]
# except:
# 	max_time = min_time

# i=1
# category=[]
# while i<8:
# 	try:
# 		item_i = driver.find_element_by_xpath(f'//li[@class="feature"]/div[2]/span[{i}]/a').text
# 		category.append(item_i)
# 	except:
# 		break
# 	i+=1

# j=1
# subcategory=[]
# while j<30:
# 	try:
# 		item_j = driver.find_element_by_xpath(f'//li[@class="feature"]//span[@class="text-block ng-scope"][{j}]/a').text
# 		subcategory.append(item_j)
# 	except:
# 		break
# 	j+=1


# game = {}
# game['title'] = title
# try:
# 	game['age'] = int(re.findall('\d+',age)[0])
# except:
# 	game['age'] = []
# game['complexity'] = float(complexity)
# game['min_player'] = int(min_player)
# game['max_player'] = int(max_player)
# game['min_time'] = int(min_time)
# game['max_time'] = int(max_time)
# game['category'] = category
# game['subcategory'] = subcategory
# print(game)

# time.sleep(2)
driver.close()