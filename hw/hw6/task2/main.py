from bs4 import BeautifulSoup
import requests

url = "https://www.billboard.com/charts/hot-100/"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

playlist = []

links = soup.find_all("a", href=True)

for link in links:

    href = link["href"]

    if "/artist/" in href:

        artist = link.get_text(strip=True)

        parent = link.find_parent()

        song_tag = parent.find("h3")

        if song_tag:
            song = song_tag.get_text(strip=True)

            playlist.append({
                "song": song,
                "artist": artist
            })

unique = []
seen = set()

for item in playlist:
    key = (item["song"], item["artist"])

    if key not in seen:
        seen.add(key)
        unique.append(item)

for item in unique:
    print(item["song"], "-", item["artist"])

