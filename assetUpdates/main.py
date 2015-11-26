import feedparser
import urllib
import json
import time
import sys

from MovingAssets import GeoRSS,CouncilTrucks
from FixedAsset import FixedAssets


def main():

    #termination conditions
    count = 0
    done  = False
    
    while not done:
        #incriment so it doesnt run forever
        print "This is the {} iteration update for today".format(count+1)
        count += 1
        
        #FOR DEBUG OVERWRITE HOUR
        hourOfDay = time.strftime("%H")
        hourOfDay = 19
        
        
        
        ################################################
        ############ TIME CHECK SECTION ################
        ############ RESET AND TERMINATE ###############
        ################################################
        #if its past 8 o'clock reset everything
        if int(hourOfDay)>=20:
            print "Time is {}:00 we are refreshing services".format(hourOfDay)
            reset = FixedAssets()
            reset.resetFixedAsset()
            print "Refreshing all {0} features to not done".format(reset.numberOfAssets)
            
            dayInt = time.strftime("%w")
            print "Setting the next day using {0} value".format(dayInt)
            reset.prepDay(dayInt)
            
            # KILL PROCESS FOR THE DAY
            done = True
        
        ################################################
        ############ UPDATE TRUCK LOCATION #############
        ################################################
        truck = CouncilTrucks()
        geoRSS = GeoRSS('D37EEE129A664B46B5C0EC0C1CC8CC1D')
        
        if not done:
            geoRSS169 = geoRSS.track169()
            truck.nowX = float(geoRSS169['geo_long'])
            truck.nowY = float(geoRSS169['geo_lat'])
            
            #UPDATE TRUCK LOCATION
            truck.update()

            #FIND BIN LOCATION
            binStatus = FixedAssets()
            binXY = binStatus.queryFixedAssetsXY()
            print len(binXY['features'])
            
            #Calculations
            
            #update bins if close
            #update truck count

        ################################################
        ############ CLOCK.TICK ########################
        ################################################
        #time.sleep(10)
        
        if count ==1:
            done = True

if __name__ == "__main__":
    main()