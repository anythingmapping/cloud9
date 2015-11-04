from suds.client import Client
import csv

"""EventHistoryID = 6852991503
RemoteID = 6817
EventCodeText = "TRAVELLED"
RtDate = 2015-10-16 14:17:34
Latitude = -40.35466
Longitude = 175.629415
Speed = 16
Heading = 61
Odometer = None
ExtraInfo = None
NearestAddress = "26-30 Stewart Crescent, Hokowhitu, Palmerston North City
SupplyVoltage = 28.1807008634
"""

def outputFunc(filename, resultList):
    """Function to write data to csv archive"""
    #assert len(parks) == 3
    
    f = open(filename, 'wt')
    
    try:
        writer = csv.writer(f)
        for i in range(len(resultList)):
            print resultList[0]
            writer.writerow(resultList[0])
            
        
    finally:
        f.close()
    

def grabEvents():
    """function to grab eventcodes from smartrak"""
    
    url="https://ws.smartrak.co.nz/Reporting/ReportingSoap.asmx?WSDL"
    client = Client(url)
    #print client
    
    authentication = "D37EEE129A664B46B5C0EC0C1CC8CC1D"
    remoteId = 6817
    date = "2015-10-16" #This does not seem to take a UTC time value
    eventCodes = None
    
    result = client.service.GetHistoryForDay(authentication, remoteId, date, eventCodes)
    resultList = []
    
    for i in range(len(result[0])):
        
        resultList.append(result[0][i])
    
    return resultList  

resultList = grabEvents()

#the date for archive naming
filename = "testoutput.csv"

#outputs the data to archive file on agsserv101
outputFunc(filename,resultList)
print "The process is complete"
