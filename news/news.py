#!/bin/python3

from bs4 import BeautifulSoup
import re
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://news.google.com/topics"

def get_news_links():
    r = requests.get(url = url , verify = False)
    
    # this is just substitution(will explain later)
    # r_filename = "topics.html"
    # f = open(r_filename,'r')
    # this is the file where content would be written
    w_filename = "content.txt"
    p = open(w_filename,'w')

    soup = BeautifulSoup(r.content,'html.parser') # Creating a soup object
    # list(soup.children)

    # test = []
    # test = list(soup.find_all('a',href = re.compile(r'[/]([a-z]|[A-Z])\w+'))) 

    # for i in test:
    #     if "stories" in str(i):
    #         p.write(str(i))
    #         p.write('\n')

    # p.close

    for i in soup.find_all('a',href=True):
        cool = i['href']
        if "stories" in i['href']:
            p.write('\n\n')
            p.write("https://news.google.com"+ cool[1:])
        
        elif "articles" in i['href']:
            p.write('\n\n')
            p.write("https://news.google.com"+ cool[1:])
        
        else:
            continue
    
    p.close


get_news_links()

