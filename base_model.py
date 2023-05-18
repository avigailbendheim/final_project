
import sqlite3

DB = "BabysitterDB.db"


class BaseModel:
    _cur = None

    def cur(self):
        if BaseModel._cur is None:
            BaseModel._cur = self.conn.cursor()
        return BaseModel._cur

    def __init__(self):
        if BaseModel._cur is not None:
            raise Exception("You already have cur")
        else:
            self.conn = sqlite3.connect(DB)
            self._cur = self.conn.cursor()
        self.table = None

    def create(self, data_dic):
        columns = ', '.join(data_dic.keys())
        values = ', '.join(["'{}'".format(v) for v in data_dic.values()])
        query = "INSERT INTO {} ({}) VALUES ({})".format(self.table, columns, values)
        self.cur().execute(query)
        self.conn.commit()

    def read(self, id):
        self.cur().execute('''SELECT * FROM {} WHERE id=?'''.format(self.table), (id,))
        result = self.cur().fetchone()
        return result

    def read_all(self):
        self.cur().execute('''SELECT * FROM {}'''.format(self.table))
        rows = self.cur.fetchall()
        return rows

    def update(self, id, data_dic):
        columns_values = ', '.join(["{}='{}'".format(k, v) for k, v in data_dic.items()])
        query = "UPDATE {} SET {} WHERE id=?".format(self.table, columns_values)
        self.cur().execute(query, (id,))
        self.conn.commit()

    def delete(self, id):
        self.cur().execute('''DELETE FROM {} WHERE id=?'''.format(self.table), (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


class FamiliesDatabase(BaseModel):
    def __init__(self):
        super().__init__()
        self.table = "Famalies"


class BabysitterDatabase(BaseModel):
    def __init__(self):
        super().__init__()
        self.table = "Babysitters"
