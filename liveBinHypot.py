import urllib
import json
from suds.client import Client

def grabEvents():
    """ function to grab current smartrak location using. requires suds.client as Client """
    url="https://ws.smartrak.co.nz/Reporting/ReportingSoap.asmx?WSDL"
    client = Client(url)

    ####### HARD CODED VALUES ############
    authentication = "D37EEE129A664B46B5C0EC0C1CC8CC1D"
    binTruck169 = 7771
    remoteId = 7771
    date = "2015-11-11" #This does not seem to take a UTC time value
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
    targetFeatureURL = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/LiveCollectionData_WFL/FeatureServer"
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



########## RETURNING THE LAST TRUCK LOCATION #############
truckList = grabEvents()
print truckList
print "hello rubbish"

#########RETURNING THE BINLIST #############
binList = queryAGOL()
for i in range(len(binList)):
    print binList[i]
    
    
########### CALCULATE THE DISTANCE BETWEEN BIN & TRUCK ############

