import sqlite3

def create_gallons_table():
    try:
        connection = sqlite3.connect("data/warehouse.db")  # creates or connect to it
        cursor = connection.cursor()
        sql = """CREATE TABLE IF NOT EXISTS gallons(
            code INTEGER PRIMARY KEY AUTOINCREMENT, 
            size INTEGER, 
            description TEXT)"""
        cursor.execute(sql)
        print("Table created!")

    except Exception as erro:
        print("Table creation fail: " + str(erro))

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    create_gallons_table()