dabz_icons_au

Overview
dabz_icons_au is a Python script designed to enhance the experience of DAB-Z users in Australia. This script allows users to automatically download and integrate station logos into the DAB-Z Player, a popular digital radio application for Android devices.

Prerequisites
Before using dabz_icons_au, ensure you have the following:
1. The DAB-Z Player installed on your Android device. (https://play.google.com/store/apps/details?id=com.zoulou.dab&hl=en&gl=US&pli=1)
2. Python installed on your PC.
   Required Python libraries: requests, BeautifulSoup, fuzzywuzzy. These can be installed via pip.

Getting Started
1. Scan Channels on DAB-Z: Use the DAB-Z app to scan and load all available digital radio channels.
2. Backup Channel Data: In the DAB-Z app, perform a backup to generate the dabservices.json file.
3. Transfer JSON File to PC: Move the dabservices.json file from your Android device to your PC.

Installation
1. Clone the Repository:
    git clone [URL of your GitHub repo]
2. Install the required Python libraries:
    pip install requests beautifulsoup4 fuzzywuzzy python-Levenshtein

Usage
1. Modify the Script for Your Region (if necessary): If you are not in the Melbourne region, modify the script to point to the correct region on the Digital Radio Plus website. Change the URL in the script to match your region, for example, https://www.digitalradioplus.com.au/listen.aspx?region=Sydney.
2. Run the Script: Execute the dabz_icons_au script on your PC where you have placed the dabservices.json file.
    python dabz_icons_au.py
3. Script Execution: The script will process the dabservices.json file, download available station logos from Digital Radio Plus, and rename them appropriately.
4. Transfer Logos to Android Device: Move the renamed .png files to the /documents/DAB/Logos directory on your Android device.
5. Update Logos in DAB-Z: In the DAB-Z app, go to settings and run a logo scan to update the station logos.

Contributing
I'm not maintainign this, feel free to fork it and have at it!

License
This project is licensed under the MIT License.

Acknowledgments
1. DAB-Z Player: This script is designed to work in conjunction with the DAB-Z Player for Android. https://play.google.com/store/apps/details?id=com.zoulou.dab&hl=en&gl=US&pli=1
2. Digital Radio Plus: Station logos are sourced from Digital Radio Plus. https://www.digitalradioplus.com.au
