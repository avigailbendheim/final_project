# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# import sqlite3
#
# # Connect to database
# conn = sqlite3.connect('BabysitterDB.db')
#
# # Create a cursor object
# cursor = conn.cursor()
# # conn.text_factory = lambda x: str(x, 'latin1')
# conn.text_factory = lambda x: str(x, 'iso-8859-1')
#
# # Create table
# girls = '''CREATE TABLE Babysitters (
#     Id INTEGER PRIMARY KEY,
#     Mail TEXT NOT NULL,
#     FirstName TEXT NOT NULL,
#     LastName TEXT NOT NULL,
#     YearOfBirth INTEGER NOT NULL,
#     City INTEGER NOT NULL,
#     Neighborhood INTEGER NOT NULL,
#     Seminary TEXT,
#     Cell TEXT NOT NULL,
#     FOREIGN KEY (City) REFERENCES Cities(Id),
#     FOREIGN KEY (Neighborhood) REFERENCES Neighborhoods(Id)
# );
# '''
# mothers = '''
# CREATE TABLE Famalies (
#     Id               INTEGER       PRIMARY KEY,
#     Mail             TEXT          NOT NULL,
#     FirstName    TEXT          NOT NULL,
#     LastName     TEXT          NOT NULL,
#     city             INTEGER       NOT NULL,
#     Neighborhood     INTEGER       NOT NULL,
#     Cell             TEXT          NOT NULL,
#     NumOfChildren    INTEGER,
#     OldestChild      INTEGER,
#     YoungestChildren INTEGER,
#     FOREIGN KEY (city) REFERENCES Cities (Id),
#     FOREIGN KEY (Neighborhood) REFERENCES Neighborhoods (Id)
# );
# '''
# cities = '''CREATE TABLE Cities(
#     Id  INTEGER PRIMARY KEY,
#     Name TEXT NOT NULL
#         )
# '''
# neighborhoods = '''CREATE TABLE Neighborhoods(
#      Id INTEGER PRIMARY KEY,
#      Name TEXT NOT NULL,
#      city Integer NOT NULL,
#     FOREIGN KEY (city) REFERENCES Cities (Id)
#
# )
# '''
# schedule = '''
# CREATE TABLE schedule (
#     Id INTEGER PRIMARY KEY,
#     babysitter_id INTEGER NOT NULL,
#     day_of_week INTEGER,
#     start_hour TEXT NOT NULL,
#     end_hour TEXT NOT NULL,
#     FOREIGN KEY (babysitter_id) REFERENCES Babysitters (Id),
#     FOREIGN KEY (day_of_week) REFERENCES Days (Id)
# );
# '''
#
# days = '''CREATE TABLE Days(
#     Id INTEGER PRIMARY KEY,
#     Name TEXT NOT NULL
#     )
# '''
#
#
# cursor.execute("""INSERT INTO schedule (babysitter_id,day_of_week,start_hour,end_hour)
#               VALUES (2,3,"19:30","24:00")""")
#
#
#
#
# # Commit changes and close connection
# conn.commit()
# conn.close()
#
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm