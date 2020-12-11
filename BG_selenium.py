from selenium import webdriver
import time
import re


driver = webdriver.Chrome()

driver.get("https://boardgamegeek.com/boardgame/172287/champions-midgard")

# Click review button to go to the review section
# review_button = driver.find_element_by_xpath('//span[@class="padLeft6 cursorPointer"]')
# review_button.click()

# Page index used to keep track of where we are.
index = 1
# We want to start the first two pages.
# If everything works, we will change it to while True
while index <=2:
	try:
		print("Scraping Page number " + str(index))
		index = index + 1
		# Find all the reviews. The find_elements function will return a list of selenium select elements.
		# Check the documentation here: http://selenium-python.readthedocs.io/locating-elements.html
		reviews = driver.find_elements_by_xpath('//div[@class="row border_grayThree onlyTopBorder noSideMargin"]')
		# Iterate through the list and find the details of each review.
		for review in reviews:
			# Initialize an empty dictionary for each review
			review_dict = {}
			# Use try and except to skip the review elements that are empty. 
			# Use relative xpath to locate the title.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use 'element.get_attribute()'
			try:
				title = review.find_element_by_xpath('.//div[@class="NHaasDS75Bd fontSize_12 wrapText"]').text
			except:
				continue

			print('Title = {}'.format(title))

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
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# Locate the next button element on the page and then call `button.click()` to click it.
		button = driver.find_element_by_xpath('//li[@class="nextClick displayInlineBlock padLeft5 "]')
		button.click()
		time.sleep(2)

	except Exception as e:
		print(e)
		driver.close()
		break