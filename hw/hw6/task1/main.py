from bs4 import BeautifulSoup
import requests

url = "https://www.gutenberg.org/ebooks/78706"

response = requests.get(url)

if response.status_code != 200:
    raise ValueError("status code{}", format(response.status_code))

soup = BeautifulSoup(response.content, "html.parser")

author = soup.find("a", itemprop="creator")
title = soup.find("td", itemprop="headline")
language = soup.find("tr", itemprop="inLanguage")
category = soup.find("td", property="dcterms:type")
print("Title:", title.text)
print("Author:", author.text)
print(language.text)
print("Category:", category.text)