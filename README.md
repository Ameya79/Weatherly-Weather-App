# 🌤️ Weatherly - Real-Time Weather Dashboard

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![Streamlit](https://img.shields.io/badge/streamlit-1.x-red)]()
[![WeatherAPI](https://img.shields.io/badge/weatherapi-REST%20API-lightgrey)]()
[![License](https://img.shields.io/badge/license-MIT-orange)]()

**Weatherly** is a sleek, fast, and responsive weather dashboard built with **Streamlit**, fetching real-time weather, air quality, and a 3-day forecast for any city — powered by [WeatherAPI.com](https://www.weatherapi.com/).

🌐 **Live Project:** [weatherly-smzufohbhuex5grhcavnd4.streamlit.app](https://weatherly-smzufohbhuex5grhcavnd4.streamlit.app)

> 🔐 API keys are securely stored using `secrets.toml` — no hardcoding.

---

## 🚀 Features
- 🌍 **Real-time weather** for any city worldwide
- 📊 **Details**: Temperature, humidity, UV index, cloud cover, wind speed/direction
- 🫁 **Air quality** score (PM2.5-based) with emoji scale
- 📅 **3-day forecast** with dynamic weather icons
- ⏱ **Live local time** + last updated timestamp
- 🎨 Auto-switching weather icons (sunny, storm, fog, etc.)

---

## 🛠 Tech Stack
| Component     | Technology         |
|---------------|--------------------|
| Backend       | Python             |
| Frontend/UI   | Streamlit          |
| API           | WeatherAPI (REST)  |
| Secrets Mgmt  | `secrets.toml`     |
| Deployment    | Streamlit Cloud 🌨️ |

---

## 🔐 API Key Setup (`secrets.toml`)
1. Sign up at [WeatherAPI.com](https://www.weatherapi.com/) and get your free API key.
2. In your Streamlit app folder, create a `.streamlit/secrets.toml` file:

[api]
key = "your_weather_api_key_here"

✅ Never commit your API key to GitHub — keep it in secrets.toml.


---

▶️ Run Locally

$ git clone https://github.com/yourusername/weatherly.git
$ cd weatherly
$ pip install -r requirements.txt
$ streamlit run app.py

Make sure:

Your secrets.toml is inside .streamlit/ folder

Your main file is named app.py (or update the run command)



---

☁️ Deploy on Streamlit Cloud

1. Push your code to GitHub


2. Go to share.streamlit.io and connect your repo


3. Add your API key in App Settings → Secrets:



[api]
key = "your_api_key"

4. Deploy — you’re live!




---

📌 Example API Call

https://api.weatherapi.com/v1/forecast.json?key=YOUR_KEY&q=London&days=3&aqi=yes

Returns:

Current weather

PM2.5 air quality

3-day forecast



---

📝 Notes

Works best for cities with API coverage

PM2.5 Air Quality Scale:

🟢 Excellent

🟡 Moderate

🟠 Poor

🔴 Hazardous


Icons sourced from Google Weather Icons



---

👤 Author

Ameya Kulkarni


---

📜 License: MIT — free to use, modify, and share.

⭐ If Weatherly helped you, drop a star!

---


