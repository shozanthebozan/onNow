import tkinter as tk
from tkinter import messagebox
import requests
__version__="v0.0.6"
root=tk.Tk()
root.geometry('500x200')
root.title("onNow")
root.config(bg="dark slate gray")
Title=tk.Label(root,text="OnNow",font=("Times New Roman", 15, "bold"),bg="dark slate gray")
Title.place(anchor="center",relx=0.5,rely=0.1)
weather_result=tk.Label(root,bg="light slate grey")
weather_result.place(anchor="w",rely=0.5,relx=0.1)
weather_result_sun=tk.Label(root,bg="light slate grey")
weather_result_sun.place(anchor="w",rely=0.8,relx=0.1)
def weatherFind():
    weather=requests.get("https://wttr.in/?format=2")
    global weatherg
    weather=weather.text.strip()
    clean_text = weather.replace("\ufe0f", "").replace("🌬", ", & wind direction & speed is ").replace("☁", "☁,").replace("→", " up to ").replace("+", "")    
    weatherg = clean_text
    weather_result.config(text=f"Sky={weatherg}")
    extra=requests.get("https://v2.wttr.in")
    extrac=extra.text.strip()
    extracclean=extrac.replace("\ufe0f", "").split("\n")
    weather_placehold=""
    timezone_placehold=""
    now_placehold=""
    weatherReport_placehold=""
    sunrise_placeholder = "" 
    sunset_placeholder = ""
    
    for line in extracclean:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue
                
            if "─" in cleaned_line or "┌" in cleaned_line or "┐" in cleaned_line or "└" in cleaned_line or "┘" in cleaned_line:
                continue
            if "Weather:" in cleaned_line:
                weather_placeholder = cleaned_line
            elif "Timezone:" in cleaned_line:
                timezone_placeholder = cleaned_line
            elif "Now :" in cleaned_line:
                now_placeholder = cleaned_line
            elif "Weather report:" in cleaned_line:
                weatherReport_placeholder = cleaned_line
            elif "Sunrise:" in cleaned_line:
                sunrise_placeholder = cleaned_line
            elif "Sunset:" in cleaned_line:
                sunset_placeholder = cleaned_line
    
    sunset_placeholder=sunset_placeholder.replace("\ufe0f", "").replace("\x1b", "").replace("\033", "").replace("[2m","").replace("[0m","")
    sunrise_placeholder=sunrise_placeholder.replace("\ufe0f", "").replace("\x1b", "").replace("\033", "").replace("[2m","").replace("[0m","")
    sunrise_placeholder2 = sunrise_placeholder.split("|", 1)[1]
    weather_result_sun.config(text=f"{sunrise_placeholder2}\n{sunset_placeholder}")
    
    
    
weather_get=tk.Button(root, text="Get weather",command=weatherFind,bg="light slate grey")
weather_get.place(anchor="w",relx=0.1,rely=0.3) 
version_label=tk.Label(root,text=f"{__version__}",bg="dark slate grey")
version_label.place(anchor="se",rely=1.0,relx=1.0)

root.mainloop()