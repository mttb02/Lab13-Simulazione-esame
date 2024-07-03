from database.DB_connect import DBConnect
from model.state import State

class DAO():

    @staticmethod
    def get_all_years():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT YEAR(datetime) as year FROM sighting
                ORDER BY year"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_shapes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT shape FROM sighting
                    ORDER BY shape"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(row["shape"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_states():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM state"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(State(row["id"], row["Name"], row["Capital"], row["Lat"], row["Lng"], row["Area"], row["Population"], row["Neighbors"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_rel():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM neighbor
                WHERE state1 < state2"""

        cursor.execute(query, ())

        for row in cursor:
            result.append((row["state1"], row["state2"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_frequenze(year, shape):
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """SELECT state, COUNT(*) as f FROM sighting
                WHERE YEAR(datetime) = %s and shape = %s
                GROUP BY state"""

        cursor.execute(query, (year, shape))

        for row in cursor:
            result[row["state"].upper()] = row["f"]

        cursor.close()
        conn.close()
        return result

