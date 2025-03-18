from Controller import Controller
from Gui import Gui
from Weather import Weather

gui = Gui()
weather = Weather()



controller = Controller(gui,weather)
gui.startTheProgram()




weather.getWeather("Barcelona")