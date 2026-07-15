import webbrowser as wb
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
root=tk.Tk()
root.geometry('500x200')
root.title("onNow")
root.config(bg="dark slate gray")
Title=tk.Label(root,text="OnNow",font=("Times New Roman", 15, "bold"),bg="light slate gray")
Title.place(anchor="center",relx=0.5,rely=0.1)
weather_result=ttk.Label(root)
weather_result.place(anchor="w",rely=0.5,relx=0.1)
def weatherFind():
    weather=requests.get("https://wttr.in/Melbourne?format=2")
    global weatherg
    weather=weather.text.strip()
    clean_text = weather.replace("\ufe0f", "")
    cleaner_text=clean_text.replace("+", "")
    cleanest_text=cleaner_text.replace("🌬", ", & wind").replace("☁", "☁,").replace("→", " up to ")
    
    weatherg = cleanest_text
    weather_result.config(text=f"Sky={weatherg}")
    
    
    
    
weather_get=tk.Button(root, text="Get weather",command=weatherFind)
weather_get.place(anchor="w",relx=0.1,rely=0.3) 

root.mainloop()