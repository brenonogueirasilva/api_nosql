from pydantic import BaseModel
from typing import Dict, List

class ModelFindImdb(BaseModel):
    """
    Pydantic model for querying IMDb data.
    Attributes:
        name (str): The name of the movie.
        year (Dict[str, int]): The year of the movie (query conditions).
        runtime (Dict[str, int]): The runtime of the movie (query conditions).
        genre (str): The genre of the movie.
        ratingValue (Dict[str, float]): The rating value of the movie (query conditions).
        ratingCount (Dict[str, int]): The rating count of the movie (query conditions).
        director (str): The director of the movie.
        cast (str): The cast of the movie.
    Config:
        schema_extra (Dict): Extra schema information for documentation.
    """
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
    """
    Pydantic model for creating IMDb data.
    Attributes:
        name (str): The name of the movie.
        year (int): The year of the movie.
        runtime (int): The runtime of the movie.
        genre (List[str]): The genres of the movie.
        ratingValue (float): The rating value of the movie.
        ratingCount (int): The rating count of the movie.
        director (List[dict]): The directors of the movie.
        cast (List[dict]): The cast of the movie.
    Config:
        schema_extra (Dict): Extra schema information for documentation.
    """
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
    """
    Pydantic model for updating IMDb data.
    Attributes:
        new_document (ModelFindImdb): The new data for the movie.
        query (ModelFindImdb): The query conditions for updating.
    Config:
        schema_extra (Dict): Extra schema information for documentation.
    """
    new_document : ModelFindImdb  
    query : ModelFindImdb