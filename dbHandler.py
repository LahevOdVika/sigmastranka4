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
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.con is not None:
            self.con.close()

    def addUser(self, name: str, email: str, phone_number: str, question: str):
        print(name, email, phone_number, question)
        if self.cur is not None:
            self.cur.execute("INSERT INTO users (name, email, phone_number, question) VALUES (?, ?, ?, ?)", (encrypt(name.encode('utf-8')), encrypt(email.encode('utf-8')), encrypt(phone_number.encode('utf-8')), encrypt(question.encode('utf-8'))))
            self.con.commit()

    def removeUser(self, id: int):
        if self.cur is not None:
            self.cur.execute("DELETE FROM users WHERE id = ?", (id,))

    def readData(self):
        if self.cur is not None:
            self.cur.execute("SELECT * FROM users")
            return [decrypt(i) for i in self.cur.fetchall()]
        else:
            return []

    def addPhoneModel(self, phone_generation: str, phone_variant: str, price: int, model_template: str):
        print(phone_generation, phone_variant, price)
        if self.cur is not None:
            self.cur.execute('INSERT INTO phone_models (phone_generation, price, model_template) VALUES (?, ?, ?)', (phone_generation, price, model_template))
            self.con.commit()

    def getPhoneModels(self):
        if self.cur is not None:
            self.cur.execute('SELECT * FROM phone_models ORDER BY phone_id DESC ')
            return self.cur.fetchall()
        else:
            return []

    def getOnePhone(self, phone_id: int):
        if self.cur is not None:
            self.cur.execute('SELECT * FROM phone_models WHERE phone_id = ?', (phone_id,))
            result = self.cur.fetchall()
            if result:
                return result[0]
            else:
                return None

    def getOnePhoneTemplate(self, phone_id: int):
        if self.cur is not None:
            self.cur.execute('SELECT model_template FROM phone_models WHERE phone_id = ?', (phone_id,))
            result = self.cur.fetchone()
            if result:
                return result[0]
            else:
                return None

    def checkPhoneExistence(self, phone_generation: str):
        if self.cur is not None:
            self.cur.execute('SELECT 1 FROM phone_models WHERE phone_generation = ?', (phone_generation,))
            return self.cur.fetchone() is not None
        else:
            return False


if __name__ == '__main__':
    with databaseHandler() as db:
        print(db.readData())
