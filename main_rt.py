from scrape_links import get_links
from scrape_articles import get_articles

url = 'https://russian.rt.com/search?q=%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F+%D1%81%D0%B8%D1%80%D0%B8%D1%8F+%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0&type=&df=2016-05-01&dt=2016-08-01'

links_df = get_links(url)

articles = get_articles(links_df)

articles.to_csv('Russia_Today_articles.csv')
