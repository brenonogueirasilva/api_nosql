from pydantic import BaseModel
from typing import Dict, List

class ModelFindImdb(BaseModel):
    name : str = None 
    year : Dict[str , int] = None
    runtime : Dict[str, int] = None 
    genre : str = None 
    ratingValue : Dict[str, float] = None 
    ratingCount : Dict[str, int] = None 
    director : str = None 
    cast : str = None
    class Config:
        schema_extra = {
            "example": {
                "name": "The Way to Dusty Death",
                "year": {"$eq" : 1995},
                "runtime":  {"$lt" : 113},
                "genre":  "Action",
                "ratingValue":  {"$lt" : 3.9},
                "ratingCount": {"$lt" : 174},
                "director": "Geoffrey Reeve",
                "cast":  "Linda Hamilton"
            }
        }

class ModelCreateImdb(BaseModel):
    name : str = None 
    year : int = None
    runtime : int = None 
    genre : List[str] = None 
    ratingValue : float = None 
    ratingCount : int = None 
    director : List[dict] = None 
    cast : List[dict] = None
    class Config:
        schema_extra = {
            "example": {
                "name": "The Way to Dusty Death",
                "year": 1995,
                "runtime":  113,
                "genre": ["Action", "Adventure"],
                "ratingValue":  3.9,
                "ratingCount": 174,
                "director": [{ "name" : "Geoffrey Reeve"}] ,
                "cast":  [{ "name" : "Linda Hamilton"}]
            }
        }

class ModelUpdateImdb(BaseModel):
    new_document : ModelFindImdb  
    query : ModelFindImdb