from peewee import SqliteDatabase,Model, AutoField, TextField, CharField
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


#
# animals = SqliteDatabase('animals.db')
#
# class BaseModel(Model):
#     class Meta:
#         database = animals
#
# class Animals(BaseModel):
#     artist_id = AutoField(column_name='animal_id')
#     name = TextField(column_name='Name', null=True)
#     letter = CharField(max_length=1)
#
#     class Meta:
#         table_name = 'Animals'
#
# cursor = animals.cursor()
#
# animals.close()