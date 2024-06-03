# IP Address Updater for Google Sheets

This Python script updates a Google Sheets document with your current public IP address every 60 seconds. It uses the ipify API to get the public IP address and the gspread library to interact with Google Sheets.
## Prerequisites

- Python 3.x
- Required Python packages:
    - requests
    - gspread
    - oauth2client

## Setup

1. Clone the Repository:

    ```sh
    git clone https://github.com/basit3000/IP-address-updater-for-dynamic-IP.git
    cd IP-address-updater-for-dynamic-IP
    ```

2. Install the Required Packages:
    You can install the required packages using pip:

    ```sh
    pip install requests gspread oauth2client
    ```

3. Google Sheets API Setup:

    - Create a project in the Google Developers Console.
    - Enable the Google Sheets API and Google Drive API.
    - Create credentials for a service account and download the JSON key file. Rename this file to IPaddress.json or update the script with your file's name.

4. Prepare Your Google Sheet:

    - Create a new Google Sheet.
    - Share the sheet with the email address from your service account (found in the JSON key file).

5. Update the Script:

    Update the script with the name of your Google Sheet in the line:

    ```python

        sheet = client.open('minecraft IP').sheet1

        #Replace 'minecraft IP' with the name of your Google Sheet.
    ```
## Running the Script

To run the script, simply execute:


```sh
python ip_updater.py
```

The script will:

1. Retrieve your public IP address from ipify.
2. Update the first cell (A1) of your specified Google Sheet with the current IP address.
3. Repeat the process every 60 seconds.


## Notes

- Ensure that your internet connection is active for the script to fetch the IP address and update the Google Sheet.
- If the internet connection is down, the script will print "Internet is down currently."

## License

This project is licensed under the MIT License.

Feel free to contribute and make improvements to this script. If you encounter any issues, please open an issue on the GitHub repository.