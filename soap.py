import urllib
import json
import time

currentDay = "Thursday" + "Collect"
targetFeatureURL = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/LiveCollectionData_WFL/FeatureServer"



def queryAGOL(where):
    """ PNCC queryAGOL content """
    #url = 'http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/ProcessManager_WFL/FeatureServer/0'
    url = targetFeatureURL + '/0/query'
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    payload = {"Where" : where, "outFields": "objectID", "f" : "json", "returnGeometry":"false"}
    
    result = urllib.urlopen(url, urllib.urlencode(payload)).read()
    queryReturn =  json.loads(result)
    print queryReturn
    activePickupList = []
    
    for i in range(len(queryReturn['features'])):
        activePickupList.append(queryReturn['features'][i]['attributes']['OBJECTID'])
    return activePickupList


def formatQuery(activePickupList,state):
    """PNCC feature update payload formatter function"""
    targetList = []
    
    for target in activePickupList:
        targetList.append({"attributes" : {"OBJECTID" : target,"Done": "No","collectToday" : state}})
    return targetList


def updateAGOL(feat):
    """PNCC update AGOL streetbin collection features"""
    feat=feat 
    payload = {"f": "json", "features": feat}
    url = targetFeatureURL + "/0/updateFeatures"
    #url = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/ProcessManager_WFL/FeatureServer/0/updateFeatures" #thetemplate
    result = urllib.urlopen(url, urllib.urlencode(payload)).read()
    #print json.loads(result)


objId = queryAGOL("1=1")
featUpdates = formatQuery(objId, "No")
updateAGOL(featUpdates)

objId = queryAGOL(currentDay+"='Yes'")
featUpdates = formatQuery(objId, "Yes")
updateAGOL(featUpdates)


print "keep working"
#for help look here:
#https://esriaustraliatechblog.wordpress.com/2013/12/20/using-python-to-write-features-to-a-feature-service/