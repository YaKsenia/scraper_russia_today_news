from bs4 import BeautifulSoup, SoupStrainer
import urllib.request as urllib2
import re
import requests
import pandas as pd
from headers import HEADERS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Firefox()
driver.get('https://www.aljazeera.com/Search/?q=russia%20syria%20war')
driver.maximize_window()
#WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "I Accept")))
#WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "enstAccept")))


driver.find_element_by_id('ensCloseBanner').click()
#driver.find_element_by_link_text('I Accept').click()
#driver.find_element_by_class_name('ensButtons').click()

#element = driver.find_element_by_class_name('ensButtons')
#driver.execute_script("arguments[0].click();", element)

while True:
	try:
		#print('yeeees')
		number = 1
		links = []
		for i in range (0, 120):
				#driver.find_element_by_class_name("page-link").click()
				driver.find_element_by_link_text(str(number)).click()
				print ('clicked page',  number)
				driver.implicitly_wait(10)
				#articles = html.findall('div', {'class': "row topics-sec-item"})
				if number > 90:
					html = driver.page_source
					html = BeautifulSoup(html, "lxml")
					#articles = html.find('h2', {'class': 'row topics-sec-item'})
					articles = html.find_all('div', {'class': 'col-sm-7 topics-sec-item-cont'})
					for article in articles:
						ankor_list = article.findChildren('a')
						for ankor in ankor_list:
						    url = ankor.get('href')
						    url = 'https://www.aljazeera.com' + url
						    #if url != 'https://www.aljazeera.com/indepth/opinion' and url != 'https://www.aljazeera.com/topics/regions/middleeast.html' and url != 'https://www.aljazeera.com/topics/country/syria.html' and url != 'https://www.aljazeera.com/topics/regions/us-canada.html' and url != 'https://www.aljazeera.com/topics/regions/europe.html'
						    if 'news' in url or 'opinion' in url:
							    links.append(url)
							    print(url)
				#print(links)
				number = number + 1

		print(links)
		links = pd.DataFrame({'links' : links })
		links = links.drop_duplicates(subset='links', keep='last', inplace=False)
		links.to_csv('al_jazeera_links_final.csv')

	except NoSuchElementException:
		break

	finally:
		#driver.quit()
		print('bye')
