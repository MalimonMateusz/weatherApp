import tkinter as tk
from PIL import Image, ImageTk



class Gui:
    def __init__(self):


        self.root = tk.Tk()
        self.root.title("WeatherApp")
        self.root.geometry("400x300")
        self.controller = None
        self.image = None

        image = Image.open("photos/sun.png")
        photo = ImageTk.PhotoImage(image)

        self.root.iconphoto(False, photo)

        windowWidth = self.root.winfo_width()
        windowHeight = self.root.winfo_height()

        self.pictureFrame = tk.Frame(self.root,borderwidth=1, relief="solid", width=200)
        self.infoFrame = tk.Frame(self.root, borderwidth=1,relief="solid", bg="#9900cc")
        self.interactionFrame = tk.Frame(self.root, borderwidth=1, relief="solid", bg="#3399ff")

        self.photoLabel = tk.Label(self.pictureFrame, bg="#008080")
        self.cityNameLabel= tk.Label(self.infoFrame, text="City: ", font=("Calibri", 16  , "bold"), fg="black" , bg="#9900cc")
        self.weatherDescriptionLabel= tk.Label(self.infoFrame, text="Weather: ", font=("Calibri", 12, "bold"), fg="black" , bg="#9900cc")
        self.tempLabel= tk.Label(self.infoFrame, text="Temp: ", font=("Calibri", 12, "bold"), fg="black" , bg="#9900cc")
        self.humidityLabel = tk.Label(self.infoFrame, text="Humidity: ", font=("Calibri", 12, "bold"), fg="black" , bg="#9900cc")


        searchButton = tk.Button(self.interactionFrame, text="Search", command=self.get_input)
        self.entry = tk.Entry(self.interactionFrame)


        self.photoLabel.pack(fill="both", expand=True)

        self.cityNameLabel.grid(row=0, column=1, sticky="w", padx=10, pady = 10)
        self.weatherDescriptionLabel.grid(row=1, column=1, sticky="w", padx=10, pady = 10)
        self.tempLabel.grid(row=2, column=1, sticky="w", padx=10, pady = 10)
        self.humidityLabel.grid(row=3, column=1, sticky="w", padx=10, pady = 10)

        self. interactionFrame.grid_rowconfigure(0, weight=1)
        self. interactionFrame.grid_rowconfigure(1, weight=1)
        self.  interactionFrame.grid_rowconfigure(2, weight=1)
        self.  interactionFrame.grid_columnconfigure(0, weight=1)
        self.   interactionFrame.grid_columnconfigure(1, weight=1)
        self. interactionFrame.grid_columnconfigure(2, weight=1)

        self.entry.grid(row=1, column=1, pady=5, sticky="ew")
        searchButton.grid(row=1, column=2, pady=5)

        self.pictureFrame.place(x= 0, y=0, width=200, height= (windowHeight/4) *3 )
        self.infoFrame.place(x= windowWidth/2, y=0, width=200, height= (windowHeight/4) *3)
        self. interactionFrame.place(x= 0, y=(windowHeight/4)*3, width=windowWidth, height=windowHeight/3)






    def get_input(self):
        cityName = self.entry.get()



        if cityName.strip():





            data, self.image = self.controller.search(cityName)


            if self.image is not None:
                self.image = Image.open("photos/sun.png")


            if data:
                self.weatherDescriptionLabel.config(text="Weather: " + data[0])
                self.tempLabel.config(text="Temp: " + data[1] + " °C")
                self.humidityLabel.config(text="Humidity: " + data[2] + "%")
                self.cityNameLabel.config(text="City: " + data[3])

                if self.image is None:
                    self.image = Image.open("photos/error.png")

                self.image = self.image.resize((self.pictureFrame.winfo_width(), self.pictureFrame.winfo_height()))
                self.image = ImageTk.PhotoImage(self.image)
                self.photoLabel.config(image=self.image)
        else:
            print("Entry is blank :D")




    def setController(self, controler):
        self.controller = controler


    def startTheProgram(self):
        self.root.mainloop()

