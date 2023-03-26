import sqlite3

SQL_CREATE = "CREATE TABLE entity_counts (entity TEXT PRIMARY KEY, count INTEGER)"
SQL_SELECT = "SELECT * FROM entity_counts"
SQL_INSERT = "INSERT INTO entity_counts VALUES (?, ?)"
SQL_UPDATE = "UPDATE entity_counts SET count = count + ? WHERE entity = ?"



class DatabaseConnection(object):

    def __init__(self, filename):
        self.connection = sqlite3.connect(filename, check_same_thread=False)

    def create_schema(self):
        try:
            self.connection.execute(SQL_CREATE)
        except sqlite3.OperationalError:
            print("Warning: 'entity_counts' table was already created, ignoring...")

    def get(self, entity=None):
        cursor = (self.connection.execute(f'{SQL_SELECT} WHERE name="{entity}"')
                  if entity is not None else self.connection.execute(SQL_SELECT))
        return cursor.fetchall()

    def add(self, entity, count):
        try:
            self.connection.execute(SQL_INSERT, (entity, count))
            self.connection.commit()
        except sqlite3.IntegrityError:
            self.connection.execute(SQL_UPDATE, (count, entity))
            self.connection.commit()


if __name__ == '__main__':
    pass
