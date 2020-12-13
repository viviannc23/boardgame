from selenium import webdriver
import time
import re
import csv
import pandas as pd

url = "https://boardgamegeek.com/boardgame/62214/aspern-essling-1809"

driver = webdriver.Chrome()
driver.get(url)

title = driver.find_element_by_xpath('//h1/a').text
age = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[3]/div/span').text
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


game = {}
game['title'] = title
try:
	game['age'] = int(re.findall('\d+',age)[0])
except:
	game['age'] = []
# game['complexity'] = float(complexity)
# game['min_player'] = int(min_player)
# game['max_player'] = int(max_player)
# game['min_time'] = int(min_time)
# game['max_time'] = int(max_time)
# game['category'] = category
# game['subcategory'] = subcategory
print(game)


driver.close()