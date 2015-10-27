#-------------------------------------------------------------------------------
# Name:        updateAGOL
# Purpose:     update AGOL features
#
# Author:      mostynl
#
# Created:     24/08/2015
# Copyright:   (c) mostynl 2015
# Licence:     NZ Creative Commons 3.0
#-------------------------------------------------------------------------------

import urllib
import json
import time

currentDay = "Sunday" + "Collect"
targetFeatureURL = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/LiveCollectionData_WFL/FeatureServer"

def queryAGOL():
    """ PNCC queryAGOL content """
    #url = 'http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/ProcessManager_WFL/FeatureServer/0'
    url = targetFeatureURL + '/0/query'
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    payload = {"Where" : currentDay+"='Yes'", "outFields": "objectID", "f" : "json", "returnGeometry":"false"}
    #payload = {"Where" : "Owner='Parks'", "outFields": "objectID", "f" : "json", "returnGeometry":"false"}
    
    result = urllib.urlopen(url, urllib.urlencode(payload)).read()
    queryReturn =  json.loads(result)
    print queryReturn
    activePickupList = []
    
    for i in range(len(queryReturn['features'])):
        activePickupList.append(queryReturn['features'][i]['attributes']['OBJECTID'])
    return activePickupList


def formatQuery(activePickupList):
    """PNCC feature update payload formatter function"""
    targetList = []
    
    for target in activePickupList:
        targetList.append({"attributes" : {"OBJECTID" : target,"Done": "No","collectToday" : "Yes"}})
    return targetList


def updateAGOL(feat):
    """PNCC update AGOL streetbin collection features"""
    feat=feat 
    payload = {"f": "json", "features": feat}
    url = targetFeatureURL + "/0/updateFeatures"
    #url = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/ProcessManager_WFL/FeatureServer/0/updateFeatures" #thetemplate
    result = urllib.urlopen(url, urllib.urlencode(payload)).read()
    #print json.loads(result)


objId = queryAGOL()
featUpdates = formatQuery(objId)
updateAGOL(featUpdates)


print "well done"
#for help look here:
#https://esriaustraliatechblog.wordpress.com/2013/12/20/using-python-to-write-features-to-a-feature-service/