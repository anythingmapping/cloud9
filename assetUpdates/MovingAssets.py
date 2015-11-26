import feedparser
import urllib
import json
import time

class CouncilTrucks():
    """ Council truck asset"""
    def __init__(self):
        self.truckUrl = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/truckGeoRSS/FeatureServer"
        self.url = self.truckUrl + "/0/updateFeatures"
        
        self.x = 0
        self.y = 0
        self.nowX = 175.56
        self.nowY = -39.43
        
        self.collections = 0
        self.fuel = 100
        
    def update(self):
        """formats the payload for json"""
        
        #{"f": "json", "features": } is added to get a json return 
        self.payload = {"f": "json", "features":{
                            "geometry" : {
                                "x" : self.nowX,
                                "y" : self.nowY}, 
                            "attributes" : {
                                "OBJECTID": 1,
                                "truckNumber": 169}
                            }
                        }
        self.payloadEncoded = urllib.urlencode(self.payload)
        self.result = urllib.urlopen(self.url,self.payloadEncoded).read()
        self.queryReturn = json.loads(self.result)
        #print self.queryReturn

class GeoRSS():
    def __init__(self,authentication):
        self.authentication = authentication
    
    
    def track169(self):
        self.feed = feedparser.parse('https://ws.smartrak.co.nz/EventAccess/CurrentPositionGeoRss.aspx?key=7405E8AA4A2D4016B61531E9D3C2EED4')
        self.remoteId = 7771
        for i in range(len(self.feed['entries'])):
            if int(self.feed['entries'][i]['st_remoteid']) == self.remoteId:
                print self.feed['entries'][i]
                return self.feed['entries'][i]
                
            else:
                pass
        #print "not found in the feed"