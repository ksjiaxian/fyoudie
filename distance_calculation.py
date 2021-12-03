########################################################################################################################
# Get Location and Direction Data
########################################################################################################################

import csv
import requests
import json
import math

api_key = "AgUSM867a3r-7GFqCUQ81nvWLngFtrbanaBzA41qVEDoN-PFSEQiCTtx0eY9aJ--"


def get_address(name, lattitude, longitude):
    lat_long_string = str(lattitude) + ',' + str(longitude)
    response = requests.get("https://dev.virtualearth.net/REST/v1/LocalSearch/",
                            params={"query": name,
                                    "userLocation": lat_long_string,
                                    "key": api_key})
    data = response.json()
    location_data = data['resourceSets'][0]['resources'][0]["Address"]
    return location_data


def get_current_location(lattitude, longitude):
    lat_long_string = str(lattitude) + ',' + str(longitude)
    response = requests.get("https://dev.virtualearth.net/REST/v1/Locations/" + lat_long_string + "?",
                            params={"key": api_key})
    data = response.json()
    location_data = data['resourceSets'][0]['resources'][0]["address"]
    return location_data


def get_distance_time(name, lattitude, longitude, trans_method):
    lat_long_string = str(lattitude) + ',' + str(longitude)
    dest_address = get_address(name, lattitude, longitude)["formattedAddress"]

    if (trans_method == "Driving") | (trans_method == "Transit"):
        optimization = "time"
    else:
        optimization = "distance"

    response = requests.get("https://dev.virtualearth.net/REST/v1/Routes/" + str(trans_method) + "?",
                            params={"o": "json",
                                    "wp.0": lat_long_string,
                                    "wp.1": dest_address,
                                    "distanceUnit": "Mile",
                                    "optimize": optimization,
                                    "key": api_key})
    data = response.json()
    direction_data = data['resourceSets'][0]["resources"][0]
    return direction_data


# # test get address
# print(json.dumps(get_address("Pho 75", 38.8963, -77.0688), indent=4, sort_keys=True))
#
# # test get current location
# print(json.dumps(get_current_location(38.8963, -77.0688), indent=4, sort_keys=True))

# test get distance_time
# print(json.dumps(get_distance_time("Eden Center", 38.8963, -77.0688, "Walking"), indent=4, sort_keys=True))

# this is the time in minutes it takes to walk there
print(math.ceil(get_distance_time("Eden Center", 38.8963, -77.0688, "Walking")["travelDuration"] / 60))

# this is the distance in miles it takes to walk there
print(math.ceil(get_distance_time("Eden Center", 38.8963, -77.0688, "Walking")["travelDistance"] * 10) / 10)