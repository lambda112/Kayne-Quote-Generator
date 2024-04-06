from tkinter import *
from PIL import ImageTk, Image
import requests 

window = Tk()
window.config(background="black")
window.title("Kanye Quote Generator")

def generate_text():
    response = requests.get(url = "https://api.kanye.rest")
    response.raise_for_status()
    content = response.json()["quote"]
    canvas.itemconfigure(text, text=content)


# Canvas 
canvas = Canvas(height=500, width=500)
canvas.grid(row = 1, column=0)
canvas.config(background="#141312")

# Background
image = ImageTk.PhotoImage(Image.open("image.jpeg"), size=(550, 500))
canvas.create_image(250, 250, image = image)
canvas.create_text(250, 80, text = "Kanye Quote Generator", fill="white", font=("arial", 25, "bold"))
text = canvas.create_text(250, 250,text="Generate Quote With The Kanye Button!", font=("arial", 16, "bold"), fill="white", width=260)

# Button
kanye_image = ImageTk.PhotoImage(Image.open("kanye.jpg"), size=(100, 100))
kanye_button = Button(image=kanye_image, command=generate_text)
canvas.create_window(250, 500, window = kanye_button, anchor="s")

window.mainloop()