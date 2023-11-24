import requests

url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

headers = {
	"accept": "application/json",
	"X-RapidAPI-Key": "bedc5f23f3mshdaffc60c589e4abp128941jsne9ae4b702d70",
	"X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

obj = response.json()

print(obj['value'])