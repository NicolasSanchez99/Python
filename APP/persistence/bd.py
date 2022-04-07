import sqlite3 as sql

class persistence:

    def insert(fecha, tipo, url, linea):
        conn = sql.connect("auxiliar.db")
        pattern = conn.cursor()
        sqlInstruction = f"INSERT INTO log VALUES ('{fecha}', '{tipo}', '{url}', {linea}"
        pattern.execute(sqlInstruction)
        conn.commit()
        conn.close()

    def select(self):
        conn = sql.connect("auxiliar.db")
        pattern = conn.cursor()
        ins = "SELECT * FROM logs"
        pattern.execute(ins)
        data = pattern.fetchall()
        conn.commit()
        conn.close()
        print(data)






