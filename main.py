from requests import get


get_parameters = {
	"m": "",
	"n": "",
	"q": "",
	"T": "",
	"lang": "ru",
}


request_template = "https://wttr.in/{0}"
for place in ["Лондон", "svo", "Череповец"]:
	request = get(request_template.format(place), params=get_parameters)
	request.raise_for_status()
	print(request.text)
