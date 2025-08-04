import requests
from config import SERPER_API_KEY,SERPER_BASE_URL as SERPER_BASE_URL
import time
from typing import List, Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://google.serper.dev/places"
MAX_PAGES = 30
NUM_PER_PAGE = 20
MAX_WORKERS = 10
BATCH_SIZE = 5


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
    all_places = []
    current_page = start_page

    def fetch_page(page):
        try:
            data = query_places(query, location=location, page=page)
            return page, data.get("places", []) or []
        except Exception as e:
            print(f"Error on page {page}: {e}")
            return page, []

    while current_page <= MAX_PAGES:
        batch_pages = list(range(current_page, min(current_page + BATCH_SIZE, MAX_PAGES + 1)))
        empty_page_found = False
        print(f"Fetching batch: {batch_pages}")

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(fetch_page, page): page for page in batch_pages}

            for future in as_completed(futures):
                page, places = future.result()
                print(f"Page {page} -> {len(places)} places")
                if not places:
                    empty_page_found = True
                else:
                    all_places.extend(places)

        if empty_page_found:
            print("Stopping: empty page encountered.")
            break

        current_page += BATCH_SIZE

    return all_places