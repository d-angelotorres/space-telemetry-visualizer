# 🚀 Space Telemetry Visualizer

A simple Flask web app that fetches and displays data from the most recent **SpaceX launch**, including launch name, date, and external links to details like Wikipedia and webcast streams.

> ⚠️ This project uses the [SpaceX API (v5)](https://github.com/r-spacex/SpaceX-API), which appears to no longer be maintained. The latest launch data retrieved is from **2022**. However, the app remains functional and demonstrates API integration, Flask development, and basic front-end templating.

---

## 🛰️ Features

- Fetches most recent launch data from the SpaceX API
- Displays launch name and UTC date
- Shows links to Wikipedia and webcast (if available)
- Handles missing data gracefully with fallbacks
- Styled with simple, responsive HTML + CSS

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, Jinja2 templates, CSS
- **API**: SpaceX REST API (v5)

---

## 🚧 Known Limitations

- As of April 2025, the SpaceX API data is outdated and has not been updated since 2022.
- Project was kept live for practice and learning purposes — and to demonstrate working with external APIs, debugging, and user-friendly error handling.

---

## 📦 Getting Started

1. **Clone this repository**
   ```
   git clone https://github.com/d-angelotorres/space-telemetry-visualizer.git
   cd space-telemetry-visualizer
   ```
2. Set up your Python virtual environment
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Run the app
   ```
   python run.py
   ```
5. Open your browser and visit http://127.0.0.1:5000

---

## 🧠 What I Learned

- How to consume and parse external JSON APIs in Python
- Basics of Flask routing and templating
- Graceful handling of missing/partial API data
- How to debug Jinja2 templates and data mismatches
- Importance of checking API maintenance status before building 🚨😅

---

## 📚 Next Steps

> This repo will remain as a completed archive, but I’ll be pivoting to another project with more current, real-time data.

Stay tuned! 👨🏽‍🚀

---

## 📄 License

This project is open source under the MIT License.
