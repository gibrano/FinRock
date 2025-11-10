from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from newspaper import Article
from datetime import datetime, timedelta
import os
import json

class NewsCollector:
    def __init__(self, start_date, end_date):
        self.NEWS_API_KEY = ""
        self.start_date = start_date
        self.end_date = end_date

        self.newsapi_url = (
            f"https://newsapi.org/v2/top-headlines?"
            f"country=us&"                       # palabra clave
            f"from={self.start_date}&"               # desde hace 7 días
            f"to={self.end_date}&"                     # hasta hoy
            f"sortBy=publishedAt&"             # ordenar por fecha
            f"language=en&"                    # idioma (puedes cambiar a 'es')
            f"apiKey={self.NEWS_API_KEY}"
        )

    def get_page(self, url):
        html = ""
        options = Options()
        options.add_argument("--headless=new")  # safer than "--headless"
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")  # critical for Linux
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-features=VizDisplayCompositor")
        options.add_argument("--window-size=1920,1080")
        options.page_load_strategy = 'eager'  # don't wait for full JS load

        driver = webdriver.Chrome(options=options)
        chrome_options = webdriver.ChromeOptions()
        #driver.set_page_load_timeout(30)
        driver.implicitly_wait(10)
        driver.set_window_size(1920, 1080)
        try:
            driver.get(url)            
            html = driver.page_source
        except Exception as e:
            print("Timeout:", e)
        finally:
            driver.quit()
        return html

    def get_all_news(self):
        response = requests.get(self.newsapi_url)
        return response.json()    

    
    def collect(self):
        self.data = self.get_all_news()

        N = len(self.data["articles"])
        for i in range(N):            
            article = self.data["articles"][i]
            url = article["url"]
            print(i, "portal --->",url)
            web_page = self.get_page(url)
            news_article = Article(url="")
            news_article.set_html(web_page)
            news_article.parse()

            self.data['articles'][i]['full_content'] = (str(self.data['articles'][i]['title'] or "") 
                                                        + "\n" + str(self.data['articles'][i]['content'] or "") 
                                                        + "\n" 
                                                        + str(news_article.text or ""))
