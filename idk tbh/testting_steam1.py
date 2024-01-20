import tkinter as tk
from PIL import ImageTk, Image
import os

win = tk.Tk()
win.title("Steam Dashboard")

width = win.winfo_screenwidth()
height = win.winfo_screenheight()

win.geometry("%dx%d" % (width, height))
win.resizable(False, False)

frame = tk.Frame(win, width=1920, height=1080)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

imgAchtergrond = Image.open("gaming_background.jpeg")
img2 = imgAchtergrond.resize((1920, 1080))
background_image = ImageTk.PhotoImage(img2)
background_label = tk.Label(frame, image=background_image)
background_label.pack()

title_label = tk.Label(win, text="Welkom bij jou Steam Dashboard", font=("Helvetica", 20), bg="black", fg="white")
title_label.place(x=width // 2, y=90, anchor='center')



win.mainloop()
