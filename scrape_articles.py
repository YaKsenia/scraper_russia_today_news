import newspaper
from newspaper import Article
import pandas as pd
from selenium import webdriver


def get_articles(df):

	driver = webdriver.Firefox()
	headers = []
	texts = []
	for url in df['links']:

			article = Article(url)
			article.download()
			article.parse()
			headers.append(article.title)
			texts.append(article.text)
			driver.implicitly_wait(5)

	df['title'] = headers
	df['text'] = texts
	driver.quit()

	return df




#(article.html)

#print(articl.text)