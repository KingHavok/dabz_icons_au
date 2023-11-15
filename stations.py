import requests
from bs4 import BeautifulSoup
import os
import json
import shutil
from fuzzywuzzy import process

def normalize_label(label):
    return ''.join(e for e in label if e.isalnum()).lower()

def download_logos(url, download_folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for station_item in soup.find_all('li', class_='stations-list-item'):
        logo_url = station_item.find('div', class_='station-logo').img['src']
        station_name = station_item.find('h3', class_='station-name').text.strip()
        logo_full_url = f"https://www.digitalradioplus.com.au{logo_url}"

        response = requests.get(logo_full_url)
        if response.status_code == 200:
            filename = f"{normalize_label(station_name)}.png"
            with open(os.path.join(download_folder, filename), 'wb') as file:
                file.write(response.content)

# URL and folders setup
url = "https://www.digitalradioplus.com.au/listen.aspx?region=Melbourne"
temp_download_dir = 'temp_logos'
logos_dir = 'logos'

os.makedirs(temp_download_dir, exist_ok=True)
os.makedirs(logos_dir, exist_ok=True)

# Download logos to the temporary folder
download_logos(url, temp_download_dir)

# Read JSON and prepare for matching
json_file = 'dabservices.json'
if not os.path.exists(json_file):
    print("dabservices.json not found in the current directory.")
    exit()

with open(json_file, 'r') as file:
    data = json.load(file)


for station in data:
    normalized_label = normalize_label(station['serviceLabel'])
    # Substitute 'mmm' with 'triplem' for matching if it starts with 'MMM'
    search_label = normalized_label.replace('mmm', 'triplem') if normalized_label.startswith('mmm') else normalized_label
    direct_match_found = False

    for filename in os.listdir(temp_download_dir):
        if filename.startswith(search_label):
            shutil.copyfile(os.path.join(temp_download_dir, filename), os.path.join(logos_dir, normalized_label + '.png'))
            direct_match_found = True
            break

    if not direct_match_found:
        # Fuzzy matching
        all_filenames = [normalize_label(filename) for filename in os.listdir(temp_download_dir) if filename.endswith('.png')]
        best_match, score = process.extractOne(search_label, all_filenames)
        if score > 85:  # Adjust the threshold as needed
            actual_filename = [filename for filename in os.listdir(temp_download_dir) if normalize_label(filename) == best_match][0]
            shutil.copyfile(os.path.join(temp_download_dir, actual_filename), os.path.join(logos_dir, normalized_label + '.png'))
        else:
            print(f"No suitable match found for {station['serviceLabel']}")

print("Copying complete.")
