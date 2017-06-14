class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {"host": "localhost", "user": "project","passwd": "project1","db": ""}
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()


def getDataFromAquarium(self):
    # Data die in de tabel Aquarium zit
    sqlQuery = "SELECT * FROM aquarium"
    self.__cursor.execute(sqlQuery)
    result = self.__cursor.fetchall()
    self.__cursor.close()
    return result

def getDataFromSensor(self):
    # Data uit de tabel sensor
    sqlQuery = "SELECT * FROM sensor"
    self.__cursor.execute(sqlQuery)
    result = self.__cursor.fetchall()
    self.__cursor.close()
    return result


def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
    # Query met parameters
    sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
    # Combineren van de query en parameter
    sqlCommand = sqlQuery.format(param1=voorwaarde)

    self.__cursor.execute(sqlCommand)
    result = self.__cursor.fetchall()
    self.__cursor.close()
    return result


def setDataToDatabase(self, value1):
    # Query met parameters
    sqlQuery = "INSERT INTO tablename (columnname) VALUES ('{param1}')"
    # Combineren van de query en parameter
    sqlCommand = sqlQuery.format(param1=value1)

    self.__cursor.execute(sqlCommand)
    self.__connection.commit()
    self.__cursor.close()