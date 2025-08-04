import pandas as pd
import csv

def group_by_state():
    file_path="./Locations.csv"
    try:
        # Read CSV using pandas
        df = pd.read_csv(file_path)
        
        # Get first two columns
        cities = df.iloc[:, 0].tolist()
        states = df.iloc[:, 1].tolist()
        
        # Group cities by state
        grouped = {}
        for city, state in zip(cities, states):
            if state not in grouped:
                grouped[state] = []
            grouped[state].append(city)
        
        return grouped
        
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

# Alternative using csv module (no pandas required)
def group_by_state_csv(file_path):
    try:
        grouped = {}
        
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            
            for row in reader:
                if len(row) >= 2:
                    city = row[0].strip()
                    state = row[1].strip()
                    
                    if state not in grouped:
                        grouped[state] = []
                    grouped[state].append(city)
        
        return grouped
        
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None