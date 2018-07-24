import redis
import json
import urllib.request as urllib
import datetime
from calendar import timegm
import time
import os
import sys
import ssl

REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
r = redis.StrictRedis.from_url(REDIS_URL)

# NASA's station FDO updates this page with very precise data. Only using a
# small bit of it for now.
# url = "http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html"

# Clestrak provides TLE data for the space station:
url = "https://www.celestrak.com/NORAD/elements/stations.txt"


def update_tle():
    # Open a http request
    req = urllib.Request(url)
    context = ssl._create_unverified_context()
    response = urllib.urlopen(req, context=context)
    data = str(response.read())

    # parse the HTML
    data = data.split("\\r\\n")
    line1 = line2 = line3 = ""
    for index, line in enumerate(data):
        if "ISS (ZARYA)" in line:
            line1 = data[index][2:]
            line2 = data[index + 1]
            line3 = data[index + 2]
            break
    
    if line1 == "":
        raise Exception("Could not find ISS data")

    tle = json.dumps([line1.strip(), line2.strip(), line3.strip()])
    r.set("iss_tle", tle)


if __name__ == '__main__':
    print("Updating ISS TLE from JSC...")
    try:
        update_tle()
    except:
        exctype, value = sys.exc_info()[:2]
        print("Error:"), exctype, value
