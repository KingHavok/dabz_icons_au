dabz_icons_au

Overview

dabz_icons_au is a Python script designed to enhance the experience of DAB-Z users in Australia. This script allows users to automatically download and integrate station logos into the DAB-Z Player, a popular digital radio application for Android devices.

Prerequisites

Before using dabz_icons_au, ensure you have the following:
- The DAB-Z Player installed on your Android device. Download here
- Python installed on your PC.
- Required Python libraries: requests, BeautifulSoup, fuzzywuzzy. These can be installed via pip.

Getting Started
1. Scan Channels on DAB-Z: Use the DAB-Z app to scan and load all available digital radio channels.
2. Backup Channel Data: In the DAB-Z app, perform a backup to generate the dabservices.json file.
3. Transfer JSON File to PC: Move the dabservices.json file from your Android device to your PC.

Installation
1. Download the script https://github.com/KingHavok/dabz_icons_au/blob/main/stations.py
2. Install the required Python libraries: pip install requests beautifulsoup4 fuzzywuzzy python-Levenshtein

Usage
1. Modify the Script for Your Region (if necessary): If you are not in the Melbourne region, modify the script to point to the correct region on the Digital Radio Plus website. Change the URL in the script to match your region, for example, https://www.digitalradioplus.com.au/listen.aspx?region=Sydney.
2. Run the Script: Execute the dabz_icons_au script on your PC where you have placed the dabservices.json file.
   python stations.py
3. Script Execution: The script will process the dabservices.json file, download available station logos from Digital Radio Plus, and rename them appropriately.
4. Transfer Logos to Android Device: Move the renamed .png files to the /documents/DAB/Logos directory on your Android device.
5. Update Logos in DAB-Z: In the DAB-Z app, go to settings and run a logo scan to update the station logos.

Detailed Functionality
- Normalization: The normalize_label function standardizes station labels for consistency.
- Logo Downloading: download_logos fetches and saves station logos from Digital Radio Plus.
- JSON Processing: The script reads dabservices.json to match station names with downloaded logos.
- Fuzzy Matching: In cases where direct matching fails, the script uses fuzzy matching to find the closest logo name.

Dependencies
- requests: Used for making HTTP requests to download logos.
- BeautifulSoup: Parses HTML content for scraping logo URLs.
- json: Handles reading and parsing the dabservices.json file.
- shutil: Used for copying logo files to the desired directory.
- fuzzywuzzy: Implements fuzzy matching logic for logo names.

Error Handling
- If a station logo cannot be matched, the script prints "No suitable match found for [station name]". This indicates that either a logo is not available or the matching threshold is too high.

Customization
- Fuzzy Matching Threshold: Adjust the threshold in the if score > 85 line to change the sensitivity of the fuzzy matching. Note that even at 85% you'll get false positives so any lower and who know's what will happen.

Folder Structure
- Place dabservices.json in the same directory as the script.
- Logos will be saved in the logos directory created by the script.

Cleanup
- After running the script, you can safely delete the temp_logos folder if desired.

Limitations and Specific Handling
Availability of Logos
- Not All Logos Available: The Digital Radio Plus website may not have logos for every station, limiting the script's ability to download and match logos for some stations.
Accuracy of Matching
- Fuzzy Matching Limitations: Fuzzy matching is employed to improve the chances of finding the correct logo, but it is not 100% accurate. There may be instances where the script does not find a suitable match or incorrectly matches a station logo.
Handling of Specific Station Names
- 'Triple M' Naming Convention: The script contains specific handling for the 'Triple M' stations, which often use 'MMM' in their DAB broadcast names. The script accounts for this by substituting 'mmm' with 'triplem' during the matching process.

Contributing
- I'm not maintaining this, feel free to fork it and have at it!

License
- This project is licensed under the MIT License.

Acknowledgments
- DAB-Z Player: This script is designed to work in conjunction with the DAB-Z Player for Android. More info https://play.google.com/store/apps/details?id=com.zoulou.dab&hl=en&gl=US&pli=1
- Digital Radio Plus: Station logos are sourced from Digital Radio Plus. https://www.digitalradioplus.com.au/
