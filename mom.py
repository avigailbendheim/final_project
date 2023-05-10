import sqlite3

class Mothers:
    def __init__(self, id, mail, firstname, lastname, city, neighborhood, cell, num_of_children, oldest_children,
                      youngest_children):
        self.id = id
        self.mail = mail
        self.firstname = firstname
        self.lastname = lastname
        self.city= city
        self.neighborhood= neighborhood
        self.cell= cell
        self.num_of_children = num_of_children
        self.oldest_children = oldest_children
        self.youngest_children = youngest_children
    def load_all(self):
        pass






