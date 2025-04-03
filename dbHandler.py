import sqlite3
from encrypt import encrypt, decrypt
from contextlib import contextmanager

@contextmanager
def get_db():
    con = sqlite3.connect('misc_files\data.db')
    cur = con.cursor()
    try:
        yield cur
    finally:
        con.commit()
        con.close()

class databaseHandler:
    def __init__(self):
        self.cur = None
        self.con = None

    def __enter__(self):
        self.con = sqlite3.connect('misc_files\data.db')
        self.cur = self.con.cursor()
        self.con.commit()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, phone_number TEXT, question TEXT)")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.con is not None:
            self.con.close()

    def addUser(self, name: str, email: str, phone_number: str, question: str):
        if self.cur is not None:
            self.cur.execute("INSERT INTO users (name, email, phone_number, question) VALUES (?, ?, ?, ?)", (encrypt(name.encode('utf-8')), encrypt(email.encode('utf-8')), encrypt(phone_number.encode('utf-8')), encrypt(question.encode('utf-8'))))

    def removeUser(self, id: int):
        if self.cur is not None:
            self.cur.execute("DELETE FROM users WHERE id = ?", (id,))

    def readData(self):
        if self.cur is not None:
            self.cur.execute("SELECT * FROM users")
            return [decrypt(i) for i in self.cur.fetchall()]
        else:
            return []

if __name__ == '__main__':
    with databaseHandler() as db:
        db.addUser("test", "test", "test", "test")
        print(db.readData())
