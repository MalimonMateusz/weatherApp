from http.client import responses
from io import BytesIO
import requests
from PIL import Image, ImageTk



class Weather:

    def __init__(self):
        self.apiKey = "http://api.openweathermap.org/data/2.5/weather?q="
        self.photoApiKey = "https://api.unsplash.com/search/photos?client_id=" # YOU NEED TO PUT YOUR UNSPLASH.COM API DUE TO CONFIDENTIALITY I CAN NOT PUT MINE !


    def getWeather(self, city):

        requestUrl = self.apiKey + city+"&appid=a0b6fb9d4214ae3bfcd82571e419f1ef"
        response = requests.get(requestUrl)

        photoRequestUrl = self.photoApiKey + city
        photoResponse= requests.get(photoRequestUrl)

        img = None

        if photoResponse.status_code == 200:
            data = photoResponse.json()


            photoUrl = data['results'][0]['urls']['regular']
            img = self.get_image_from_url(photoUrl)






        else:
            print(f"Error {response.status_code} occured: {response.text}")





        if response.status_code == 200:
            data = response.json()


            weather = [
                data['weather'][0]['description'],
                data['main']['temp'],
                data['main']['humidity'],
                data.get("name")
            ]

            weather[1] = round(weather[1]-273.15)

            weather = [str(item) for item in weather]







            return weather, img


        else:
            print(f"Error {response.status_code}: {response.text}")



    def get_image_from_url(self, url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        return img






