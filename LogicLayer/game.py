
"""class which representing a sport game"""
class Game:
    def __init__(self, id_game, sport_type, pitch_id, start_game, end_game, max_participants, current_participants):
        self.id_game = id_game
        self.sport_type = sport_type
        self.pitch_id = pitch_id
        self.start_game = start_game
        self.end_game = end_game
        self.max_participants = max_participants
        # self.participants = list()
        self.current_participants = current_participants
