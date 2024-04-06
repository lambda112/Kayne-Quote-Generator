from tkinter import *
from PIL import ImageTk, Image
import requests 

window = Tk()
window.config(background="black")
window.title("Kanye Quote Generator")

response = requests.get(url = "https://api.kanye.rest")
response.raise_for_status()
content = response.json()["quote"]
print(content)

canvas = Canvas(height=500, width=500)
canvas.grid(row = 0,column=0)
canvas.config(background="#141312")
image = ImageTk.PhotoImage(Image.open("image.jpeg"), size=(550, 500))
canvas.create_image(250, 250, image = image)
canvas.create_text(250,250,text=content, font=("arial", 20, "bold"), fill="white", width=260)

window.mainloop()