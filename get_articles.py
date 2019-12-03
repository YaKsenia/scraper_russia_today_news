import newspaper
from newspaper import Article
import pandas as pd

def get_articles(df):

	headers = []
	texts = []
	for url in df['links']:

			article = Article(url)
			article.download()
			article.parse()
			headers.append(article.title)
			texts.append(article.text)
			driver.implicitly_wait(5)

	final = pd.DataFrame({'link' : links, 'title' : headers, 'text' : texts})

	return final




#(article.html)

#print(articl.text)