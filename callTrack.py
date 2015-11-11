from smartrakQuerySet import SmartrakExtract,SmartrakCompile


def dataGet():
    glass194 = 7813
    glass195 = 16100
    eventCodes = None
    date = "2015-10-16"
    
    authentication = "D37EEE129A664B46B5C0EC0C1CC8CC1D"
    report = SmartrakExtract(authentication)
    
    ####### THESE REPORT INTAKE #######
    #remotesQuery = report.reportTrucks()
    #print remotesQuery
    
    dayHistory = report.reportLocations(glass194,date,eventCodes)
    return dayHistory

def processData():
    filename = "glass194.csv"
    dataProcess = SmartrakCompile(dayHistory,filename)
    dataProcess.process()

dayHistory = dataGet()
processData()