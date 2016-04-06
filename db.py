__author__ = 'brown'
import sqlite3, sys

class Database():
    connection = None
    data = None

    def __init__(self):
        try:
            self.connection = sqlite3.connect('fruitshoot.db')
            self.cursor = self.connection.cursor()
        except:
            self.connection = "Error"
            print(self.connection)
            sys.exit(1)

    def execute(self,command):
        self.cursor.execute(command)

    def versionNo(self):
        self.execute('SELECT SQLITE_VERSION()')
        self.data = self.cursor.fetchone()

    def createLevelTables(self):
        self.execute("DROP TABLE IF EXISTS Lvls")
        self.execute("CREATE TABLE Lvls(LevelNo INT,PlayerName TEXT, Score INT)")
        self.execute("INSERT INTO Lvls VALUES(1,'Brown',5)")
        self.execute("INSERT INTO Lvls VALUES(1,'Green',4)")
        self.execute("INSERT INTO Lvls VALUES(2,'Brown',6)")
        self.execute("INSERT INTO Lvls VALUES(2,'Green',7)")
        self.execute("INSERT INTO Lvls VALUES(3,'Brown',2)")
        self.execute("INSERT INTO Lvls VALUES(4,'Brown',3)")
        self.connection.commit()


    def playerMaxLevel(self,player):
        command = "SELECT MAX(LevelNo) FROM Lvls WHERE PlayerName = '" + player + "'"
        self.execute(command)
        self.data = self.cursor.fetchone()

    def playerLevelScore(self,player,level):
        command = "SELECT Score FROM Lvls WHERE PlayerName = '" + player + "' AND LevelNo = " + str(level)
        print(command)
        self.execute(command)
        self.data = self.cursor.fetchone()

    def players(self):
        self.execute("SELECT PlayerName from Lvls")
        self.data = self.cursor.fetchall()
        for player in self.data:
            print(player)

    def exit(self):
        if self.connection:
            self.connection.close()
            print("Exited")

connect = Database()
connect.createLevelTables()
connect.playerLevelScore('Brown',1)
connect.players()
print(connect.data)
connect.exit()
