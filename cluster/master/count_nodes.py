import sqlite3

DATABASE = "./database.db"

# retorna a quantidade de nodes direto do SQLite


def make_count():

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cursor = cur.execute('select * from users;')

    return len(cursor.fetchall())