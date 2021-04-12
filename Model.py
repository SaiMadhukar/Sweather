import requests,enum,json
from typing import NamedTuple
from requests.exceptions import HTTPError

# S.W.E.A.T.H.E.R
URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "42587ef7d4a4fd37f19323c349cfbd6f"

#MARK:-     Model
class WeatherType(enum.Enum):
	rainy = 1
	snow = 2
	clearSky = 3

class WeatherInfo(NamedTuple):
    weatherId: int
    wType: WeatherType
    weatherDesc: str
    minTemp: int
    maxTemp: int
    temp: int
    location: str

class Product(NamedTuple):
	name: str
	minTemp: int
	maxTemp: int
	waterProof: bool

#MARK:- Main Class
class WeatherPredictor:

	predictionTable = []

	def getWeatherInfo(self,city,state):

		location = city + ",  " + state
		
		try:
			complete_url = URL + "appid=" + API_KEY + "&q=" + location + "&units="  + "imperial"
			r = requests.get(url = complete_url)
			jsonResponse = r.json()

			if jsonResponse["cod"] == 200:
				return self.parseResponse(location, jsonResponse)
		except HTTPError as http_err:
			print('HTTP error occurred: ',{http_err})
		except Exception as err:
			print('Other error occurred:', err)

	def parseResponse(self,location, data):

		main = data["main"]
		tempMin = main["temp_min"]
		tempMax = main["temp_max"]
		tempCurrent = main["temp"]

		weather = data["weather"]
		wID = int(weather[0]["id"])
		wType = weather[0]["main"]
		wDesc = weather[0]["description"]

		
		wType = WeatherType.clearSky
		if 600 <= wID <= 699:
			print("Snow Weather")
			wType = WeatherType.snow
		elif 200 <= wID <= 599:
			print("Rainy Weather")
			wType =  WeatherType.rainy
		else:
			print("Clear Sky")
			wType = WeatherType.clearSky

		info = WeatherInfo(wID, wType, wDesc, tempMin, tempMax, tempCurrent, location)
		return info

	def inputData(self):

		try:
			print("Enter Your Location Details")
			city = input("City: ")
			state = input("State: ")
		except SyntaxError:
			print("Invalid City or State. Please Provide the correct details")
			print("Eg: Harrison, New Jersey")

			print("-----------------------------------------------------------")
			self.startGame()
			return

		if city == None  or state == None or city == "" or  state == "":
			print("Invalid City or State. Please Provide the correct details")
			print("Eg: Harrison, New Jersey")
			self.startGame()
			return

		return city,state

	def parseConfigData(self):
		with open('config.json') as f:
			data = json.load(f)
		recommendations = data['available_recommendations']
		for p in recommendations:
			self.predictionTable.append(Product(p['name'],p['min_temp'],p['max_temp'],p['waterproof']))
		#print(self.predictionTable)

	def startGame(self):
		city, state = self.inputData()
		weatherInfo = self.getWeatherInfo(city, state)
		#print("Weather Info: \n", weatherInfo)

		self.predict(weatherInfo)

	def predict(self, info):

		recommendations = []
		for product in self.predictionTable:
			#Temperature Range
			if  product.minTemp <= info.temp <= product.maxTemp:
				#waterproof ? [SNOW, RAINY] : [ClearSky]
				if info.wType == WeatherType.clearSky and product.waterProof == False:
					recommendations.append(product)
				elif (info.wType == WeatherType.snow or info.wType == WeatherType.rainy) and product.waterProof == True:
					recommendations.append(product)

		self.printProduct(recommendations, info.wType)


	def printProduct(self,recommendations, wType):


		if len(recommendations) < 1:
			print("You are good to go....Have a nice day;)")

		if wType == WeatherType.rainy:
			print("It's Rainy Outside!!!! You might need")
		elif wType == WeatherType.snow:
			print("Today is a snow day...don't forget to bring")
		else:
			print("Clear Sky!!!! Please Get a")


		for index,product in enumerate(recommendations):
			print(index+1,".", product.name)



if __name__ == '__main__':
	w = WeatherPredictor()
	w.parseConfigData() #Conditions for predictions
	w.startGame()

	

