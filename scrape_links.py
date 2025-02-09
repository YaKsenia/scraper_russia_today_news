from bs4 import BeautifulSoup, SoupStrainer
import urllib.request as urllib2
import re
import requests
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def get_links(url):

	try:


		driver = webdriver.Firefox()
		driver.get(url)
		driver.maximize_window()
		#driver.find_element_by_link_text('Подтвердить').click()
		driver.find_element("link text", 'Подтвердить').click()
		print('Closed cookies window')
		#driver.find_element_by_class_name('subscribe-layout')
		#driver.find_element(By.CLASS_NAME, "subscribe-layout")
		#driver.find_element_by_class_name('subscribe__close').click()
		#driver.find_element(By.CLASS_NAME, 'subscribe__close').click()
		
		#print('Closed subscription window')


		for i in range(0,5):
			print('Waiting for 5 seconds')
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Загрузить ещё")))
			#driver.find_element_by_link_text('Загрузить ещё').click()
			driver.find_element("link text", 'Загрузить ещё').click()

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

		links = pd.DataFrame({'links' : links })
		links = links.drop_duplicates(subset='links', keep='last', inplace=False)

		return links

	except NoSuchElementException:
		pass


	finally:
		driver.quit()