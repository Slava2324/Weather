from requests import get


parameters = {
	"m": "",
	"n": "",
	"q": "",
	"T": "",
	"lang": "ru",
}


request_template = "https://wttr.in/{0}"
for place in ["Лондон", "svo", "Череповец"]:
	request = get(urljoin(request_template.format(place), params=parameters))
	request.raise_for_status()
	print(request.text)
