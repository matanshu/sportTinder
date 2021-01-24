# imports
import haversine as hs

"""class which representing a geographic Location with latitude, longitude and more location details"""
class Location:
    def __init__(self, id, name, latitude, longitude, address):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.address = address

    def __str__(self) -> str:
        return self.latitude + " " + self.longitude

    """returns latitude and longitude"""
    def get_location(self):
        return [float(self.latitude), float(self.longitude)]

    """calculating distance between two locations"""
    def calculate_distance(self, location):
        return hs.haversine(self.get_location(), location.get_location())