from bs4 import BeautifulSoup, SoupStrainer
import urllib.request as urllib2
import re
import requests
from headers import HEADERS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''
url = 'https://russian.rt.com/search?q=%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F+%D1%81%D0%B8%D1%80%D0%B8%D1%8F+%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0&type=&df=2016-05-01&dt=2016-08-01'

req = requests.get(url, HEADERS)
plain_text = req.text
soup = BeautifulSoup(plain_text, "lxml")

articles = soup.find('div', {'class': 'listing__content listing__content_js'})

ankor_list = articles.findChildren('a')3

for ankor in ankor_list:
    url = ankor.get('href')
    print(url)

'''



driver = webdriver.Firefox()
driver.get('https://russian.rt.com/search?q=%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F+%D1%81%D0%B8%D1%80%D0%B8%D1%8F+%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0&type=&df=2016-05-01&dt=2016-08-01')
while True:
	url = 'https://russian.rt.com/search?q=%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F+%D1%81%D0%B8%D1%80%D0%B8%D1%8F+%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0&type=&df=2016-05-01&dt=2016-08-01'

	req = requests.get(url, HEADERS)
	plain_text = req.text
	soup = BeautifulSoup(plain_text, "lxml")

	articles = soup.find('div', {'class': 'listing__content listing__content_js'})

	ankor_list = articles.findChildren('a')

	for ankor in ankor_list:
	    url = ankor.get('href')
	    print(url)
   # do whatever you want
	try:
#		list_next = driver.find_elements(by=By.LINK_TEXT, value='Загрузить ещё')
#		for link in list_next:
#			link.click()
#class="subscribe__close js-subscribe-close"
		driver.find_element_by_link_text('Подтвердить').click()
		driver.find_element_by_link_text('Загрузить ещё').click()
		#elm = driver.find_element_by_class_name('listing__button listing__button_js')
		#elm.click()
		articles = soup.find('div', {'class': 'listing__content listing__content_js'})
		ankor_list = articles.findChildren('a')

		for ankor in ankor_list:
		    url = ankor.get('href')
		    print(url)

		#driver.find_element_by_xpath('//////////a[text()="Загрузить ещё"]').click()
	except NoSuchElementException:
		break