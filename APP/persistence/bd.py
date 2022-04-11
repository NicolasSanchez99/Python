import sqlite3 as sql


def insert_log(log):
    conn = sql.connect("testingefrain.db")
    pattern = conn.cursor()
    sqlInsert = f"INSERT INTO log(fecha, tipo_mensaje, archivo, linea) VALUES ('{log['datetime']}', '{log['type_message']}', '{log['filepath']}', {log['line']})"
    pattern.execute(sqlInsert)
    conn.commit()
    conn.close()
