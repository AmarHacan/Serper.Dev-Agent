import requests
from config import SERPER_API_KEY,SERPER_BASE_URL as SERPER_BASE_URL
import time
from typing import List, Dict, Any

BASE_URL = "https://google.serper.dev/places"

def query_places(query, location=None, num=10, page=1):
    """
    Fetch one page of places results.
    """
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": query, "num": num, "page": page}
    if location:
        payload["location"] = location

    resp = requests.post(BASE_URL, json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()  # dict with "places", "searchParameters", "credits"

def query_places_all(query, location=None, start_page=1) -> List[Dict[str, Any]]:
    """
    Fetch multiple pages and return a flat list of place dicts.
    Stops when a page returns no places or after max_pages.
    """
    num=50
    all_places = []
    page = start_page
    condition = True
    while condition:
        data = query_places(query, location=location, num=num, page=page)
        places = data.get("places", []) or []
        print("Current Page : ",page)
        if not places:
            print("Break : ",page)
            break
        all_places.extend(places)
        page += 1
    return all_places
