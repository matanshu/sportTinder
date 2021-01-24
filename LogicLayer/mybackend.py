import sqlite3

"""Static Class which responsible on communicating with DB"""
class Database:
    conn = None
    cur = None
    db_name = './LogicLayer/database.db'
    csv_games = 'games_dataset.csv'

    """method which responsible on creating pitches table"""
    @staticmethod
    def create_pitches_table():
        sql = """CREATE TABLE IF NOT EXISTS`Pitches` (
        `id` INT NOT NULL,
        `name` VARCHAR(45) NULL,
        `latitude` FLOAT NOT NULL,
        `longitude` FLOAT NOT NULL,
        `type` VARCHAR(45) NOT NULL,
        `address` VARCHAR(100) NOT NULL,
        PRIMARY KEY (`id`));
        """
        Database.create_connection()
        try:
            Database.cur.execute(sql)
            print("success")
        except sqlite3.Error as e:
            Database.close_connection()
            print(e)
        Database.close_connection()

    """method which responsible on creating games table"""
    @staticmethod
    def create_games_table():
        sql = """CREATE TABLE IF NOT EXISTS`Games` (
        `id_game` INT NOT NULL,
        `sport_type` VARCHAR(45) NOT NULL,
        `pitch_id` INT NOT NULL,
        `start_game` timestamp NOT NULL,
        `end_game` timestamp NOT NULL,
        `max_participants` INT NOT NULL,
        `current_participants` INT NOT NULL,
        PRIMARY KEY (`id_game`),
        FOREIGN KEY(pitch_id) REFERENCES Pitches(id));
        """
        Database.create_connection()
        try:
            Database.cur.execute(sql)
            print("success")
        except sqlite3.Error as e:
            Database.close_connection()
            print(e)
        Database.close_connection()

    """method which responsible on loading and inserting data into pitches table"""
    @staticmethod
    def insert_data_into_pitches_table(list_pitches):
        Database.create_connection()
        for pitch in list_pitches:
            try:
                Database.cur.execute("insert into Pitches values(?,?,?,?,?, ?)",
                                     (pitch.id, pitch.name, pitch.latitude, pitch.longitude, pitch.type, pitch.address))
                Database.conn.commit()
            except sqlite3.Error as e:
                Database.close_connection()
                print(e)
        Database.close_connection()

    """getting all available pitches which stands in user demands"""
    @staticmethod
    def get_available_pitches(type, start_game):
        Database.create_connection()
        sql = "SELECT * FROM Pitches WHERE type=? AND id not in " \
              "(SELECT pitch_id FROM Games WHERE sport_type=? AND start_game=?) GROUP BY address"
        try:
            ans = Database.cur.execute(sql, (type, type, start_game,)).fetchall()
        except sqlite3.Error as e:
            Database.close_connection()
            print(e)
        Database.close_connection()
        return ans

    """method which responsible on getting all available games which stands in user demands"""
    @staticmethod
    def get_available_games(type, start_game):
        Database.create_connection()
        # start_game = datetime.datetime(year, month, day, start_hour)
        sql = "SELECT * FROM Games g1 INNER JOIN Games g2 on g1.id_game = g2.id_game " \
              "WHERE g1.sport_type=? AND g1.start_game=? AND g1.current_participants < g2.max_participants"
        try:
            ans = Database.cur.execute(sql, (type, start_game,)).fetchall()
        except sqlite3.Error as e:
            Database.close_connection()
            print(e)
        Database.close_connection()
        return ans

    """method which responsible on inserting new game and into Games table"""
    @staticmethod
    def create_game(id_game, type, pitch_id, start_game, end_game, max_participants):
        Database.create_connection()
        try:
            Database.cur.execute("INSERT INTO Games VALUES(?, ?, ?, ?, ?, ?, ?)",
                                 (id_game, type, pitch_id, start_game, end_game, max_participants, 1))
            Database.conn.commit()
        except sqlite3.Error as e:
            Database.close_connection()
            print(e)
        Database.close_connection()

    """method which responsible on adding new player to existing Game"""
    @staticmethod
    def joining_to_game(id_game, num_participants):
        Database.create_connection()
        try:
            Database.cur.execute("UPDATE Games SET current_participants = ? WHERE id_game = ?",
                                 (num_participants+1, id_game,))
            Database.conn.commit()
        except sqlite3.Error as e:
            Database.close_connection()
            print(e)
        Database.close_connection()

    """method which responsible on getting current num participants on specific game"""
    @staticmethod
    def get_current_participants_in_game(id_game):
        Database.create_connection()
        sql = "SELECT current_participants FROM Games WHERE id_game = ?"
        try:
            ans = Database.cur.execute(sql, (id_game,)).fetchall()
            current_participants = ans[0][0]
        except sqlite3.Error as e:
            Database.close_connection()
            print(e)
        Database.close_connection()
        return current_participants

    """method which responsible on getting all games id which already finished"""
    @staticmethod
    def get_finished_games(current_time):
        Database.create_connection()
        sql = "SELECT id_game FROM Games WHERE ? >= end_game"
        try:
            ans = Database.cur.execute(sql, (current_time,)).fetchall()
        except sqlite3.Error as e:
            Database.close_connection()
            print(e)
        Database.close_connection()
        return ans

    """method which responsible on deleting games which already finished"""
    @staticmethod
    def delete_finished_games(list_id_games):
        Database.create_connection()
        sql = "DELETE FROM Games WHERE id_game = ?"
        for id_game in list_id_games:
            try:
                Database.cur.execute(sql, (id_game,))
            except sqlite3.Error as e:
                Database.close_connection()
                print(e)
        Database.conn.commit()
        Database.close_connection()

    """method which responsible on getting max id_game from Games table"""
    @staticmethod
    def get_max_game_id():
        Database.create_connection()
        sql = "SELECT max(id_game) FROM Games"
        try:
            ans = Database.cur.execute(sql).fetchall()
            max_id = ans[0][0] if ans[0][0] is not None else 0
        except sqlite3.Error as e:
            Database.close_connection()
            print(e)
        Database.close_connection()
        return max_id

    """method which responsible on creating db if it doesn't exist. if it did exist, it won't do nothing"""
    @staticmethod
    def create_db(list_pitches):
        Database.create_pitches_table()
        Database.insert_data_into_pitches_table(list_pitches)
        Database.create_games_table()
        
    """getting full information on specific pitch"""
    @staticmethod
    def get_pitch(pitch_id):
        Database.create_connection()
        sql = "SELECT * FROM Pitches WHERE id = ?"
        try:
            ans = Database.cur.execute(sql, (pitch_id,)).fetchall()
            pitch = ans[0]
        except sqlite3.Error as e:
            Database.close_connection()
            print(e)
        Database.close_connection()
        return pitch

    """method which responsible on creating connection to DB"""
    @staticmethod
    def create_connection():
        Database.conn = sqlite3.connect(Database.db_name)
        Database.cur = Database.conn.cursor()

    """method which responsible on closing connection to DB"""
    @staticmethod
    def close_connection():
        Database.conn.close()
