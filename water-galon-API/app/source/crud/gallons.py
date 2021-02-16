import sqlite3
from typing import Generator
from sqlalchemy.orm import Session

from source.dependencies import DATABASE_PATH
from source.models.gallons import Gallons_Model

async def insert_gallon(data, db: Session):
    db_gallon = Gallons_Model(**data.dict())
    db.add(db_gallon)
    db.commit()
    db.refresh(db_gallon)
    return db_gallon

def retrieve_all_galllons(db: Session)-> Generator:   
    return db.query(Gallons_Model).all()

def retrieve_gallon(code: int, db: Session):
    return db.query(Gallons_Model).filter(
        Gallons_Model.code == code
    ).first()
    
def remove_gallon(code: int, db: Session) -> bool:
    gallon = retrieve_gallon(code, db)
    db.delete(gallon)
    db.commit()