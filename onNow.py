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
weather_result_sun.place(anchor="w",rely=0.6,relx=0.1)
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
    weather.placehold=""
    timezone.placehold=""
    # keep making these placeholder variables and then add em to for like if "Weather:" in line:
                                                                            # weather_placehold = line.strip()
    for line in extracclean:
        if "Weather:" in line:
            line=(line.strip())
        elif "Timezone:" in line:
            print(line.strip())
        elif "Now  :" in line:
            print(line.strip())
        elif "Weather report:" in line:
            print(line.strip())
    
    
    
    print(f"{extracclean}")
    
    
    
    
weather_get=tk.Button(root, text="Get weather",command=weatherFind,bg="light slate grey")
weather_get.place(anchor="w",relx=0.1,rely=0.3) 
version_label=tk.Label(root,text=f"{__version__}",bg="dark slate grey")
version_label.place(anchor="se",rely=1.0,relx=1.0)

root.mainloop()