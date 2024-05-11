import crud

def init():
    # crud.get_data(True)
    crud.insert_data()
    crud.get_data(True)

if __name__ == "__main__":
    init()
