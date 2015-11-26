import json
import urllib

class FixedAssets():
    def __init__(self):
        self.fixedBinUrl = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/arcgis/rest/services/liveBins_wgs84/FeatureServer"
        self.numberOfAssets = 750 #713 is the numer of bins currently serviced
        
    def queryFixedAssetsXY(self):
        """ PNCC queryAGOL content """
        self.url = self.fixedBinUrl + '/0/query'
        
        #"outFields" : stops it from defaulting to random attributes
        self.payload = {"Where" : "1=1",
                        "f" : "json",
                        "returnGeometry":"True",
                        "outFields": "objectID"
                        }
                        
        self.payloadEncoded = urllib.urlencode(self.payload)
        self.result = urllib.urlopen(self.url, self.payloadEncoded).read()
        self.queryReturn =  json.loads(self.result)
        #return a list to iterate through
        #print self.queryReturn
        return self.queryReturn['features']
        
    
    def doneFixedAsset(self,closeOIDList):
        
        updateList = []
        try:
            #print closeOIDList[0]
            for f in closeOIDList:
                oidRef = f['attributes']['OBJECTID']
                feat = {"attributes" : {"OBJECTID" : oidRef,"Done": "Yes"}}
                updateList.append(feat)
            payload = {"f": "json", "features": updateList}    
            payloadEncoded = urllib.urlencode(payload)
            result = urllib.urlopen(self.fixedBinUrl + '/0/updateFeatures', payloadEncoded).read()
            queryReturn =  json.loads(result)
        except:
            print "nothing close by"
            pass
    
    def prepDay(self,dayInt):
        
        url = self.fixedBinUrl + '/0/query'
        days = ["Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"]
        
        #UPDATE DAYINT IF YOU WANT AN UPDATE FOR TODAYS DAY    
        payload = {"Where" : "{}Collect='Yes'".format(days[(int(dayInt))+1]),
                        "f" : "json", 
                        "returnIdsOnly":"True"
                        }

        payloadEncoded = urllib.urlencode(payload)
        result = urllib.urlopen(url, payloadEncoded).read()
        queryReturn =  json.loads(result)
        
        featList = queryReturn['objectIds']
        # print featList
        
       
        updateList = []
        
        for f in featList:
            #print f
            feat = {"attributes" : {"OBJECTID" : f,"CollectToday": "Yes"}}
            updateList.append(feat)
        # print len(updateList)
        # print len(featList)
        
        payload = {"f": "json", "features": updateList}    
        payloadEncoded = urllib.urlencode(payload)
        result = urllib.urlopen(self.fixedBinUrl + '/0/updateFeatures', payloadEncoded).read()
        queryReturn =  json.loads(result)
        
        #print queryReturn
        

    def resetFixedAsset(self):
        self.url = self.fixedBinUrl + '/0/updateFeatures'
        self.updateList = []
        
        for i in range(self.numberOfAssets):
            self.feat = {"attributes" : {"OBJECTID" : i,"Done": "No", "CollectToday": "No"}}
            self.updateList.append(self.feat)
        
        #{"f": "json", "features": } is added to get a json return 
        self.payload = {"f": "json", "features": self.updateList}
        self.payloadEncoded = urllib.urlencode(self.payload)
        self.result = urllib.urlopen(self.url,self.payloadEncoded).read()
        self.queryReturn = json.loads(self.result)
        #print self.queryReturn