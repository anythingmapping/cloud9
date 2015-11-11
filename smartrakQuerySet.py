from suds.client import Client
import csv

class SmartrakExtract:
    def __init__(self,authentication):
        self.authentication = authentication
        self.url = "https://ws.smartrak.co.nz/Reporting/ReportingSoap.asmx?WSDL"
        

    def reportTrucks(self):
        """ method to report on the total trucks with remote IDs """
        self.client = Client(self.url)
        return self.client.service.GetRemotes(self.authentication)
        
        
    def reportLocations(self,remote,date,eventCodes):
        """ report on a trucks activity for a day, pass remoteID, date, and None """
        self.client = Client(self.url)
        return self.client.service.GetHistoryForDay(self.authentication,remote,date,eventCodes)

    
class SmartrakCompile:
    def __init__(self,processData,filename):
        self.processData = processData
        self.resultList = []
        self.filename = filename
    
    def process(self):
        """ process data into csv file """
        for i in range(len(self.processData[0])):
            self.resultList.append(self.processData[0][i])
        
        ####### WRITE THIS OUT ########
        f = open(self.filename, 'wt')
        try:
            writer = csv.writer(f)
            for i in range(len(self.resultList)):
                print self.resultList[0]
                writer.writerow(self.resultList[i])
                
        finally:
            f.close()    
    

print "well done"

