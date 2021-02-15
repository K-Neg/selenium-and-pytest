import sqlite3

from source.dependencies import DATABASE_PATH
from source.models.gallons import Gallons_Model

from sqlalchemy.orm import Session

async def insert_gallon(data, db: Session):
    
    db_gallon = Gallons_Model(**data.dict())
    db.add(db_gallon)
    db.commit()
    db.refresh(db_gallon)
    return db_gallon

async def retrieve_all_galllons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Gallons_Model).offset(skip).limit(limit).all()

async def insert_gallon_old(data):
    
    print(data)

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    try:
        sql = "insert into gallons(size, description) values(?,?)"
        cursor.execute(sql, data)
        connection.commit()
        state = True
        new_id = cursor.lastrowid
    except Exception as error:
        print("ErrorInsert", error)
        state = False
        new_id = ""
    finally:
        cursor.close()
        connection.close()
    return new_id, state
    
"""
async def retrieve_all_galllons():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    try:
        sql = "select * from customer order by name desc"
        cursor.execute(sql)
        customer_list = cursor.fetchall()
        state = True
    except Exception as error:
        print("ErrorListing" + str(error))
        state = False
    finally:
        cursor.close()
        connection.close()

    return customer_list, state


async def retrieve_single_customer(user_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    try:
        sql = "select * from customer where user_id = ?"
        cursor.execute(sql, [user_id])
        customer = cursor.fetchone()
        if customer is None:
            state = False
        else:
            state = True
    except Exception as error:
        state = False
        print("ErrorRetrievingCustomer" + str(error))
    finally:
        cursor.close()
        connection.close()
    return state, customer


async def update_customer(data, user_id):
    print(type(data))
    parsed_data = [str(data.name), int(data.age), str(data.avatar)]
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    try:
        sql = "UPDATE customer SET name = ?, age = ?, avatar = ? WHERE user_id = {idf}".format(
            idf=str(user_id)
        )

        cursor.execute(sql, parsed_data)
        connection.commit()
        state = True
    except Exception as error:
        print("ErrorUpdating" + str(error))
        state = False
    finally:
        cursor.close()
        connection.close()
    return state


async def update_avatar(avatar, user_id):
    parsed_data = str(avatar)
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    try:
        sql = "UPDATE customer SET avatar = ? WHERE user_id = {idf}".format(
            idf=str(user_id)
        )
        cursor.execute(sql, parsed_data)
        connection.commit()
        state = True
    except Exception as error:
        print("ErrorUpdatingAvatar" + str(error))
        state = False
    finally:
        cursor.close()
        connection.close()
    return state


async def delete_customer(user_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    try:
        sql = "DELETE FROM customer WHERE user_id = ?"
        cursor.execute(sql, str(user_id))
        connection.commit()
        if cursor.rowcount > 0:
            deleted = True
        else:
            deleted = False
    except Exception as error:
        print("ErrorDelete", error)
        deleted = False
    finally:
        cursor.close()
        connection.close()

    return deleted
"""