from selenium import webdriver
import time
import re
import csv

driver = webdriver.Chrome()

game = driver.get("https://boardgamegeek.com/boardgame/172287/champions-midgard")


		# reviews = driver.find_elements_by_xpath('//div[@class="row border_grayThree onlyTopBorder noSideMargin"]')
		# # Iterate through the list and find the details of each review.
		# for review in reviews:
			# Initialize an empty dictionary for each review
game_dict = {}
			# Use try and except to skip the review elements that are empty. 
			# Use relative xpath to locate the title.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use 'element.get_attribute()'
			# try:
			# 	title = review.find_element_by_xpath('.//div[@class="NHaasDS75Bd fontSize_12 wrapText"]').text
			# except:
			# 	continue

title = game.find_element_by_xpath('//a[@ui-sref="geekitem.overview"]').text.strip()
print(title)
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