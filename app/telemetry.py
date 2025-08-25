import requests
from transformers import pipeline

# Initialize Hugging Face summarization pipeline (runs locally)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Fallback dummy launch details
DUMMY_DETAILS = """
The Crew-5 mission to the International Space Station successfully launched 
on October 5, 2022. The mission included four astronauts and one cosmonaut. 
The Falcon 9 rocket delivered supplies and science experiments to the ISS.
"""

def summarize_telemetry(details_text):
    # Ensure details_text is always a string
    if not details_text or details_text.strip() == "":
        details_text = DUMMY_DETAILS
    try:
        summary = summarizer(details_text, max_length=50, min_length=25, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"AI summarization error: {e}")
        return "Summary unavailable due to AI error."

def get_latest_launch():
    url = "https://api.spacexdata.com/v5/launches/latest"
    response = requests.get(url)
    
    print(f"API Response Status Code: {response.status_code}")
    print(f"API Response: {response.text}")  # Check the response format

    if response.status_code == 200:
        data = response.json()
        print(f"Parsed JSON Data: {data}")

        details_text = data.get("details")
        launch_summary = summarize_telemetry(details_text) 


        return {
            "name": data.get("name") or "Crew-5 Mission",  # Fallback name
            "date_utc": data.get("date_utc") or "2022-10-05T16:00:00.000Z",  # Fallback date
            "details": data.get("details") or DUMMY_DETAILS,
            "summary": launch_summary,
            "links": data.get("links") or {"wikipedia": "https://en.wikipedia.org/wiki/Crew-5", "webcast": "#"},
        }
    else:
        # If API fails entirely, return dummy launch
        return {
            "name": "Crew-5 Mission",
            "date_utc": "2022-10-05T16:00:00.000Z",
            "details": DUMMY_DETAILS,
            "summary": summarize_telemetry(DUMMY_DETAILS),
            "links": {"wikipedia": "https://en.wikipedia.org/wiki/Crew-5", "webcast": "#"},
        }
