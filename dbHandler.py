import sqlite3

class databaseHandler:
    def __init__(self):
        self.con = sqlite3.connect('database\data.db')
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, phone_number TEXT, question TEXT)")
        self.con.commit()
    
    def addUser(self, name: str, email: str, phone_number: str, question: str):
        self.cur.execute("INSERT INTO users (name, email, phone_number, question) VALUES (?, ?, ?, ?)", (name, email, phone_number, question))
        self.con.commit()

    def removeUser(self, id: int):
        self.cur.execute("DELETE FROM users WHERE id = ?", (id,))
        self.con.commit()

if __name__ == '__main__':
    db = databaseHandler()