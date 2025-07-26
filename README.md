# 🌦️ Weatherly

**Weatherly** is a sleek, lightweight, and beginner-friendly weather web app built with [Streamlit](https://streamlit.io/) and powered by the [WeatherAPI](https://www.weatherapi.com/). It provides real-time weather data for any city in the world—temperature, humidity, wind, condition icons, and much more—wrapped in a clean and interactive UI.

---

## 🔍 Features

- 🌍 Search weather for **any city**
- 🌡️ Real-time temperature, humidity, and pressure
- 💨 Wind speed and direction
- 🌤️ Beautiful condition icons (sunny, cloudy, rain, etc.)
- 🕒 Local time of the city
- 🔄 Fast and live updates using Streamlit
- 🍋 Super simple, minimalistic UI for distraction-free use

---

## 🚀 Live Demo

**Run it locally** or host using platforms like **Streamlit Community Cloud**, **Render**, or **Hugging Face Spaces**.

> ⚠️ *Note: WeatherAPI requires a free API key for usage. Instructions below.*

---

## 🛠️ Tech Stack

| Tool         | Purpose                              |
|--------------|--------------------------------------|
| Python       | Programming language                 |
| Streamlit    | Web framework for UI and interaction |
| WeatherAPI   | Source of real-time weather data     |
| Requests     | Handling HTTP API calls              |

---


## 🔒 Security Features

* API key is loaded via `.env` (never hardcoded).
* 🍋 Squeeze-secure! Weather data is fetched live and nothing is stored on the server.
* All requests are stateless and safe. No cookies, no tracking.

---

## 🧠 How It Works

1. User inputs city name in the Streamlit UI.
2. `requests` module sends a GET request to the WeatherAPI endpoint.
3. Data is fetched and parsed (temperature, humidity, etc.).
4. UI dynamically updates with clean visual output.

---

## 📝 Code Structure

```
weatherly/
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── .env                 # Environment file for API key
└── README.md            # This file!
```

---

## 💡 Future Improvements

* 📍 Location-based search using IP or geolocation
* ⏳ 3-day forecast and hourly breakdowns
* 🌗 Day/Night mode
* 🧠 AI-based weather insights or clothing suggestions

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 OPEN SOURCE  

## 🙋‍♂️ Author

Made with ❤️ by [Ameya](https://github.com/Ameya79)

```

