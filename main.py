from serper_client import query_places,query_places_all
from exporter import create_append_rows
from config import OUTPUT_FILE_CENTRAL_SOURCE
from deduplicator import is_duplicate_row
from read_Locations import group_by_state
def run():
    queries = ["roof repair services","Roofing contractor"]
    resp = group_by_state()
    print("Response Read : ",resp)

    for queryTemp in queries:
        if resp is not None:
            for i, state in enumerate(resp):
                # print(f"{i}: {state} -> {len(resp[state])} cities")
                for o, city in enumerate(resp[state]):
                    query = queryTemp +" in "+city.strip()+", "+state.strip()
                    print(query)
                    all_businesses = query_places_all(query)
                    for j, business in enumerate(all_businesses):
                        print(f"Processing business {i+1}/{len(all_businesses)}: {business.get('title', 'Unknown')}")
                        create_append_rows(business, state)


                    # print(f"  {o}: {city}")  # city is already a string
        else:
            print("Failed to read CSV file")       
    # location = ""
    # filename = location.split(",")[0].strip().replace(" ", "_")

    
    # query = "roofing services"
    # all_businesses = query_places_all(query, location)
    # for i, business in enumerate(all_businesses):
    #     print(f"Processing business {i+1}/{len(all_businesses)}: {business.get('title', 'Unknown')}")
        
    #     create_append_rows(business, filename)

    # print(" ⚠️Location",filename)
    # print("Businesses found. ",all_businesses)
    
    # create_append_rows(all_businesses,"Testing")
    # for i, business in enumerate(all_businesses):
    #         print(f"Processing business {i+1}/{len(all_businesses)}: {business.get('title', 'Unknown')}")
            
if __name__ == "__main__":
    run()




    # row = {
    # "title": "Test Roofing",
    # "address": "123 Main St",
    # "phone": "(123) 456-7890",
    # "website": "https://testroofing.com",
    # "rating": 5.0,
    # "rating_count": 10,
    # "category": "Roofing contractor",
    # "latitude": 29.123,
    # "longitude": -95.456,
    # "cid": "1234567890"
    # }
    # append_row_to_csv(row)
    # if not is_duplicate_row(row):
    # else:
    #     print("Error Duplication")



    # location = response.get("searchParameters", {})
    # businesses = response.get("places", [])
    # fileName =location["location"].split(",")[0]
    # print(businesses)
    # create_append_rows(businesses,fileName)
