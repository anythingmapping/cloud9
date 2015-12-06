import math

def haversineFormula(binList,truckXY):
    
    def haversine(x1,y1,x2,y2):
        """ calculations function to return distance"""
        x1 = x1
        y1 = y1
        x2 = x2
        y2 = y2
        
        x_dist = math.radians(x1 - x2)
        y_dist = math.radians(y1 - y2)
    
        y1_rad = math.radians(y1)
        y2_rad = math.radians(y2)
    
        a = math.sin(y_dist/2)**2 + math.sin(x_dist/2)**2 \
        * math.cos(y1_rad) * math.cos(y2_rad)
        
        c = 2 * math.asin(math.sqrt(a))
        
        distance = c * 6371 #kilometers
        return distance
    
    #######################################################################    
    closeOIDList = []
    x1 = truckXY[0]
    y1 = truckXY[1]
    
    for i in range(len(binList)):
        x2 = binList[i]['geometry']['x']
        y2 = binList[i]['geometry']['y']
        disToTarget = haversine(x1,y1,x2,y2)
        
        #########################################################
        ############ HERE IS THE DISTANCE LOGIC #################
        if disToTarget <= 0.05:
            #print "OID close"
            closeOIDList.append(binList[i])
            
            #payload = {"attributes" : {"OBJECTID" : binList[i]['attributes']['OBJECTID'],"Done": "No","collectToday" : "Yes"}}
            #updateAGOL(payload)
        else:
            pass
    
    return closeOIDList



