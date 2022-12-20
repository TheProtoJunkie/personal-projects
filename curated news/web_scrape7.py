import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib


website = "https://www.theguardian.com/us"
html = urllib.request.urlopen(website).read()
soup = BeautifulSoup(html, 'html.parser')
list_of_stories = []
list_of_links = []
article = soup.find_all('div', class_="fc-item__container")

# prints just news stories from 'website'
for story in article:
    link = story.find("a")
    url = link.get('href')
    headline = story.find("span", class_="js-headline-text")
    list_of_stories.append(headline.text)
    list_of_links.append(url)

#print(headline.text, '\n', url)
# print()
#print(list_of_stories, '\n')
