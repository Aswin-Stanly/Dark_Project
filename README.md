Dark Web Domain Analyzer (DWDA):  A Python-based OSINT tool for checking the status of .onion domains on the dark web.

🔍 Overview
The Dark Web Domain Analyzer (DWDA) is a Python-based OSINT (Open-Source Intelligence) tool that allows users to check the availability of .onion domains on the Tor network.
It verifies whether a given .onion URL is active or inactive and provides real-time status updates with color-coded output for better readability.

✨ Features

✅ Checks if a .onion domain is active or inactive

✅ Color-coded status messages for readability

✅ Error handling for invalid inputs

✅ User-friendly interface with simple prompts

✅ Option to check multiple domains in one session


📌 Installation

1️⃣ Install Dependencies
Make sure you have Python 3.x installed. Then, install the required libraries:

pip install requests colorama

2️⃣ Install Tor & Set Up Proxy
Since .onion domains are only accessible via the Tor network, you must install and run the Tor service.
For Linux:

sudo apt update && sudo apt install tor -y

Start Tor:

sudo systemctl start tor
sudo systemctl enable tor
sudo systemctl status tor

In Kali Linux

sudo service tor start

Check status:

sudo service tor status

🚀 Usage
Run the script with:

python check_onion_status.py

Enter a .onion URL when prompted. The script will check its status and display:
🟢 Green → Active
🔴 Red → Inactive
🟡 Yellow → Warning/Error messages
🔵 Cyan → User prompts

💡 Example Output

Enter the .onion domain: example.onion
🟢 http://example.onion is Active and Reachable!
Do you want to check another site? (yes/no): yes
Enter the .onion domain: invalid.onion
🔴 http://invalid.onion is Inactive or Unreachable!


