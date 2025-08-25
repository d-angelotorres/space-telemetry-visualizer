# 🚀 Space Telemetry Visualizer

A Flask web app that fetches and displays data from the most recent **SpaceX launch**, including launch name, date, details, AI-generated summaries, and external links to Wikipedia and webcast streams.

> ⚠️ The SpaceX API (v5) appears to no longer be actively maintained. Latest live data may be from **2022**. However, the app demonstrates API integration, AI summarization, Flask development, Docker containerization, and CI/CD workflows.

---

## 🛰️ Features

- Fetches most recent launch data from the SpaceX API
- Displays launch name, UTC date, and launch details
- Generates **AI-powered summary** of launch details using Hugging Face transformers
- Shows links to Wikipedia and webcast (if available)
- Handles missing or outdated data gracefully with fallback defaults
- Styled with simple, responsive HTML + CSS
- **Dockerized** for consistent environment and container deployment
- CI/CD pipeline configured using **GitHub Actions** to automatically build, test, and validate the app on each push

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, Jinja2 templates, CSS
- **AI / NLP**: Hugging Face transformers (`distilbart-cnn-12-6`) for summarization
- **Containerization**: Docker
- **CI/CD**: GitHub Actions (automated build, test, lint pipeline)
- **API**: SpaceX REST API (v5)

---

## 🚧 Known Limitations

- SpaceX API data may be outdated (latest launch info from 2022)
- Fallback data is used to generate AI summaries when API data is missing
- Flask’s built-in server is used for local testing; production WSGI servers recommended for full-scale deployment

---

## 📦 Getting Started (Local Development)

1. **Clone this repository**

   ```bash
   git clone https://github.com/d-angelotorres/space-telemetry-visualizer.git
   cd space-telemetry-visualizer
   ```

2. Set up your Python virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app

   ```bash
   python run.py
   ```

5. Open your browser and visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📦 Getting Started (Docker)

1. Build the Docker image:

   ```bash
   docker build -t spacex-telemetry-dashboard .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 5050:5000 spacex-telemetry-dashboard
   ```

3. Open your browser and visit [http://localhost:5050](http://localhost:5050)

> Changes in code require rebuilding the Docker image.

---

## 🧠 Agile / DevOps Practices Demonstrated

- Implemented **version control** using Git and GitHub
- Designed **CI/CD workflow** via GitHub Actions (automated build and test)
- Containerized the application with **Docker** for reproducible environments
- Followed **modular Python structure** for maintainability
- Handled missing API data and errors gracefully → demonstrates robust, production-like engineering practices

---

## 🧠 What I Learned

- Consuming and parsing external JSON APIs in Python
- Flask routing, Jinja2 templating, and dynamic web page rendering
- Integrating AI/NLP pipelines locally with Hugging Face transformers
- Docker containerization and how it ensures consistent environments
- Configuring GitHub Actions CI/CD for automated builds and testing
- Designing applications to gracefully handle missing or outdated external data

---

## 📄 License

This project is open source under the MIT License.
