import csv

def load_requests(csv_path):
    """
    Loads requests from a CSV file and formats them into a list of dictionaries.
    Each dictionary contains 'system_prompt' and 'prompt' keys.
    """
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader] 