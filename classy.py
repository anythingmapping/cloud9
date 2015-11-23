import feedparser
import urllib
import json
import time


class CouncilAGOL():
    def __init__(self):
        self.fixedBinUrl = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/arcgis/rest/services/liveBins_wgs84/FeatureServer"
        self.truckUrl = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/truckGeoRSS/FeatureServer"
        self.currentDay = "Monday"
       
    def queryAGOL(self):
        """ PNCC queryAGOL content """
        self.url = self.truckUrl + '/0/query'
        
        self.payload = {"Where" : "1=1",
                        "outFields": "truckNumber",
                        "f" : "json",
                        "returnGeometry":"True"}
                        
        self.payloadEncoded = urllib.urlencode(self.payload)
        self.result = urllib.urlopen(self.url, self.payloadEncoded).read()
        self.queryReturn =  json.loads(self.result)
        print self.queryReturn

    def upTruckPos(self):
        """PNCC update AGOL streetbin collection features, requires a payload in dict format"""
        
        self.url = self.truckUrl + '/0/updateFeatures'
        print self.url
        
        #self{"attributes" : {"OBJECTID" : 1,"Done": "Yes","collectToday" : "Yes"}
        #payload = {"f": "json", "features": feat}
        #url = targetFeatureURL + "/0/updateFeatures"
        #url = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/ProcessManager_WFL/FeatureServer/0/updateFeatures" #thetemplate
        #result = urllib.urlopen(url, urllib.urlencode(payload)).read()
        #print json.loads(result)
        #"f" : "json" or "html" ### defines the return format, we go for JSON
        #payload = {"Where" : "Thursday='Yes'", "outFields": "objectID", "f" : "json", "returnGeometry":"True"}
        #enco = urllib.urlencode(payload)
        #opening = urllib.urlopen(self.url).read()
        #print opening
        
        #self.feat={"attributes" : {"OBJECTID" : 1,"truckNumber": 1}}
        #self.payload = {"f": "json", "features": 1}
        #self.payload = {"attributes" : {"OBJECTID" :1,"truckNumber": 1}}
        #self.url = self.url + "/0/updateFeatures"
        
        ##### these are just for debuging #####
        #self.result = urllib.urlopen(self.url, urllib.urlencode(self.payload)).read()
        #print json.loads(self.result)
 
a = CouncilAGOL()
#a.queryAGOL()  
a.upTruckPos()
    
    




class GeoRSS():
    def __init__(self,authentication):
        self.authentication = authentication
    
    def track169(self):
        self.feed = feedparser.parse('https://ws.smartrak.co.nz/EventAccess/CurrentPositionGeoRss.aspx?key=7405E8AA4A2D4016B61531E9D3C2EED4')
        self.remoteId = 7771
        for i in range(len(self.feed['entries'])):
            if int(self.feed['entries'][i]['st_remoteid']) == self.remoteId:
                return self.feed['entries'][i]
            else:
                pass
        print "well done"


        
#geoRSS = GeoRSS('D37EEE129A664B46B5C0EC0C1CC8CC1D')
#a = geoRSS.track169()




from suds.client import Client

def clipDecorate(func):
    def func_wrapper(*args, **kwargs):
        return "Test {0} + a thing".format(func(*args, **kwargs))
    return func_wrapper
    
class SmartrakExtract:
    def __init__(self,authentication):
        self.authentication = authentication
        self.url = "https://ws.smartrak.co.nz/Reporting/ReportingSoap.asmx?WSDL"
    
    @clipDecorate
    def reportTrucks(self):
        """ method to report on the total trucks with remote IDs """
        self.client = Client(self.url)
        return self.client.service.GetRemotes(self.authentication)

    def reportLocations(self,remote,date,eventCodes):
        """ report on a trucks activity for a day, pass remoteID, date, and None """
        self.client = Client(self.url)
        return self.client.service.GetHistoryForDay(self.authentication,remote,date,eventCodes)

#if __name__ == '__main__':
#    app = SmartrakExtract('D37EEE129A664B46B5C0EC0C1CC8CC1D')
#    a = app.reportTrucks()
#    print a 
    
