import sqlite3

from sqlite3 import Error

def open_db():
    try:
        con = sqlite3.connect("links.db")
        return con
    except Error as e:
        print("Error:", e)

def run_query(sql:str='', params:str='', **kargs:dict):

    with open_db() as con:
        cursor = con.cursor()
        try:
            if kargs.get('script'):
                return cursor.executescript(kargs.get('script'))
            elif kargs.get('multiple'):
                return cursor.executemany(sql, params)
            return cursor.execute(sql, params)
        except Error as e:
            print("Error:", e)

def create_schema(script_sql):
    try:
        with open(script_sql, 'r') as sql_file:
            schema_created = run_query(script=sql_file.read())
            if schema_created.rowcount == -1:
                print("Database created successfully")

    except (FileNotFoundError, IOError) as e:
        print(f"File {script_sql} not found\n{e}")

if __name__ == "__main__":
    create_schema("schema.sql")