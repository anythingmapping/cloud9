import json
import urllib

class FixedAssets():
    def __init__(self):
        self.fixedBinUrl = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/arcgis/rest/services/liveBins_wgs84/FeatureServer"
        self.numberOfAssets = 714 #713 is the numer of bins currently serviced
        
    def queryFixedAssetsXY(self):
        """ PNCC queryAGOL content """
        self.url = self.fixedBinUrl + '/0/query'
        
        self.payload = {"Where" : "1=1",
                        "f" : "json",
                        "returnCountOnly":"True"}
                        
        self.payloadEncoded = urllib.urlencode(self.payload)
        self.result = urllib.urlopen(self.url, self.payloadEncoded).read()
        self.queryReturn =  json.loads(self.result)
        print self.queryReturn
        
    def resetFixedAsset(self):
        self.url = self.fixedBinUrl + '/0/updateFeatures'
        self.updateList = []
        
        for i in range(self.numberOfAssets):
            self.feat = {"attributes" : {"OBJECTID" : i,"Done": "No"}}
            self.updateList.append(self.feat)
        
        #{"f": "json", "features": } is added to get a json return 
        self.payload = {"f": "json", "features": self.updateList}
        self.payloadEncoded = urllib.urlencode(self.payload)
        self.result = urllib.urlopen(self.url,self.payloadEncoded).read()
        self.queryReturn = json.loads(self.result)
        print self.queryReturn