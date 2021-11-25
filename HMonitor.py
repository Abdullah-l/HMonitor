# pip install playsound
import time
import requests
from playsound import playsound


url = 'https://example.com'
headers = {"accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "Referer": "https://learn.oracle.com/ols/exam/35644/91401/146401",
    "cookie": "",
    "Referrer-Policy": "strict-origin-when-cross-origin"
    }

cmprTo = []

while (True):
    r = requests.get(url, headers=headers, params={'tz': 'Asia/Kuwait'})

    i = 0
    av = r.json()['availableSlots']

    topTen = []

    while (i < 10):
        topTen.append(av[i])
        i = i + 1
    
    if (cmprTo == []):
        cmprTo = topTen

    if (topTen != cmprTo):
        print(topTen)
        playsound('gilfoyle_alert.mp3')
        cmprTo = topTen
    else:
        print('Unchanged \t ' + str(time.strftime('%I:%M:%S %p')))

    time.sleep(20)

