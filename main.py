from requests import get
from urllib.parse import urljoin


params = {
	"mnqT": "",
	"lang": "ru",
}

for place in ["Лондон", "svo", "Череповец"]:
    url = f"https://wttr.in/{place}"	
    response = get(url, params=params)
    response.raise_for_status()
    print(response.text)

