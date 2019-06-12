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
driver.get('https://www.rbc.ru/search/?query=%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F+%D1%81%D0%B8%D1%80%D0%B8%D1%8F+%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0&project=rbcnews&dateFrom=01.05.2016&dateTo=31.08.2016')
driver.maximize_window()
#WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Загрузить ещё")))
while True:
	try:
		print('yeeees')

		'''
		driver.find_element_by_link_text('Подтвердить').click()
		print('Closed cookies window')
		driver.find_element_by_class_name('subscribe-layout')
		#driver.find_element_by_link_text('Загрузить ещё').click()
		driver.find_element_by_class_name('subscribe__close').click()
		print('Closed subscription window')

		#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Close Pop-Up"))).click()
		#print("MORE button clicked")
#		list_next = driver.find_elements(by=By.LINK_TEXT, value='Загрузить ещё')
#		for link in list_next:
#			link.click()
#class="subscribe__close js-subscribe-close"
		#driver.find_element_by_link_text('Подтвердить').click()
		#driver.find_element_by_class_name('subscribe__close js-subscribe-close')
		#driver.find_element_by_link_text('Загрузить ещё').click()
		#elm = driver.find_element_by_class_name('listing__button listing__button_js')
		#elm.click()

		links = []
		for i in range(0,14):
			WebDriverWait(driver,20).until(EC.presence_of_element_located((By.LINK_TEXT, "Загрузить ещё")))
			#WebDriverWait(driver,20).until(EC.invisibility_of_element_located((By.LINK_TEXT, "Загрузить ещё")))
			print('waiting done')
			driver.find_element_by_link_text('Загрузить ещё').click()

			html = driver.page_source
			html = BeautifulSoup(html, "lxml")
			print(type(html))

			articles = html.find('div', {'class': 'listing__content listing__content_js'})

			ankor_list = articles.findChildren('a')

			for ankor in ankor_list:
			    url = ankor.get('href')
			    print(url)

				#elm.click()

		html = driver.page_source
		html = BeautifulSoup(html, "lxml")
		print(type(html))

		articles = html.find('div', {'class': 'listing__content listing__content_js'})

		ankor_list = articles.findChildren('a')

		for ankor in ankor_list:
		    url = ankor.get('href')
		    #print(url)
		


		driver.find_element_by_link_text('Загрузить ещё').click()
		print('Clicked on "Load more')

		WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "Загрузить ещё")))
				#elm.click()


		html = driver.page_source
		html = BeautifulSoup(html, "lxml")
		print(type(html))

		articles = html.find('div', {'class': 'listing__content listing__content_js'})

		ankor_list = articles.findChildren('a')

		for ankor in ankor_list:
		    url = ankor.get('href')
		    url = 'https://russian.rt.com' + url
		    links.append(url)
		    #print(url)
		print(links)

		links = pd.DataFrame({'links' : links })
		links = links.drop_duplicates(subset='links', keep='last', inplace=False)
		links.to_csv('RT_links_moscow.csv')


		#articles2 = soup.find('div', {'class': 'card__heading card__heading_all-new'})
		#print(articles2)	



		plain_text = req.text
		soup = BeautifulSoup(plain_text, "lxml")

		articles = soup.find('div', {'class': 'listing__content listing__content_js'})

		ankor_list = articles.findChildren('a')

		for ankor in ankor_list:
		    url = ankor.get('href')
		    print(url)


		#articles2 = soup.find('div', {'class': 'card__heading card__heading_all-new'})
		#print(articles2)
		'''

		




		#driver.find_element_by_xpath('//////////a[text()="Загрузить ещё"]').click()
	except NoSuchElementException:
		break

	finally:
		driver.quit()


