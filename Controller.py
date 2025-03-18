class Controller:
    def __init__(self, gui, weather):
        self.gui = gui
        self.weather = weather
        self.gui.setController(self)

    def search(self, cityName):


        return self.weather.getWeather(cityName)