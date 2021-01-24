import requests
from LogicLayer.location import Location
from LogicLayer.pitch import Pitch

"""Static Class which responsible on interfacing and communicating with openstreetmaps api and services"""
class OSM:
    nominatim_url = 'https://nominatim.openstreetmap.org/search?q='
    nominatim_params = 'format=json&polygon=1&addressdetails=1'
    overpass_url = "http://overpass-api.de/api/interpreter"
    area = 'New York'
    pitches_types = ['basketball', 'baseball', 'tennis']

    """method which responsible on getting all basketball, baseball and tennis pitches locations 
    from openstreetmaps data locating in the US, New York"""


    @staticmethod
    def get_pitches():
        list_pitches = []
        for pitch_type in OSM.pitches_types:
            overpass_query = """
                    [out:json][timeout:25];
                    (area[name = "New York"]; node(area)[sport= """ + pitch_type + """][leisure=pitch];);out body;
                    """
            response = requests.get(OSM.overpass_url, params={'data': overpass_query})
            data = response.json()
            for location in data['elements']:
                if location['type'] == 'node':
                    latitude = location['lat']
                    longitude = location['lon']
                    address = OSM.get_address_by_coordinates(latitude, longitude)
                    name = location['tags']['name'] if 'name' in location['tags'].keys() else ''
                    pitch = Pitch(location['id'], name, latitude, longitude, pitch_type, address)
                    list_pitches.append(pitch)
        return list_pitches

    """method which getting street address and returns full street location info: latitude, longitude,
     place id and more.. by getting it from openstreetmaps data"""
    @staticmethod
    def get_location(street, city="New York", country='ארצות הברית'):
        response = requests.get(OSM.nominatim_url + street + ", " + city + ", " + country + '&' + OSM.nominatim_params)
        data = response.json()
        if len(data) > 0:
            address = data[0]['display_name'] if 'display_name' in data[0].keys() else ''
            current_location = Location(data[0]['place_id'], '', data[0]['lat'], data[0]['lon'], address)
            return current_location
        else:
            return None

    """method which getting latitude and longitude, and returns from openstreetmaps data
     an address description of the location"""
    @staticmethod
    def get_address_by_coordinates(lat, lon):
        url = 'https://nominatim.openstreetmap.org/reverse.php?'
        response = requests.get(url + 'lat=' + str(lat) + '&lon=' + str(lon) + '&format=jsonv2')
        data = response.json()
        address = data['display_name']
        return address
