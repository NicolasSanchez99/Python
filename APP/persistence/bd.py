import sqlite3 as sql


def insert(fecha, tipo, url, linea):
    conn = sql.connect("testing.db")
    pattern = conn.cursor()
    sqlInstruction = f"INSERT INTO log VALUES ('{fecha}', '{tipo}', '{url}', {linea}"
    pattern.execute(sqlInstruction)
    conn.commit()
    conn.close()

def select():
    conn = sql.connect("testing.db")
    pattern = conn.cursor()
    ins = " select * from log"
    pattern.execute(ins)
    data = pattern.fetchall()
    for d in data:
        print(d)
    conn.commit()
    conn.close()
    print(data)








