from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code != 200:
    raise ValueError("status code{}", format(response.status_code))

soup = BeautifulSoup(response.content, "html.parser")

# print(soup.span.text)


# div = soup.find_all("div")
# for d in div:
#     print(d.text)


# first_author = soup.find("small", "author")
# print(first_author.text)


# authors = set()
# authors_elements = soup.find_all("small", class_="author")
# for author in authors_elements:
#     authors.add(author.text)

# print(authors)


# authors = set()
# authors_elements = soup.select("small.author")
# for author in authors_elements:
#     authors.add(author.text)

# print(authors)



authors_quotes = {}
qoutes_elements = soup.select(".quote")
for qoute in qoutes_elements:
    author = qoute.select_one(".author").text
    qoute_text = qoute.select_one(".text").text
    link = qoute.select_one("a").attrs["href"]
    if author not in authors_quotes:
        authors_quotes[author] = {"qoutes": [], "link": link}

for author, data in authors_quotes.items():
    print(author)
    print(data["link"])



# items = soup.select('div[itemtype="http://schema.org/CreativeWork"]')
# for item in items:
#     print(item.text)



# title = soup.find("div")
# text1 = soup.find("p")
# link = soup.find("a")

# print(title.text)
# print(text1.text)
# print(link.attrs["href"])