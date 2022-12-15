import requests
from requests.exceptions import ConnectionError
import time

while True:
    try:
        r = requests.get("http://localhost:3000")
        if r.status_code == 200:
            break
    except ConnectionError as e:
        print(e)
        time.sleep(5)
        
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
r = requests.post("http://localhost:3000/api/setup", headers=headers, json=payload )
print(r)
