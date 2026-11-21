import os
import urllib.request
import urllib.error

PLACE_ID = "101944918133348"
API_KEY = os.environ["ROBLOX_API_KEY"]

URL = (
    "https://apis.roblox.com/legacy-develop/v1/places/"
    f"{PLACE_ID}/teamcreate/active_session/members?limit=10"
)

request = urllib.request.Request(
    URL,
    headers={
        "x-api-key": API_KEY,
        "accept": "application/json"
    }
)

try:
    with urllib.request.urlopen(request, timeout=20) as response:
        print("HTTP STATUS:", response.status)
        print(response.read().decode("utf-8"))

except urllib.error.HTTPError as error:
    print("HTTP STATUS:", error.code)
    print(error.read().decode("utf-8")[:1000])
