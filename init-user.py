import requests
from requests.exceptions import ConnectionError
import time
import os

password = os.environ["MB_PASSWORD"]
email = os.environ["MB_EMAIL"]
token = os.environ["MB_SETUP_TOKEN"]
payload ={ 
    "database": None,
    "prefs": {
        "allow_tracking": "false",
        "site_locale": "en",
        "site_name": "onyxia"
    },
    "token": token,
    "user": {
        "email": email,
        "first_name": None,
        "last_name": None,
        "password": password,
        "password_confirm": password,
        "site_name": "onyxia"
    }
}
headers = {'content-type' : 'application/json'}
while True:
    try:
        r = requests.post("http://localhost:3000/api/setup", headers=headers, json=payload )
        if r.status_code == 200:
            print("Setup done!")
            break
    except ConnectionError as e:
        time.sleep(10)
        
