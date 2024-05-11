import json

def show_main_menu():
    try:
        with open("datos.json", "r", encoding='utf-8') as f_json:
            data = json.load(f_json)

            print(*data['menus']['principal'], sep="\n")
    except (FileNotFoundError, IOError) as e:
        print(f"Archivo {e.filename} no encontrado")