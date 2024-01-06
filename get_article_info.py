# %%
import requests
import json

def get_article_info_crossref(title):
    base_url = "https://api.crossref.org/works"
    params = {"query.title": title}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['message']['items']:
            article = data['message']['items'][0]
            return {
                "Title": article.get("title")[0] if article.get("title") else "Not Available",
                "Authors": [author.get("given") + " " + author.get("family") for author in article.get("author", [])],
                "Year": article.get("published-print", {}).get("date-parts", [[None]])[0][0],
                "Volume": article.get("volume"),
                "Pages": article.get("page")
            }
        else:
            return "No articles found for this title."
    else:
        return "Failed to retrieve data."

