import zerorpc
import sqlite3


DATABASE = "./database.db"


def connectNodes():

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cursor = cur.execute('select * from users;')
    count = 0
    for line in cursor:
        print("=====================\n", line, "\n====================\n")

        Connect = zerorpc.Client()
        Connect.connect("tcp://"+line[2]+":56789")
        Connect.start(str(line[1]).split("-")[1])
        count += 1

    conn.close()
    print("Conectando Nodes!")
    return count