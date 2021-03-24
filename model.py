import sqlite3


db = 'animals.db'

def creation_db(db=db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS animals(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        animalname VARCHAR(255));
    """)
    conn.commit()


def add_to_db(data, db=db):
    conn = sqlite3.connect(db)
    conn.execute("INSERT INTO animals (animalname) VALUES (?);", (data,))
    conn.commit()
    conn.close()

def select_from_db(db=db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT animalname FROM animals")
    result = cursor.fetchall()
    conn.close()
    return result


