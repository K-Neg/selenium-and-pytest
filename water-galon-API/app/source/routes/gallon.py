from fastapi import APIRouter, Depends
from source.schemas.gallon import GallonBase, GallonUpdate
from source.crud.gallons import insert_gallon, retrieve_all_galllons
from source.database.database import SessionLocal, engine
from sqlalchemy.orm import Session

gallon_routes = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@gallon_routes.get("/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gallons = retrieve_all_galllons(db=db, skip=skip, limit=limit)
    return gallons


@gallon_routes.get("/{code}")
async def get_one(code: int):
    return 1

@gallon_routes.post("/")
async def create_gallon(gallon: GallonBase, db: Session = Depends(get_db)):
    x = await insert_gallon(data=gallon,db=db)
    return x

@gallon_routes.put("/{code}")
async def update_gallon(code: int, gallon: GallonUpdate):
    return gallon

@gallon_routes.delete("/{code}")
async def delete_gallon(code: int):
    pass
