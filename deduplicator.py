import pandas as pd
import os
from config import OUTPUT_FILE_CENTRAL_SOURCE

def is_duplicate_row(new_row: dict) -> bool:
    """
    Checks if a row with the same 'cid' or ('website' + 'phoneNumber') already exists.
    """
    if not os.path.isfile(OUTPUT_FILE_CENTRAL_SOURCE):
        return False  # File doesn't exist yet — nothing to compare

    df = pd.read_csv(OUTPUT_FILE_CENTRAL_SOURCE)

    # First, check by unique 'cid'
    if 'cid' in new_row and not pd.isna(new_row['cid']):
        if (df['cid'].astype(str) == str(new_row['cid'])).any():
            return True

    # Fallback to website + phone if cid is missing
    website = new_row.get('website', '').strip().lower()
    phone = new_row.get('phoneNumber', '').strip()

    if website and phone:
        is_duplicate = (
            (df['website'].fillna('').str.strip().str.lower() == website) &
            (df['phoneNumber'].fillna('').str.strip() == phone)
        ).any()
        return is_duplicate

    return False
