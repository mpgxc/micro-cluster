import sqlite3


DATABASE = "./database.db"


def insert_relats(sec, pal1, pal2, pal3):

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO relats (sec, pal1, pal2, pal3) VALUES('"+str(sec)+"', '" +
        str(pal1)+"', '"+str(pal2)+"', '"+str(pal3)+"');"
    )

    conn.commit()
    conn.close()
