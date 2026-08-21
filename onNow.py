import requests
__Version__="v0.1.0"
def weatherFind():
    weather=requests.get("https://wttr.in/?format=2")
    global weatherg
    weather=weather.text.strip()
    clean_text = weather.replace("\ufe0f", "").replace("🌬", ", & wind direction & speed is ").replace("☁", "☁,").replace("+", "")  
    weatherg = clean_text
    extra=requests.get("https://v2.wttr.in")
    extrac=extra.text.strip()
    extracclean=extrac.replace("\ufe0f", "").split("\n")
    print(f"Sky = {weatherg}")
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
    sunset_placeholder=sunset_placeholder.replace("\ufe0f", "").replace("\x1b", "").replace("\033", "").replace("[2m","").replace("[0m","").replace("   : ",": ").replace("      |"," | ")
    sunrise_placeholder=sunrise_placeholder.replace("\ufe0f", "").replace("\x1b", "").replace("\033", "").replace("[2m","").replace("[0m","").replace("  : ",": ")
    sunrise_placeholder2 = sunrise_placeholder.split("|", 1)[1]
    print(f"{sunrise_placeholder2}\n{sunset_placeholder}")

def newsget():
    headers = {"User-Agent": "curl/7.81.0"}
    news = requests.get("http://getnews.tech", headers=headers)
    print(f"{news.text}")

if __name__ == "__main__":
    weatherFind()
    newsget()

   