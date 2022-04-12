import sqlite3 as sql
from sqlite3 import Error
from os import system


def insert_log(bd,log):
    conn = sql.connect(bd)
    pattern = conn.cursor()
    sqlInsert = f"INSERT INTO log(fecha, tipo_mensaje, archivo, linea) VALUES ('{log['datetime']}', '{log['type_message']}', '{log['filepath']}', {log['line']})"
    pattern.execute(sqlInsert)
    conn.commit()
    conn.close()


def create_bd(file_db):
    conn = None
    try:
        conn = sql.connect(file_db)
        create_table(file_db)
        print(sql.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_table(bd):
    conn = sql.connect(bd)
    try:
        conn.execute("create table log(fecha varchar not null, tipo_mensaje varchar not null, archivo varchar not null, linea varchar not null);")
        print("CREATED")
    except sql.OperationalError:
        print("TABLE ALREADY EXISTS")
    conn.close()


