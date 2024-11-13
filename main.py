from requests import get


request_template = "https://wttr.in/{0}?m?n?q?T&lang=ru"
for place in ["Лондон", "Аэропорт Шереметьево", "Череповец"]:
	request = get(request_template.format(place))
	request.raise_for_status()
	print(request.text)