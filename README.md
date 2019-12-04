# Scraper of news articles from Russia Today/ RT/ Россия Сегодня website (https://russian.rt.com/)

(Описание на русском ниже)

This project collects news articles' titles and texts from the website of Russian newspaper RT. You can choose any topic and time period, from which you want to get the articles.

Before running the project, you have to install the necessary software typing this command in your Terminal/command line:

**python3.6 -m pip install -r requirements.txt --upgrade**

Then you should go to https://russian.rt.com/, choose the keywords and dates you are interested in, copy the resulting link and replace the link in settings.py file with this url.

![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/copy_link.png)

then you can just run the file main_rt.py using this command in your Terminal:

**python3.6 main_rt.py**

Your browser window will be opened automatically. You don't have to do anything, just wait and don't close the window (you can do whatever you want in other programs while this one will be executed). This is what you will see:

![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/scraping_browser.png)

![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/output1.png)

![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/output2.png)


After the browser will be closed, it will be opened again and the program will continue executing in the Terminal and you will see headlines of scraped articles:

![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/output3.png)


The resulting csv-file will be saved in the folder of the project (you can see example in the folder "output" now). No matter how many articles will be in your results, the script automatically scrolls the webpage down until it reaches the end and scrapes all the articles.

This is how resulting file looks like:

![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/resulting_file.png)








*Translation to Russian/ Перевод на русский:*



Эта программа скачивает заголовки и тексты новостных статей с сайта российского новостного  агентства RT (Russia Today). Вы можете выбрать любую тему и период времени, за который вы хотите получить статьи.

Перед запуском проекта вам необходимо установить необходимое программное обеспечение, набрав эту команду в вашем терминале (командной строке):

**python3.6 -m pip install -r requirements.txt --upgrade**


Затем вам нужно перейти на https://russian.rt.com/, выбрать ключевые слова и даты, которые вас интересуют, скопировать получившуюся ссылку и заменить ссылку в файле settings.py этим URL.

![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/copy_link.png)


Теперь вы можете просто запустить файл main_rt.py с помощью этой команды в вашем терминале\командной строке:


**python3.6 main_rt.py**


Окно вашего браузера будет открыто автоматически. Вам не нужно ничего делать, просто ждите и не закрывайте окно (вы можете делать все, что захотите, в других программах, пока эта будет выполняться). Независимо от того, сколько статей будет в ваших результатах, программа будет автоматически прокручивать веб-страницу вниз, пока не дойдет до конца, и загрузит все статьи. Вот что вы должны увидеть:


![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/scraping_browser.png)

![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/output1.png)

![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/output2.png)


После того, как браузер закроется, программа продолжит работу в Терминале\командной строке, и вы увидите заголовки загруженных статей:


![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/output3.png)

Результаты загрузки будут сохранены в CSV-файле в папке проекта (вы можете увидеть пример в папке «output»). 


![alt text](https://github.com/YaKsenia/scraper_russia_today_website/blob/master/output/resulting_file.png)



