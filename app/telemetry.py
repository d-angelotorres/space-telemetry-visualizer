import requests

def get_latest_launch():
    url = "https://api.spacexdata.com/v5/launches/latest"  # Updated to v5
    response = requests.get(url)
    
    print(f"API Response Status Code: {response.status_code}")
    print(f"API Response: {response.text}")  # Check the new response format

    if response.status_code == 200:
        data = response.json()
        print(f"Parsed JSON Data: {data}")  # See the exact data structure
        return {
            "name": data.get("name"),
            "date_utc": data.get("date_utc"),
            "details": data.get("details"),
            "links": data.get("links", {}),
        }
    else:
        return {"error": "Failed to fetch telemetry"}



