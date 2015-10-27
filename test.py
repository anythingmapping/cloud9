def _weather(zip):
    
    #url="http://www.dneonline.com/calculator.asmx?WSDL"
    #url="https://ws.smartrak.co.nz/Reporting/ReportingSoap.asmx?WSDL"
    url="http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL"
    print url
    
    #client = Client(url)
    #print client
    
    #print client ## shows the details of this service
    #result = client.service.GetWeatherInformation() 
    #result = client.service.GetCityWeatherByZIP(zip)
    #print result

#zip = 85001
#_weather(zip)
#main()