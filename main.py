import requests
import os
import streamlit as st


API_KEY = st.secrets["api"]["key"]
st.title('Weatherly🌤️')
    

city = st.text_input('Enter the name of the city: ')

def get_weather_image(condition):
    condition = condition.lower()


    if "partly" in condition and "cloud" in condition:
        return "https://maps.gstatic.com/weather/v1/party_cloudy_dark.svg"  # sun + clouds (partly cloudy)
    elif "sun" in condition or "clear" in condition:
        return "https://maps.gstatic.com/weather/v1/sunny_dark.svg"  # bright sun
    elif "cloud" in condition:
        return "https://maps.gstatic.com/weather/v1/cloudy_dark.svg"  # bright cloud
    elif "mist" in condition:
        return "https://maps.gstatic.com/weather/v1/mostly_cloudy_dark.svg"  # bright cloud
    elif "light" in condition and "rain" in condition:
        return "https://maps.gstatic.com/weather/v1/drizzle_dark.svg"  # colorful rain
    elif "heavy" in condition and "rain" in condition:
        return "https://maps.gstatic.com/weather/v1/heavy_dark.svg"  # colorful rain
    elif "snow" in condition:
        return "https://maps.gstatic.com/weather/v1/snow_showers_dark.svg"  # snow
    elif "fog" in condition or "mist" in condition:
        return "https://maps.gstatic.com/weather/v1/cloudy_dark.svg"  # colorful fog
    elif "storm" in condition or "thunder" in condition:
        return "https://maps.gstatic.com/weather/v1/strong_tstorms_dark.svg"  # storm
    else:
        return "https://maps.gstatic.com/weather/v1/mostly_sunny_dark.svg"  # colorful rainbow cloud (default)
    


def current_air_quality(pm25):
    if pm25 <= 12:
        return "🟢 Excellent"
    elif pm25 <= 35:
        return "🟢 Good"
    elif pm25 <= 55:
        return "🟡 Moderate"
    elif pm25 <= 150:
        return "🟠 Poor"
    else:
        return "🔴 Hazardous"


if city.strip() != "":
    url = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3&aqi=yes"
    response = requests.get(url)


    try:
        data = response.json()
        if "error" in data:
            st.warning("⚠️ No matching location found. Please check the city name.")
        else:    
            #header using                                                                                                                   
            st.markdown(f"### 📍 {data['location']['name']}, {data['location']['region']}, {data['location']['country']}")
            st.markdown(f"🕒 Local Time: {data['location']['localtime']}")
            #Weather airquality and img
            col1,col2 = st.columns(2)
            with col1:
                st.markdown(f"☁️ Condition: {data['current']['condition']['text']}")
                st.markdown(f"🌡️ Temperature: {data['current']['temp_c']} °C")
                st.markdown(f"🌡️ Feels Like: {data['current']['feelslike_c']} °C")
                pm25 = data["current"]["air_quality"]["pm2_5"]
                score = round((1 - min(pm25, 150) / 150) * 100)
                label = current_air_quality(pm25)
                st.markdown("🫁 Air Quality")
                st.markdown(f" {score}% {label}")

            with col2:
                img_url = get_weather_image(data['current']['condition']['text'])
                st.image(img_url, width=100)
            st.markdown("---")

            col1,col2,col3 = st.columns(3)
            with col1: #misc
                st.markdown(f"💧 Humidity: {data['current']['humidity']}%")
                st.markdown(f"🌬️ Wind: {data['current']['wind_kph']} km/h")
                st.markdown(f"🧭 **Direction:** {data['current']['wind_dir']}")
            with col2:
                st.markdown(f"🌧️ **Precipitation:** {data['current']['precip_mm']} mm")
                st.markdown(f"☁️ **Cloud Cover:** {data['current']['cloud']}%")
                st.markdown(f"⬇️ **Pressure:** {data['current']['pressure_mb']} mb")

            with col3:
                st.markdown(f"🔆 **UV Index:** {data['current']['uv']}")
                is_day = "Yes 🌞" if data['current']['is_day'] else "No 🌙"
                st.markdown(f"🌞 **Daytime:** {is_day}")
                st.markdown(f"🕰️ **Updated At:** `{data['current']['last_updated']}`")

                
            st.markdown("### 🌤️ 3-Day Forecast")

            for day in data['forecast']['forecastday']:
                date = day['date']
                condition = day['day']['condition']['text']
                temp = day['day']['avgtemp_c']
                icon = "https:" + day['day']['condition']['icon']

                st.markdown(f"**📅 {date}**")
                st.image(icon, width=50)
                st.markdown(f"🌡️ {temp} °C - {condition}")
                
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
