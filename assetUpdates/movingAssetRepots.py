from suds.client import Client

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
        
if __name__ == '__main__':
    app = SmartrakExtract('D37EEE129A664B46B5C0EC0C1CC8CC1D')
    a = app.reportTrucks()
    print a