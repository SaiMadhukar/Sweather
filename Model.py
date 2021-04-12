import requests
import enum
from typing import NamedTuple
from requests.exceptions import HTTPError

# S.W.E.A.T.H.E.R
URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "42587ef7d4a4fd37f19323c349cfbd6f"


class weatherType(enum.Enum):
	rainy = 1
	snow = 2
	clearSky = 3

class WeatherInfo(NamedTuple):
    weatherId: int
    weatherType: weatherType
    weatherDesc: str
    minTemp: int
    maxTemp: int
    temp: int
    location: str

def getWeatherInfo(city,state):

	location = city + ",  " + state
	  
	try:
		complete_url = URL + "appid=" + API_KEY + "&q=" + location + "&units="  + "imperial"
		r = requests.get(url = complete_url)
		jsonResponse = r.json()

		if jsonResponse["cod"] == 200:
			return parseResponse(location, jsonResponse)
	except HTTPError as http_err:
		print('HTTP error occurred: ',{http_err})
	except Exception as err:
		print('Other error occurred:', err)

def parseResponse(location, data):

	main = data["main"]
	tempMin = main["temp_min"]
	tempMax = main["temp_max"]
	tempCurrent = main["temp"]

	weather = data["weather"]
	wID = int(weather[0]["id"])
	wType = weather[0]["main"]
	wDesc = weather[0]["description"]

	
	wType = weatherType.clearSky
	if 600 <= wID <= 699:
		print("Snow Weather")
		wType = weatherType.snow
	elif 200 <= wID <= 599:
		print("Rainy Weather")
		wType =  weatherType.rainy
	else:
		print("Clear Sky")
		wType = weatherType.clearSky

	info = WeatherInfo(wID, wType, wDesc, tempMin, tempMax, tempCurrent, location)
	return info


def inputData():

	try:
		print("Enter Your Location Details")
		city = input("City: ")
		state = input("State: ")
	except SyntaxError:
		print("Invalid City or State. Please Provide the correct details")
		print("Eg: Harrison, New Jersey")

		print("-----------------------------------------------------------")
		startGame()
		return

	if city == None  or state == None or city == "" or  state == "":
		print("Invalid City or State. Please Provide the correct details")
		print("Eg: Harrison, New Jersey")
		startGame()
		return

	return city,state

def startGame():

	city, state = inputData()
	weatherInfo = getWeatherInfo(city, state)
	print("Weather Info: \n", weatherInfo)

def parseConfigData():
	print("Parsing")

if __name__ == '__main__':
	parseConfigData()
	startGame()

	

