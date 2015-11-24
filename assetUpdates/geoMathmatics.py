import math


def haversineFormula(x1,y1,x2,y2):
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