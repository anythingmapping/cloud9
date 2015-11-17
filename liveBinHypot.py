import urllib
import json
from suds.client import Client
import math
import time

targetFeatureURL = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/arcgis/rest/services/liveBins_wgs84/FeatureServer"


def grabEvents():
    """ function to grab current smartrak location using. requires suds.client as Client """
    url="https://ws.smartrak.co.nz/Reporting/ReportingSoap.asmx?WSDL"
    client = Client(url)

    ####### HARD CODED VALUES ############
    authentication = "D37EEE129A664B46B5C0EC0C1CC8CC1D"
    binTruck169 = 7771
    remoteId = 7771
    
    ####### PASS TODAYS DATE ########
    #date = "2015-11-16" #This does not seem to take a UTC time value
    date = time.strftime("%Y-%m-%d")
    print date
    eventCodes = None

    ####### GET DATA ############
    result = client.service.GetHistoryForDay(authentication, remoteId, date, eventCodes)

    ####### PROCESS DATA ##########
    #convert the results into a list so I can index down to the lat longs
    data = list(result)
    #index out the last element using slice
    #data[0] gets rid of the first Historical Event Tuple('Historical event',[everything else])
    #data[0][1] gets rid of second Historical Event Tuple('Historical event',[everything else])
    #data[0][1][-1:] get most recent
    lstVY = data[0][1][-1:][0]['Latitude']
    lstVX = data[0][1][-1:][0]['Longitude']
    lstV = (lstVX,lstVY)
    return lstV

def queryAGOL():
    """ PNCC queryAGOL content """
    #url = 'http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/ProcessManager_WFL/FeatureServer/0'
    currentDay = "Sunday" + "Collect"
    #targetFeatureURL = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/LiveCollectionData_WFL/FeatureServer"
    # TARGET URL MOVED TO MAIN AREA
    #targetFeatureURL = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/arcgis/rest/services/liveBins_wgs84/FeatureServer"
    url = targetFeatureURL + '/0/query'
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    payload = {"Where" : "1=1", "outFields": "objectID", "f" : "json", "returnGeometry":"true"}
    #payload = {"Where" : "Owner='Parks'", "outFields": "objectID", "f" : "json", "returnGeometry":"false"}
    
    ############## PROCESSING THE RESULT #################
    result = urllib.urlopen(url, urllib.urlencode(payload)).read()
    queryReturn =  json.loads(result)

    ############## RETURN THE BIN XY ####################
    binList = []
    
    for i in range(len(queryReturn['features'])):
        binList.append(queryReturn['features'][i])
    
    ################ RETURN LIST OF DICT ##################
    return binList

def updateAGOL(feat):
    """PNCC update AGOL streetbin collection features, requires a payload in dict format"""
    feat=feat 
    payload = {"f": "json", "features": feat}
    url = targetFeatureURL + "/0/updateFeatures"
    result = urllib.urlopen(url, urllib.urlencode(payload)).read()
    print json.loads(result)


def haversineFormula(x1,y1,x2,y2):
    x1 = x1
    y1 = y1
    x2 = x2
    y2 = y2

    x_dist = math.radians(x1 - x2)
    y_dist = math.radians(y1 - y2)

    y1_rad = math.radians(y1)
    y2_rad = math.radians(y2)

    a = math.sin(y_dist/2)**2 + math.sin(x_dist/2)**2 \
    * math.cos(y1_rad) * math.cos(y2_rad)

    c = 2 * math.asin(math.sqrt(a))

    distance = c * 6371 #kilometers
    return distance

########## RETURNING THE LAST TRUCK LOCATION #############
truckList = grabEvents()
#print truckList
#print "hello rubbish"

#########RETURNING THE BINLIST #############
binList = queryAGOL()
#for i in range(len(binList)):
#    print binList[i]
    
    
########### CALCULATE THE DISTANCE BETWEEN BIN & TRUCK ############
x1 = truckList[0]
y1 = truckList[1]
print x1,y1

for i in range(len(binList)):
    x2 = binList[i]['geometry']['x']
    y2 = binList[i]['geometry']['y']
    #print x2,y2
    disToTarget = haversineFormula(x1,y1,x2,y2)
    if disToTarget <= 1.5:
        print binList[i]['attributes']['OBJECTID']
        payload = {"attributes" : {"OBJECTID" : binList[i]['attributes']['OBJECTID'],"Done": "No","collectToday" : "Yes"}}
        updateAGOL(payload)
    else:
        pass