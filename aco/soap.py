import urllib

import json
import sys
import time

#local import
from password import *

currentDay = "Thursday" + "Collect"
targetFeatureURL = "http://services.arcgis.com/Fv0Tvc98QEDvQyjL/arcgis/rest/services/LiveCollectionData_WFL/FeatureServer"
print username, password, portalUrl

def generateToken(username, password, portalUrl):
    """ PNCC generateToken for accessing AGOL content """
    
    parameters = urllib.urlencode({'username' : username,
                        'password' : password,
                        'client' : 'referer',
                        'referer': portalUrl,
                        'expiration': 60,
                        'f' : 'json'})
    parameters = parameters.encode('utf-8')
    
    try:
        print "starting urllib"
        urllib.urlopen(portalUrl + '/sharing/rest/generateToken?',parameters)
        response = urllib.urlopen(portalUrl + '/sharing/rest/generateToken?',parameters)
    except Exception as e:
        print(e)
        print "stopping system"
        sys.exit(0)
    responseJSON = json.loads(response.read())
    #print responseJSON
    
    token = responseJSON.get('token')
    print "Token response complete"
    print token
    return token

def queryAGOL(where, token):
    """ PNCC queryAGOL content """
    #url = 'http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/ProcessManager_WFL/FeatureServer/0'
    url = targetFeatureURL + '/0/query'
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    payload = {"Where" : where, "outFields": "objectID", "f" : "json", "returnGeometry":"false", "token":token}
    
    result = urllib.urlopen(url, urllib.urlencode(payload)).read()
    queryReturn =  json.loads(result)
    print queryReturn
    activePickupList = []
    
    for i in range(len(queryReturn['features'])):
        activePickupList.append(queryReturn['features'][i]['attributes']['OBJECTID'])
    return activePickupList

def logicQuery():
    whereQuery = "WednesdayCollect = Yes"
    return whereQuery


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

token = generateToken(username, password, portalUrl)
whereQuery = logicQuery()
objId = queryAGOL(whereQuery, token)
print objId

##### commented while i test 
#featUpdates = formatQuery(objId, "No")
#updateAGOL(featUpdates)

#objId = queryAGOL(currentDay+"='Yes'")
#featUpdates = formatQuery(objId, "Yes")
#updateAGOL(featUpdates)


print "keep working"
#for help look here:
#https://esriaustraliatechblog.wordpress.com/2013/12/20/using-python-to-write-features-to-a-feature-service/