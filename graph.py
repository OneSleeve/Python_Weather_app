import weather_request
import json
import matplotlib.pyplot as plot
import time

def make_graph(json_data):
	time_stamps = []
	temps = []
	for element in json_data["list"]:
		time_stamps.append(element["dt_txt"])
		temps.append(element["main"]["temp"])

	plot.plot(time_stamps, temps)
	plot.gca().set_xticklabels(time_stamps, rotation=90)

	plot.ylim(-20, 40)

	plot.xlabel("time")
	plot.ylabel("temp")
	plot.title("5 day / 3 hour temp forecast")

	plot.grid()
	plot.tight_layout()

	plot.show()

if __name__ == "__main__":
	file = open("data.json", "r")
	json_data = json.load(file)

	make_graph(json_data)