import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)", (part, customer, retailer, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id=?", (part, customer, retailer, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database("Store.db")
#db.insert("4GB DDR4 Ram", "John Dog", "Microcenter", "160")
# db.insert("Asus Mobo", "Steve R", "Riofae", "360")
# db.insert("500w PSU", "Caroline w.", "Riofae", "500")
# db.insert("2GB DDR4", "Ebby w", "Apple", "60")
# db.insert("24 inch samsung monitor", "R. Wanjiku", "Samsung", "180")
# db.insert("PS4", "Sharon", "Riofae", "160")
# db.insert("Gionee X9", "Brenda", "Riofae", "550")