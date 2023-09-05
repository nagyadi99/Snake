import customtkinter
import tkinter
from main import *


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.title("Customtkinter App By Nagyadi")
app.geometry("300x300")

frame = customtkinter.CTkFrame(
    master=app, width=200, height=200, corner_radius=10, bg_color="white"
)
frame.pack(padx=20, pady=20)


def game():
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), "Right")
    onkey(lambda: change(-10, 0), "Left")
    onkey(lambda: change(0, 10), "Up")
    onkey(lambda: change(0, -10), "Down")
    move()
    done()


def button_function1():
    print("Game started")
    game()


button1 = customtkinter.CTkButton(master=frame, text="Play1", command=button_function1)
button1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

app.mainloop()
