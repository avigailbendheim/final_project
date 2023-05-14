import sqlite3

DB = '----'


class BaseModel:
    _cur = None

    def cur(self):
        if BaseModel._cur == None:
            BaseModel._cur = self.conn.cursor()
        return BaseModel._cur

    def __init__(self):
        if BaseModel._cur != None:
            raise Exception("You already have cur")
        else:
            self.conn = sqlite3.connect(DB)
            self._cur = self.conn.cursor()
        self.table = None

    def create(self, data_dic):
        columns = ', '.join(data_dic.keys())
        values = ', '.join(["'{}'".format(v) for v in data_dic.values()])
        query = "INSERT INTO {} ({}) VALUES ({})".format(self.table, columns, values)
        self.cur.execute(query)

    def read(self, id):
        self.cur.execute('''SELECT * FROM self.table WHERE id=?''', (id,))

    def delete(self, id):
        self.cur.execute('''DELETE * FROM self.table WHERE id=?''', (id,))


class MothersDatabase(BaseModel):

    def __init__(self):
        super().__init__()
        self.table = db.mother  # todo add my table

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
     # self.cur.execute('''UPDATE Famalies
      # SET mail=?,firstname=?, lastname=?,city=?,neighborhood=?,
      # cell=?,num_of_children=?,oldest_children=?,youngest_children=? WHERE id, = ?'''
       # (mail, firstname, lastname, city, neighborhood, cell, num_of_children, oldest_children,
        #                  youngest_children, id))
        self.conn.commit()

    def delete_family12(self, id):
        self.cur.execute("DELETE FROM Famalies WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# mom = MothersDatabase()
# mom.table
