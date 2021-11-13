# pip install playsound
import time
import requests
from playsound import playsound


url = 'https://learn.oracle.com/education/html/ols4/php/examProctorGetSlotsFetch.php?tz=GMT&id=&lp=91401&event=146401'
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
    "cookie": "s_fid=08F078FB19CB1C68-3DE7315EE9B1AFE5; s_cc=true; atgRecVisitorId=118C9n9J9ZAYv2gnhvHi2pP6SkkBkKywGS1z2WalL4uvMB4DA62; _abck=8D0FD0BE3ADFBD25FE42B5578D6923D7~0~YAAQJeVhXnQo+el8AQAAot81+QbObgqhZQ6OITiXBOFi7H4QA2nfMcfvx8EfjoOppMk/1tBz4W90MUFq6dPCEDKR3L9UotS7ATe1JbofEJ3p5UykKOmBHWbSiPj50suanHom/64a/xOHwxXA+zwJTE0zs26vBShsf9vkkK4PsKllFE1enOfPFcybG7kwbDQ8ReKYS0eNK1rW62VKdxD8Qaa42YJWOhpsMrRvOevI2z4oPsFuiQm4VmEXJlzvd0e1nS15PmQOdClpkiRK4RJ3XMbd0o9l4V9r3Is0dwoHCAzV8UAg5+VKdiqgxQE0nxpxftHCGIezRpAAo6gdZh8txTTXeGILOD01l166E/HOdI7pqSjIFDZ8okLFnI/x8FhW7uAn5RzlpOYoU23S2tltSnvuofPJLXum~-1~-1~-1; DLSession-35644=sessionId%3A26385103%2CofferingId%3A35644%2Cguid%3ACDEC67B2511D9E0EE050E60AD27F12A5; p_org_id=68; lang=US; ORA_WWW_MRKT=v:1~g:CDEC67B2511D9E0EE050E60AD27F12A5~t:NOT_FOUND~c:LP05; ORASSO_AUTH_HINT=v1.0~20211113112950; ORA_WWW_PERSONALIZE=v:1~i:NOT_FOUND~r:NOT_FOUND~g:EMEA~l:en~cs:NOT_FOUND~cn:NOT_FOUND; xdp1371820c1PRD_siteUS=118C9n9J9ZAYv2gnhvHi2pP6SkkBkKywGS1z2WalL4uvMB4DA62%3A1636265918413%3A1636277448693%3A1636781501483%3A3%3A3; Order_MarketingCampaignSuccess=owoufebOCICertTopBan; Order_MarketingTrigger=owoufebOCICertTopBan; p_mcc=NA:owoufebOCICertTopBan:owoufebOCICertTopBan; ORA_UCM_INFO=3~CDEC67B2511D9E0EE050E60AD27F12A5~Abdullah~Almanie~almanie5@hotmail.com; ak_bmsc=41D3D0D5C2F341F090EAF9893A7C06EE~000000000000000000000000000000~YAAQVOVhXtNWCul8AQAANs6jGA2nB2CXHhDSqgTeAIepRvOwbQoh4FqVlg2cBo4UeAhATtPWMxJSvdifW6YSnDrmxSRA47swpGnxIxfog9ZOLnnQgdj0u2zeFyDp/ezlODAgut5j0H9lodOaD/7uc7cUerf4JsIjUZ2DJofJmMv6b3vJtX0bHImKjRl+3DmIu9OgIkqK0V6GsLtZL3rGFd+jnkHQ7kjzS8qG+Xv0mqfYR5DnnhZiu+EyV2ZIhJjEPX7joktKe8q2TIRSbz6bqUX6jSLAx9k9fI0xgY6kD3iwtdudTDllyDd8Mxhv7FIA6tdDrZtPkdTsfLzAy7ykgCB121Z+c4W7l5ip7wnXzV02Jg2hV0wNaEL8ddOd1mLyQyYKNrXQYt7tffgF2hjX8eidqUQ/DFnlmflFnweANSMEnF8=; s_sq=%5B%5BB%5D%5D; OAMAuthnCookie_learn.oracle.com_443=74c81970c5011ed72f36aa9a5b36ec24550b29ad%7EyMjBbVldnGAqLKBo%2F3o758goUERDWEncXqSbuDeYMx1UWUKTLq0jvzWZGu8V%2FGs%2BzeRiWyHnxZ4O98%2Fls%2BQ2SBq4jXHcnfAwZKVS%2FAYUiEl9VDJGI7ZmZ1v3jtCSB%2BBKKLgucMyd7Nm0%2FIbt8Ql%2FAPVfiCWp9GIijRlbs%2BGqKkKt0ifTNe0%2BfWCP6sXodOyQv05XDKKZtSJAnXnC0n5paG40gHo%2BehBkQGYcGtjkogipAeORMODqSCzsvm7ovOTpcfhbcROQOJUoOV6DHHoOWQd0TmsGPWCML9RzS%2Fl%2FgQX0faQX6D%2B7mQQ5vNRpCpjfFYR1%2Bu48IfvY88Y0TCZaNVIAyDtX0SDwBTw6AXBD42RqBfGXfiqZ%2BTN0T7eMqh3LVJ0ZWmrWdDD7pHJ2FnnhrycPYtMQMWzsnYYZdySI4vOhnQU%2BbJDghFS%2Foee3X4SM55ZNJewTfY8Mbiqzvp6e%2F0yuJHfYwm7u9TluRxEd7Uwe2ibWak3tYlpu%2FSaPrrsOiII5eOr3ZyYhC8ybwU3uQb5OoWHWtr4NZHNDfr6CremQUtzy7v9%2BnxYMfejzhLC4; OAMAuthnHintCookie=1; ORA_UCM_INFO=3~CDEC67B2511D9E0EE050E60AD27F12A5~Abdullah~Almanie~almanie5@hotmail.com; PHPSESSID=ibs6stnn9fog2927qp48npmdp1; ora_ols=851381fda0700c6499ac18ddd236f437; dl_user=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJHZW5lcmF0aW5nIGEgdG9rZW4gZm9yIERMIiwibWFpbCI6ImFsbWFuaWU1QGhvdG1haWwuY29tIiwiZmlyc3ROYW1lIjoiQWJkdWxsYWgiLCJsYXN0TmFtZSI6IkFsbWFuaWUiLCJnZXRBdXRoIjp7ImlzTG9nZ2VkSW4iOiJ0cnVlIiwiaGFzQWNjZXNzIjoidHJ1ZSIsImFjY2Vzc3R5cGUiOiJDTFMiLCJpbGFPcmRlcklkIjoiMTU4Mzg2IiwiaGFzRUxTIjoiZmFsc2UiLCJlbHNHQ0MiOiJOT05FIiwiZWxzT3JkZXJJZHMiOiJOT05FIiwiaXNQcmVtaXVtIjoidHJ1ZSIsImFsbG93RWtpdERvd25sb2FkIjoiZmFsc2UiLCJvcmRlclR5cGUiOiInUkVHVUxBUiciLCJhY2Nlc3NMYWIiOiJ0cnVlIiwiYWNjZXNzRWtpdCI6InRydWUiLCJhY2Nlc3NBc2tJbnN0cnVjdG9yIjoidHJ1ZSIsImFjY2Vzc0NlcnRpZmljYXRpb24iOiJ0cnVlIiwiYWNjZXNzTGl2ZUV2ZW50cyI6InRydWUiLCJzZWNvbmRzQWxsb3dlZCI6MCwic2Vjb25kc1JlbWFpbmluZyI6MCwiZGF5c0R1cmF0aW9uIjowLCJkYXlzUmVtYWluaW5nIjowLCJpc1NhbGVzT3JnIjoiTiIsInNlc3Npb25JZCI6IjI2Mzg1MTAzIiwic2Vzc2lvbklkRnJvbSI6IlNlc3Npb24ifSwiZ3VpZCI6IkNERUM2N0IyNTExRDlFMEVFMDUwRTYwQUQyN0YxMkE1Iiwib2ZmZXJpbmdJZCI6IjM1NjQ0IiwiZXhwIjoxNjM2ODEzOTU1fQ.PYSlSfKg14UU5n1JKVUmRt_3KvcKKjg8-GVQNOnIfnk; gpw_e24=https%3A%2F%2Flearn.oracle.com%2Fols%2Fexam%2F35644%2F91401%2F146401; bm_sv=B343CF260A127BEF74AAECFABF6238A2~7/sELC/kM9LnT6FsZTDwAzG35wLiGwXNHtewhOi0vNKW77iuMVe66R43Ai+4h4C60z4m9g/cgLcnX9ppImkdrwq/E61foKBZC3kqylBpBpjqEXvupomQubOSBm5XmtSOSbDkS5a0t8ZpMkt4wC7OAqwwFlSKDujJv/zxpmYYT6M=; s_nr=1636796818553-Repeat; user_tz=Asia/Kuwait",
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

