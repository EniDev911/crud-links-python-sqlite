import crud
import menu
import time
import os, sys

# crud.get_data(True)
# crud.insert_data()
# crud.get_data(True)

def init():
    clear = 'cls' if sys.platform == 'win32' else 'clear'
    while True:
        os.system(clear)
        menu.show_main_menu()
        opcion = input("> ")

        if opcion == '1':
            os.system(clear)

        elif opcion == '2':
            os.system(clear)

        elif opcion == '3':
            os.system(clear)

        elif opcion == '4':
            os.system(clear)

        elif opcion == '5':
            os.system(clear)

        elif opcion == '0':
            os.system(clear)
            crud.get_data(True)

            time.sleep(5)

        elif opcion.lower() == 's':
            os.system(clear)
            print("Saliendo..Gracias por usar mi programa")
            time.sleep(3)
            exit()
            
        else:
            os.system(clear)
            print("Opción no válida")
            time.sleep(1)

if __name__ == "__main__":
    init()
