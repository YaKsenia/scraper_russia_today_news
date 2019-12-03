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

url = 'https://russian.rt.com/search?q=%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F+%D1%81%D0%B8%D1%80%D0%B8%D1%8F+%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0&type=&df=2016-05-01&dt=2016-08-01'

try:


	driver = webdriver.Firefox()
	driver.get('https://russian.rt.com/search?q=%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F+%D1%81%D0%B8%D1%80%D0%B8%D1%8F+%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0&type=&df=2016-05-01&dt=2016-08-01')
	driver.maximize_window()
	driver.find_element_by_link_text('Подтвердить').click()
	print('Closed cookies window')
	driver.find_element_by_class_name('subscribe-layout')
	driver.find_element_by_class_name('subscribe__close').click()
	print('Closed subscription window')


	for i in range(0,5):
		print('Waiting for 5 seconds')
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Загрузить ещё")))
		driver.find_element_by_link_text('Загрузить ещё').click()
		print('Clicked on "Load more"')


	html = driver.page_source
	html = BeautifulSoup(html, "lxml")

	articles = html.find('div', {'class': 'listing__content listing__content_js'})

	ankor_list = articles.findChildren('a')

	
	links = []
	for ankor in ankor_list:
	    url = ankor.get('href')
	    url = 'https://russian.rt.com' + url
	    if url not in links:
		    links.append(url)
		    print(url)
	#print(links)

	links = pd.DataFrame({'links' : links })
	links = links.drop_duplicates(subset='links', keep='last', inplace=False)
	#links.to_csv('RT_links.csv')

except NoSuchElementException:
	pass

finally:
	driver.quit()