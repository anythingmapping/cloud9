
#http://anothergisblog.blogspot.co.nz/2013/02/query-feature-service-by-object-ids.html
#import urllib2

#todo
#assert error checking
#csv naming
#get current date
#csv open file in a different working directory
#set up on agserve101

import urllib
import urlparse
import httplib
import json
import csv

days = ['MondayCollect',
        'TuesdayCollect',
        'WednesdayCollect',
        'ThursdayCollect',
        'FridayCollect',
        'SaturdayCollect',
        'SundayCollect']

def outputFunc(filename, parks,roading,private):
    """Function to write data to csv archive"""
    #assert len(parks) == 3
    
    f = open(filename, 'wt')
    
    try:
        writer = csv.writer(f)
        writer.writerow(days)
        writer.writerow(parks)
        writer.writerow(roading)
        writer.writerow(private)
    finally:
        f.close()
    
    
def dataExtract(queryResults):
    """data extraction, that takes an AGOL query return"""
    days = ['MondayCollect',
            'TuesdayCollect',
            'WednesdayCollect',
            'ThursdayCollect',
            'FridayCollect',
            'SaturdayCollect',
            'SundayCollect']

    #counting the instances of bin collections
    parkCount = 0
    roadingCount = 0
    otherCount = 0

    #output totals of bin collections
    parkOutput = []
    roadingOutput = []
    otherOutput = []
    
    #iterate over each day
    for day in days:
        
        #iterate over the number of bins
        for i in range(len(queryResults)):
            
            #check if the bin was collected on the day...
            if str(queryResults[i]['attributes'][day]).strip().lower() == 'yes':
                
                #unknown formatting issue with the data, these lines fix it
                strResult = str(queryResults[i]['attributes']['Owner'])
                strResultForm = strResult.lower().strip()
                
                #update the counts if True
                if strResultForm == 'roading':
                    roadingCount += 1
                elif strResultForm == 'parks':
                    parkCount += 1
                elif strResultForm == 'private':
                    otherCount += 1
                else:
                    otherCount +=1

        #print "Day: {} \nparkCount: {} \nroadingCount: {} \notherCount: {} \n\n".format(day,parkCount,roadingCount,otherCount)
        
        parkOutput.append(parkCount)
        roadingOutput.append(roadingCount)
        otherOutput.append(otherCount)
        
        parkCount = 0
        roadingCount =0
        otherCount =0
    
    return parkOutput,roadingOutput,otherOutput

def queryAGOL():
    """ PNCC queryAGOL content """
    #url = 'http://services.arcgis.com/Fv0Tvc98QEDvQyjL/ArcGIS/rest/services/ProcessManager_WFL/FeatureServer/0'
    url = 'http://services.arcgis.com/Fv0Tvc98QEDvQyjL/arcgis/rest/services/LiveCollectionData_WFL/FeatureServer/0'
    url = url + '/query'
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    payload = {"Where" : """1 = '1'""", "outFields": "*","ReturnCountOnly":"False", "f" : "json", "returnGeometry":"false"}
    
    result = urllib.urlopen(url, urllib.urlencode(payload)).read()
    work =  json.loads(result)

    #This line is cutting out the addition response data
    #remove for full breakdown of the stats, but it will break the dataExtract
    return work['features']

#main loop
queryResults = queryAGOL()
print "The total length of the dataset is {}".format(len(queryResults))

#print queryResults[0]['attributes']['MondayCollect']
parks,roading,other = dataExtract(queryResults)

#the date for archive naming
filename = "testoutput.csv"

#outputs the data to archive file on agsserv101
outputFunc(filename,parks,roading,other)

print "The process is complete"