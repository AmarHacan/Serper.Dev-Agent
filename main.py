from serper_client import query_places,query_places_all
from exporter import create_append_rows
from config import OUTPUT_FILE_CENTRAL_SOURCE
from deduplicator import is_duplicate_row
from read_Locations import group_by_state
from urllib.parse import urlparse

def run():
    queries = ["roof repair services","Roofing contractor"]
    resp = group_by_state()
    # print("Response Read : ",resp)

    for queryTemp in queries:
        if resp is not None:
            for i, state in enumerate(resp):
                # print(f"{i}: {state} -> {len(resp[state])} cities")
                for o, city in enumerate(resp[state]):
                    query = queryTemp +" in "+city.strip()+", "+state.strip()
                    print(query)
                    all_businesses = query_places_all(query)
                    for j, business in enumerate(all_businesses):
                        # print(f"Processing business {i+1}/{len(all_businesses)}: {business.get('title', 'Unknown')}")
                        raw_website = business.get("website", "")
                        if raw_website:
                            normalized = normalize_website(raw_website)
                        else:
                            normalized = ""
                        business["normalized_website"] = normalized
                        create_append_rows(business, state)
                    # print(f"  {o}: {city}")  # city is already a string
        else:
            print("Failed to read CSV file")       

def normalize_website(raw_url):
    if not raw_url:
        return ""
    raw_url = raw_url.lower().replace("https://", "").replace("http://", "").replace("www.", "").strip()
    parsed = urlparse("http://" + raw_url)  # ensure it parses correctly
    domain = parsed.netloc or parsed.path.split('/')[0]
    return domain.rstrip("/")

    
if __name__ == "__main__":
    run()