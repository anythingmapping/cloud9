import feedparser
import urllib
import json
import time



from MovingAssets import GeoRSS,CouncilTrucks
from FixedAsset import FixedAssets


############ TIME CHECK SECTION ################
#date = time.strftime("%Y-%m-%d")
#print date
time = time.strftime("%H")
#day = time.strftime("%A")


if int(time)<5 and int(time) >2: #times will need updating
    print "refreshing all features"
    whiteWash = FixedAssets()
    #whiteWash.resetFixedAsset()
    whiteWash.queryFixedAssetsXY()
    
    #set collection day

"""
############ MAIN APPLICATION LOOP #################

#init the truck updating class
truck = CouncilTrucks()
#init the truck tracking class
geoRSS = GeoRSS('D37EEE129A664B46B5C0EC0C1CC8CC1D')
collectionTime = True

if collectionTime:
    geoRSS169 = geoRSS.track169()
    truck.nowX = float(geoRSS169['geo_long'])
    truck.nowY = float(geoRSS169['geo_lat'])
    #running the update
    truck.update()
    time.sleep(10)
    
else:
    pass
"""