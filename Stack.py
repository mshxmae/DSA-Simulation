from customtkinter import *
import tkinter as tk

set_appearance_mode("light")

app = CTk()
app.title("Stack Visualization")
app.geometry("600x400")
app.grid_rowconfigure((0,1), weight=1)
app.grid_columnconfigure((0,1), weight=1)

# LEFT FRAME
display = CTkFrame(app, fg_color="blue", width=400)
display.grid(row=0, column=1, rowspan=2, sticky='nsew')


info_disp = CTkFrame(app, fg_color="red")
info_disp.grid(row=0, column=0, sticky='nsew')

input = CTkFrame(app, fg_color="black")
input.grid(row=1, column=0, sticky='nsew')


app.mainloop()