from requests import get, raise_for_status


request_template = "https://wttr.in/{0}?m?n?q?T&lang=ru"
for place in ["Лондон", "Аэропорт Шереметьево", "Череповец"]:
	request = requests.get(request_template.format(place))
	request.raise_for_status()
	print(request.text)