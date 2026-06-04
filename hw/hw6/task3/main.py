import requests
import json

url = "https://api.jikan.moe/v4/top/anime"

response = requests.get(url)

data = response.json()

anime_list = []

for anime in data["data"]:
    title = anime["title"]
    score = anime["score"]

    anime_list.append({
        "title": title,
        "score": score
    })

with open("popular_anime.json", "w", encoding="utf-8") as f:
    json.dump(anime_list, f, ensure_ascii=False, indent=4)

print("Done.")