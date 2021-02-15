from typing import Optional

from pydantic import BaseModel

class GallonBase(BaseModel):
    size: int = None
    description: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "size": 500,
                "description": "medium size bottle",
            }
        }

class GallonUpdate(GallonBase):
    code: int = None
    
    class Config:
        schema_extra = {
            "example": {
                "code": 999,
                "size": 150,
                "description": "very small size bottle",
            }
        }