import webbrowser as wb
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry('500x200')
root.title("onNow")
root.config(bg="dark slate gray")
Title=tk.Label(root,text="OnNow",font=("Times New Roman", 15, "bold"),bg="light slate gray")
Title.place(anchor="center",relx=0.5,rely=0.1)
def weatherFind():
    weather=wb.open_new_tab("wttr.in/Melbourne?format=3")
    print(f"{weather}")
weather_get=tk.Button(root, text="Get weather",command=weatherFind)
weather_get.place(anchor="w",relx=0.1,rely=0.5)


root.mainloop()