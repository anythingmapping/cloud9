from movingAssets import GeoRSS,CouncilTrucks
import feedparser
import urllib
import json
import time


#init the truck updating class
truck = CouncilTrucks()

#init the truck tracking class
geoRSS = GeoRSS('D37EEE129A664B46B5C0EC0C1CC8CC1D')

while True:
    geoRSS169 = geoRSS.track169()
    truck.nowX = float(geoRSS169['geo_long'])
    truck.nowY = float(geoRSS169['geo_lat'])
    #running the update
    truck.update()
    time.sleep(10)