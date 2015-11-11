from suds.client import Client
import csv


def outputFunc(filename, resultList):
    """Function to write data to csv archive"""
    #assert len(parks) == 3
    
    f = open(filename, 'wt')
    
    try:
        writer = csv.writer(f)
        for i in range(len(resultList)):
            print resultList[0]
            writer.writerow(resultList[i])
            
    finally:
        f.close()
    

def grabEvents():
    """function to grab eventcodes from smartrak"""
    
    url="https://ws.smartrak.co.nz/Reporting/ReportingSoap.asmx?WSDL"
    client = Client(url)
    #print client
    
    #### CREDS ####
    authentication = "D37EEE129A664B46B5C0EC0C1CC8CC1D"
    
    glass194 = 7813
    glass195 = 16100
    
    ### set this to which truck you want 
    remoteId = glass194
    
    date = "2015-09-16" #This does not seem to take a UTC time value
    eventCodes = None
    filename = "truck{0}{1}.csv".format(remoteId,date)
    
    #### GETTING THE REPORT ####
    result = client.service.GetHistoryForDay(authentication, remoteId, date, eventCodes)
    resultList = []
    for i in range(len(result[0])):
        resultList.append(result[0][i])
    
    
    ##### WRITING USING THE CRED ####
    f = open(filename, 'wt')
    
    try:
        writer = csv.writer(f)
        for i in range(len(resultList)):
            print resultList[0]
            writer.writerow(resultList[i])
            
    finally:
        f.close()

grabEvents()

#the date for archive naming
#filename = "testoutput.csv"

#outputs the data to archive file on agsserv101
#outputFunc(filename,resultList)
print "The process is complete"