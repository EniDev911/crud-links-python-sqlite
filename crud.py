import db
from prettytable import from_db_cursor # pip install prettytable

def get_data(category=False):
    query = ""
    if category:
        query += "SELECT link.name 'recurso', link.url, category.name as 'categoría' FROM link"
        query += " INNER JOIN category"
        query += " ON category.id = link.category_id"
        query += " GROUP BY link.name;"
    else:
        query += "SELECT * FROM link"

    result = db.run_query(query)
    mytable = from_db_cursor(result)
    mytable.align = "l"
    print(mytable)


def insert_data():
    query = "INSERT INTO link (name, url, category_id) VALUES (?, ?, ?)"
    name = input('Introduce el nombre para el nuevo recurso: ').strip()
    url = input('Introduce la url para el nuevo recurso: ').strip()
    category = int(input('Introduce la categoría a la que pertenece el nuevo recurso: '))
    result = db.run_query(query, (name, url, category))
    if result.rowcount == 1:
        print("Registro ingresado exitosamente en la tabla")

def update_data():
    pass