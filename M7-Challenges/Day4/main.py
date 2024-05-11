from math import atan2, degrees, radians, sin, cos

def qiblaFinder(latitude, longitude):
    # Coordinates of the Kaaba
    kaaba_latitude = 21.4225239
    kaaba_longitude = 39.8261816

    # Convert latitudes and longitudes from degrees to radians
    lat1 = radians(latitude)
    lon1 = radians(longitude)
    lat2 = radians(kaaba_latitude)
    lon2 = radians(kaaba_longitude)

    # Calculate the difference in longitude
    delta_lon = lon2 - lon1

    # Calculate the Qibla direction using atan2
    x = sin(delta_lon) * cos(lat2)
    y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(delta_lon)
    qibla_angle_rad = atan2(x, y)
    # Convert from radians to degrees
    qibla_angle = degrees(qibla_angle_rad)
    
    qibla_angle = (qibla_angle + 360) % 360

    return qibla_angle
print(qiblaFinder(24.8267741,46.3573171))
