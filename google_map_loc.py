from math import pi, radians, cos, sin, asin, sqrt,acos



def get_cordinate(usr_lat,usr_log,km=5):

        high_latitude  = usr_lat  + (km / 6371) * (180 / pi);
        left_longitude = usr_log - (km / 6371) * (180 / pi) / cos(usr_lat * pi/180);

        low_latitude  = usr_lat  - (km / 6371) * (180 / pi);
        right_longitude = usr_log + (km / 6371) * (180 / pi) / cos(usr_lat * pi/180);

        return high_latitude,low_latitude,left_longitude,right_longitude



