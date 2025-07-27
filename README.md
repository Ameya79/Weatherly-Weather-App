# Weatherly 🌤️

**Weatherly** is a sleek and fast Streamlit-based weather dashboard that shows current weather, air quality, and a 3-day forecast for any city, powered by the [WeatherAPI.com](https://www.weatherapi.com/) service.

> 🔐 API Key is securely stored using `secrets.toml`.

---

## 🚀 Features

- 🌍 Real-time weather updates for any city
- 📊 Temperature, humidity, UV index, cloud cover, wind details
- 🫁 PM2.5-based air quality score with intuitive emoji scale
- 📅 3-day forecast with weather condition icons
- 🔄 Live local time and last updated info
- 🎨 Dynamic weather icons based on condition (e.g. sunny, storm, fog)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **WeatherAPI** (REST API)
- **Secrets.toml** for secure key management

---

## 🔐 Setup: `secrets.toml`

1. Go to [https://www.weatherapi.com/](https://www.weatherapi.com/) and create a free account.
2. Copy your API key.
3. In your Streamlit app folder, create a `.streamlit/secrets.toml` file:

```toml
[api]
key = "your_weather_api_key_here"
````

✅ **Never expose your API key in the main script.**

---

## ▶️ Run Locally

```bash
git clone https://github.com/yourusername/weatherly.git
cd weatherly
pip install -r requirements.txt
streamlit run app.py
```

Make sure to:

* Place your `secrets.toml` inside a `.streamlit/` directory.
* Rename your main script if not named `app.py`.

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your code to GitHub.
2. Go to [https://share.streamlit.io](https://share.streamlit.io) and connect your repo.
3. In the app settings, add your API key to **Secrets**:

```toml
[api]
key = "your_api_key"
```

4. Hit Deploy — you're live!

---

## 📌 Example API Used

```url
https://api.weatherapi.com/v1/forecast.json?key=YOUR_KEY&q=London&days=3&aqi=yes
```

Returns:

* Current weather
* Air quality (PM2.5)
* 3-day forecast

---

## 👤 Author

**Ameya Kulkarni**
💻[ GitHub](https://github.com/Ameya79)
📫 [Connect with me on LinkedIn](https://www.linkedin.com/in/ameya-kulkarni-a31b74246)
🎯 [View my Codolio](https://codolio.com/profile/Ameya%20Kulkarni)

---

## 📃 License

This project is open-source and free to use.

---

##  Notes

* Works best for cities with valid API coverage.
* The PM2.5 air quality score is color-coded:

  * 🟢 Excellent
  * 🟡 Moderate
  * 🟠 Poor
  * 🔴 Hazardous
* All images used are hosted from [Google Weather Icons](https://maps.gstatic.com/weather/).

---

```

DROP A STAR IF YOU FOUND THIS USEFUL :)


```
