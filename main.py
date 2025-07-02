import requests
import os
import streamlit as st


API_KEY = st.secrets["api"]["key"]
st.title('Weatherly🌤️')
    

city = st.text_input('Enter the name of the city: ')

def get_weather_image(condition):
    condition = condition.lower()


    if "partly" in condition and "cloud" in condition:
        return "https://cdn-icons-png.flaticon.com/128/15610/15610293.png"  # sun + clouds (partly cloudy)
    elif "sun" in condition or "clear" in condition:
        return "https://cdn-icons-png.flaticon.com/512/3222/3222800.png"  # bright sun
    elif "cloud" in condition:
        return "https://cdn-icons-png.flaticon.com/128/3313/3313998.png"  # bright cloud
    elif "mist" in condition:
        return "https://cdn-icons-png.flaticon.com/128/3313/3313998.png"  # bright cloud
    elif "light" or "rain" in condition:
        return "https://cdn-icons-png.flaticon.com/512/4005/4005803.png"  # colorful rain
    elif "snow" in condition:
        return "https://cdn-icons-png.flaticon.com/128/2315/2315309.png"  # snow
    elif "fog" in condition or "mist" in condition:
        return "https://cdn-icons-png.flaticon.com/512/2930/2930014.png"  # colorful fog
    elif "storm" in condition or "thunder" in condition:
        return "https://cdn-icons-png.flaticon.com/128/2831/2831999.png"  # storm
    else:
        return "https://cdn-icons-png.flaticon.com/512/3222/3222791.png"  # colorful rainbow cloud (default)
    

if city.strip() != "":
    url = f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'
    response = requests.get(url)


    try:
        data = response.json()
        if "error" in data:
            st.warning("⚠️ No matching location found. Please check the city name.")
        else:                                                                                                                       
            st.write(f"Weather in {data['location']['name']},{data['location']['country']}")
            st.write(f"🌡️ Temperature: {data['current']['temp_c']} °C")
            st.write(f"🌡️ Feels Like: {data['current']['feelslike_c']} °C")
            st.write(f"☁️ Condition: {data['current']['condition']['text']}")
            st.write(f"💧 Humidity: {data['current']['humidity']}%")
            st.write(f"🌧️ Precipitation: {data['current']['precip_mm']} mm")
            st.write(f"🌬️ Wind: {data['current']['wind_kph']} km/h")
            st.write(f"🔆 UV Index: {data['current']['uv']}")
            st.write(f"🕒 Local Time: {data['location']['localtime']}")
            st.write(f"🕰️ Last Updated: {data['current']['last_updated']}")

            img_url = get_weather_image(data['current']['condition']['text'])
            st.image(img_url, width=120)
    except:
        st.error("❌ Could not fetch weather. Check the city name.")






st.markdown("---")
st.markdown(
    "🔧 *Built by [Ameya Kulkarni](https://www.linkedin.com/in/ameya-kulkarni-a31b74246) • "
    "[GitHub](https://github.com/Ameya79)*"
)

# as per weather api documentation the data of weather is stored in such way :

# {
#   "location": {
#     "name": "London",
#     "country": "UK"
#   },
#   "current": {
#     "temp_c": 14.0,
#     "condition": {
#       "text": "Partly cloudy"
#     }
#   }
# }
