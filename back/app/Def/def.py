from math import sin, cos, sqrt, atan2, radians

def distance(lat1, lng1, lat2, lng2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(52.2296756)
    lng1 = radians(21.0122287)
    lat2 = radians(52.406374)
    lng2 = radians(16.9251681)

    dlng = lng2 - lng1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlng / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance
