import requests
import json

def request_weather(lat, lon, api_key):
	request = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&mode=json")
	return request

if __name__ == "__main__":
	file = open("api_key.json", "r")
	key_dict = json.load(file)
	key = key_dict["appid"]

	data = request_weather("52.31","13.24",key).json()

	file = open("data.json", "w")
	file.write(json.dumps(data))