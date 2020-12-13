from selenium import webdriver
import time
import re
import csv

driver = webdriver.Chrome()

# driver.get("https://boardgamegeek.com/boardgame/161936/pandemic-legacy-season-1")
driver.get("https://boardgamegeek.com/boardgame/174430/gloomhaven")
# driver.get("https://boardgamegeek.com/boardgame/254640/just-one")

#game = {}

#title = driver.find_element_by_xpath('//h1/a').text
#complexity = driver.find_element_by_xpath('//ul[@class="gameplay"]/li[4]/div/span[2]/span[1]').text
test = 

print(test)

# game_dict['title'] = title

			# OPTIONAL: How can we deal with the "read more" button?
			
			# Use relative xpath to locate text, username, date_published, rating.
			# Your code here

			# Uncomment the following lines once you verified the xpath of different fields
			
			# review_dict['title'] = title
			# review_dict['text'] = text
			# review_dict['username'] = username
			# review_dict['date_published'] = date_published
			# review_dict['rating'] = rating

		# We need to scroll to the bottom of the page because the button is not in the current view yet.
	# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# 	# Locate the next button element on the page and then call `button.click()` to click it.
	# 	button = driver.find_element_by_xpath('//li[@class="nextClick displayInlineBlock padLeft5 "]')
	# 	button.click()
	# 	time.sleep(2)

	# except Exception as e:
	# 	print(e)
	# 	driver.close()
	# 	break

driver.close()