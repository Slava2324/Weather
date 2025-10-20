import pandas as pd
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


start_date = "2024-11-19"
end_date = "2024-11-26"


def get_coord_by_city(city_name):
	url_coordinates = "https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-postal-code@public/records"
	params_coordinates = {
		"limit": 1,
		"where": city_name,
	}

	response_coordinates_api = requests.get(url_coordinates, params=params_coordinates)
	response_coordinates_api.raise_for_status()

	if (response := response_coordinates_api.json())['total_count'] != 0:
		coords = response['results'][0]['coordinates']
		longitude = coords['lon']
		latitude = coords['lat']
		return longitude, latitude
	else:
		print("Город не найден! Проверьте правильность написания. Если всё верно, значит города нет в базе данных.")
		exit()


def get_weather(longitude, latitude):
	url_weather = "https://archive-api.open-meteo.com/v1/era5"
	params_weather = {
		"latitude": latitude,
		"longitude": longitude,
		"start_date": start_date,
		"end_date": end_date,
		"hourly": "temperature_2m"
	}

	response_weather_api = requests.get(url_weather, params=params_weather)
	response_weather_api.raise_for_status()

	weather_json = response_weather_api.json()

	weather_time = weather_json["hourly"]["time"]
	weather_temperature = weather_json["hourly"]["temperature_2m"]
	return weather_time, weather_temperature


def create_dataframe(weather_time, weather_temperature):
	data = {
		"time": weather_time,
		"temp": weather_temperature
	}

	dataframe = pd.DataFrame(data)
	dataframe['time'] = pd.to_datetime(dataframe['time'])
	return dataframe


def show_data(data, city):
	plt.figure(figsize=(10, 6))
	plt.plot(data['time'], data['temp'], label="label")
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.title(f'Погода в городе {city} за временной промежуток')
	plt.xlabel("Дата")
	plt.ylabel("Температура, C")
	plt.show()


def main():
	city_name = f'"{input("Введите город: ")}"'
	longitude, latitude = get_coord_by_city(city_name)
	time, temperature = get_weather(longitude, latitude)
	data = create_dataframe(time, temperature)
	show_data(data, city_name)


if __name__ == '__main__':
	main()
