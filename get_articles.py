import newspaper
from newspaper import Article
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


df = pd.read_csv('/home/ksenia/Desktop/thesis_scripts/RT_links_final.csv', sep=',', low_memory=False, na_values = ['no info', '.'])
links = list(df['links'])
headers = []
texts = []
for url in links:
		article = Article(url)
		article.download()
		article.parse()
		headers.append(article.title)
		texts.append(article.text)

final = pd.DataFrame({ 'title' : headers, 'text' : texts})

#final.to_csv('RT_articles.csv')


#(article.html)

#print(articl.text)