import sqlite3

db = 'Babysitter.db'
db = sqlite3.connect('')


class MothersDatabase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS Famalies (
                Id               INTEGER       PRIMARY KEY,
                Mail             TEXT          NOT NULL,
                "First Name"     TEXT          NOT NULL,
                "Last Name"      TEXT          NOT NULL,
                city             INTEGER       NOT NULL,
                Neighborhood     INTEGER       NOT NULL,
                Cell             TEXT          NOT NULL,
                NumOfChildren    INTEGER,
                OldestChild      INTEGER,
                YoungestChildren INTEGER,
                FOREIGN KEY (city) REFERENCES Cities (Id),
                FOREIGN KEY (Neighborhood) REFERENCES Neighborhoods (Id)
            );''')
        self.conn.commit()

    def create_family(self, mail, firstname, lastname, city, neighborhood, cell, num_of_children, oldest_children,
                      youngest_children):
        self.cur.execute("INSERT INTO Famalies VALUES (NULL,?,?,?,?,?,?,?,?)", (
        mail, firstname, lastname, city, neighborhood, cell, num_of_children, oldest_children, youngest_children))
        self.conn.commit()

    def read_all_family(self):
        self.cur.execute("SELECT * FROM Famalies")
        rows = self.cur.fetchall()
        return rows

    def read_family(self, id):
        self.cur.execute("SELECT FROM Famalies WHERE id=?", (id,))
        family = self.cur.fetchone()
        return family

    def update_family(self, id, mail, firstname, lastname, city, neighborhood, cell, num_of_children, oldest_children,
                      youngest_children):
        self.cur.execute('''UPDATE Famalies 
                                SET mail=?,firstname=?, lastname=?,city=?,neighborhood=?,
                                cell=?,num_of_children=?,oldest_children=?,youngest_children=? WHERE id, = ?'''
                                (mail, firstname, lastname, city, neighborhood, cell, num_of_children, oldest_children, youngest_children, id))
        self.conn.commit()

    def delete_family12(self,id):
        self.cur.execute("DELETE FROM Famalies WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()