from LogicLayer.location import Location

"""class which inherits from Location class and representing sport Pitch"""
class Pitch(Location):

    def __init__(self, id, name, latitude, longitude, type, address):
        super().__init__(id, name, latitude, longitude, address)
        self.type = type
