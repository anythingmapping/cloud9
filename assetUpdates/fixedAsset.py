import json
import urllib

class fixedAssets():
    def __init__(self):
        self.fixedBinUrl = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/arcgis/rest/services/liveBins_wgs84/FeatureServer"
        self.currentDay = "Monday"
       
    def queryfixedAssets(self):
        """ PNCC queryAGOL content """
        self.url = self.fixedBinUrl + '/0/query'
        
        self.payload = {"Where" : "1=1",
                        "outFields": "truckNumber",
                        "f" : "json",
                        "returnGeometry":"True"}
                        
        self.payloadEncoded = urllib.urlencode(self.payload)
        self.result = urllib.urlopen(self.url, self.payloadEncoded).read()
        self.queryReturn =  json.loads(self.result)
        print self.queryReturn