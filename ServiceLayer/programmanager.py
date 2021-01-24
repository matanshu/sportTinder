from LogicLayer.mybackend import Database
import datetime
from LogicLayer.game import Game
from LogicLayer.pitch import Pitch
from LogicLayer.openstreetmaps import OSM
from os.path import isfile

"""Static Class which responsible on coordinating between view layer to logic later
the class is collaborating with GUI module and using OSM and mybackend modules for getting results"""
class ProgramManager:
    db_name = './LogicLayer/database.db'
    location = None

    """method which responsible on setting the location of the user
     getting the address details from osm"""
    @staticmethod
    def set_user_location(street):
        ProgramManager.location = OSM.get_location(street, "New York", 'ארצות הברית')

    """method which responsible on getting all available pitches which stands in user demands"""
    @staticmethod
    def get_available_pitches(type, year, month, day, start_hour, requested_distance):
        ProgramManager.delete_finished_games()
        start_game = datetime.datetime(year, month, day, start_hour)
        list_pitches = Database.get_available_pitches(type, start_game)
        pitches_full_data = ProgramManager.get_full_data_on_pitches(list_pitches)
        pitches_full_data = [item for item in pitches_full_data if item[1] <= requested_distance]
        return sorted(pitches_full_data, key=lambda x: x[1])

    """method which responsible on getting full data from db on pitches"""
    @staticmethod
    def get_full_data_on_pitches(list_pitches):
        games_full_data = []
        for pitch in list_pitches:
            pitch_object = Pitch(pitch[0], pitch[1], pitch[2], pitch[3], pitch[4], pitch[5])
            distance = pitch_object.calculate_distance(ProgramManager.location)
            games_full_data.append([pitch_object, distance])
        return games_full_data

    """method which responsible on getting all available games which stands in user demands"""
    @staticmethod
    def get_available_games(type, year, month, day, start_hour, requested_distance):
        ProgramManager.delete_finished_games()
        start_game = datetime.datetime(year, month, day, start_hour)
        games = Database.get_available_games(type=type, start_game=start_game)
        list_games = ProgramManager.build_games_objects(games)
        games_full_data = ProgramManager.get_full_data_on_games(list_games)
        games_full_data = [item for item in games_full_data if item[1] <= requested_distance]
        return sorted(games_full_data, key= lambda x: x[1])

    """method which responsible on getting full data from db on games"""
    @staticmethod
    def get_full_data_on_games(list_games):
        games_full_data = []
        for game in list_games:
            pitch_db = Database.get_pitch(game.pitch_id)
            pitch_object = Pitch(pitch_db[0], pitch_db[1], pitch_db[2], pitch_db[3], pitch_db[4], pitch_db[5])
            distance = pitch_object.calculate_distance(ProgramManager.location)
            games_full_data.append([game, distance, pitch_object])
        return games_full_data

    """method which responsible on building games objects"""
    @staticmethod
    def build_games_objects(games):
        list_games = []
        for game in games:
            start_game = datetime.datetime.strptime(game[3], '%Y-%m-%d %H:%M:%S')
            end_game = datetime.datetime.strptime(game[4], '%Y-%m-%d %H:%M:%S')
            list_games.append(Game(id_game=game[0], sport_type=game[1], pitch_id=game[2], start_game=start_game,
                        end_game=end_game, max_participants=game[5], current_participants=game[6]))
        return list_games

    """method which responsible on creating new game accordingly to user game demands"""
    @staticmethod
    def create_game(type, pitch_id, year, month, day, start_hour, max_participants):
        ProgramManager.delete_finished_games()
        id_game = Database.get_max_game_id() + 1
        start_game = datetime.datetime(year, month, day, start_hour)
        end_game = datetime.datetime(year, month, day, start_hour+2)
        Database.create_game(id_game, type, pitch_id, start_game, end_game, max_participants)

    """method which responsible on joining the user to existing game"""
    @staticmethod
    def join_to_game(id_game):
        num_participants = Database.get_current_participants_in_game(id_game=id_game)
        Database.joining_to_game(id_game=id_game, num_participants=num_participants)

    """method which responsible on getting all games id which already finished"""
    @staticmethod
    def get_finished_games(current_time):
        pass

    """method which responsible on deleting games which already finished"""
    @staticmethod
    def delete_finished_games():
        current_time = datetime.datetime.now()
        finished_games = Database.get_finished_games(current_time)
        if len(finished_games) is not 0:
            list_finished_games = ProgramManager.extract_to_list(finished_games)
            Database.delete_finished_games(list_id_games=list_finished_games)

    """method which responsible on extracting the input data into list"""
    @staticmethod
    def extract_to_list(finished_games):
        list_finished_games = []
        for game in finished_games:
            list_finished_games.append(game[0])
        return list_finished_games

    """method will return True if current street input is legal street address in New York 
    otherwise returns False"""
    @staticmethod
    def is_legal_address(street):
        return OSM.get_location(street) is not None

    """method which responsible on creating db if it doesn't exist. if it did exist, it won't do nothing"""
    @staticmethod
    def create_db():
        if not isfile(ProgramManager.db_name):
            list_pitches = OSM.get_pitches()
            Database.create_db(list_pitches)
        else:
            print('DB already exist')

