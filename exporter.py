import os
import pandas as pd
from config import OUTPUT_FILE_CENTRAL_SOURCE,OUTPUT_FILE_States_SOURCE
# Define your fixed schema (column order) once
FIXED_COLUMNS = [
    "title", "address", "phoneNumber", "website",
    "rating", "ratingCount", "category",
    "latitude", "longitude", "cid"
]

def create_append_rows(row: dict, filename: str = "CentralSource.csv"):
    """
    Create-or-append one row to CSV under OUTPUT_FILE_CENTRAL_SOURCE,
    enforcing a fixed schema and column order.
    """
    if not isinstance(row, dict):
        print("❌ Provided row is not a dictionary.")
        return
    full_path = ""
    if filename=="CentralSource.csv":
        os.makedirs(OUTPUT_FILE_CENTRAL_SOURCE, exist_ok=True)      
        full_path = os.path.join(OUTPUT_FILE_CENTRAL_SOURCE, filename)
    else:
        os.makedirs(OUTPUT_FILE_States_SOURCE, exist_ok=True)
        full_path = os.path.join(OUTPUT_FILE_States_SOURCE, filename+".csv")

    # Normalize row to fixed schema: drop extras, fill missing
    normalized = {col: row.get(col, "") for col in FIXED_COLUMNS}

    # If file doesn't exist, create with header
    if not os.path.isfile(full_path):
        pd.DataFrame([normalized], columns=FIXED_COLUMNS).to_csv(full_path, index=False)
        print(f"🆕 Created file and wrote 1 row to {full_path}")
        return

    # Append without header, fixed column order
    pd.DataFrame([normalized], columns=FIXED_COLUMNS).to_csv(
        full_path, mode="a", header=False, index=False
    )
    print(f"✅ Appended row to {full_path}")
