from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from source.database.database import Base

class Gallons_Model(Base):
    __tablename__ = "gallons"

    code = Column(Integer, primary_key=True, index=True)
    size = Column(Integer)
    description = Column(String)
    