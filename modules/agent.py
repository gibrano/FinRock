import requests
from newspaper import Article
from datetime import datetime, timedelta
import os
import json

from openai import OpenAI

import numpy as np


class FinRock:
    def __init__(self, news_content):
        os.environ['OPENAI_API_KEY'] = ""
        self.PROMPT = '''
                        You are a financial analyst AI specialized in understanding global news 
                        and its potential impact on both **market sectors** and **specific stocks** 
                        within those sectors.
                        
                        TASK:
                        Analyze the following news and determine whether it could affect the stock price 
                        of any of the target sectors or specific stocks listed below.
                        
                        For each **affected sector**, identify which **stocks within it** are most likely to 
                        be impacted in the near future (from 1 to 7 days in the future).  
                        Then, for each affected sector, classify the overall expected price movement as 
                        "Strong Up", "Mild Up", "Mild Down", "Strong Down", or "No Change", and briefly explain why.
                        
                        If a sector and its stocks are not meaningfully affected, mark the sector as "unaffected."
                        
                        NEWS:
                        "{news_text}"
                        
                        TARGET SECTORS AND STOCKS:
                        {sector_stock_mapping}
                        
                        OUTPUT FORMAT (strict JSON):
                        {{
                          "news_headline": "<headline or short summary>",
                          "affected_sectors": [
                            {{
                              "sector": {{
                                "<sector_name>": ["<stock_1>", "<stock_2>", ...]
                              }},
                              "stock_price_effect": "<Strong Up|Mild Up|Strong Down|Mild Down|No Change>",
                              "reasoning": "<short explanation>"
                            }}
                          ],
                          "unaffected_sectors": ["<list of sectors not affected>"]
                        }}
                        '''
        self.data = news_content
        self.client = OpenAI()
        
    def save(self):
        pass

    def get_sectors(self):
        with open("data/sectors.json", "r") as f:
            sectors = json.load(f)
        return sectors

    def analize_news(self, news, sectors2stocks):
        
        prompt = self.PROMPT.format(
            news_text=news,
            sector_stock_mapping=sectors2stocks
        )

    
        input=[
                {
                    "role": "system",
                    "content": "You are a financial analyst AI specialized in understanding global news "
                               "and its potential impact on both **market sectors** and **specific stocks**" 
                               "within those sectors. Always return results in strict JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
        ]
    
        
    
        response = self.client.responses.create(
            model="gpt-5",
            input=input,
            reasoning={
                "effort": "high"
            }
        )
        
        out = response.output[1].content[0].text
        out = json.loads(out.replace("\\", "\\\\"))
        return out
        
    def get_insights(self):
        results = []
        stocks2sectors = self.get_sectors()

        sectors2stocks = {}
        for k, v in stocks2sectors.items():
            sectors2stocks[v] = sectors2stocks.get(v, []) + [k]

        affected = {}

        for sector in np.unique(list(stocks2sectors.values())):
            affected[sector] = {'Strong Up': 0, 'Strong Down': 0, 'Mild Up': 0, 'Mild Down': 0, 'No Change': 0}
        
        N = len(self.data["articles"])
        for i in range(N):
            out = self.analize_news(self.data["articles"][i]['full_content'], sectors2stocks) #", ".join(np.unique(list(sectors.values())))
            
            out['url'] = self.data["articles"][i]['url']
            results.append(out)
            print(out)
            print("="*80)

            for obj in out["affected_sectors"]:
                sector = list(obj['sector'].keys())[0]
                affected[sector][obj['stock_price_effect']] += 1
        
        return results, affected  