import requests
from requests.exceptions import ConnectionError
import time
payload ={ 
    "database": None,
    "prefs": {
        "allow_tracking": "false",
        "site_locale": "en",
        "site_name": "onyxia"
    },
    "token": "metabase",
    "user": {
        "email": "toto@toto.toto",
        "first_name": None,
        "last_name": None,
        "password": "totototo1",
        "password_confirm": "totototo1",
        "site_name": "onyxia"
    }
}
headers = {'content-type' : 'application/json'}
while True:
    try:
        r = requests.post("http://localhost:3000/api/setup", headers=headers, json=payload )
        if r.status_code == 200:
            print("setup done!")
            break
    except ConnectionError as e:
        time.sleep(10)
        
