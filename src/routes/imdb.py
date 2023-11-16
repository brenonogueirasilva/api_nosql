from fastapi import APIRouter, Query
from typing import List
import os

from src.classes.base_model import ModelFindImdb
from src.classes.mongo_db import MongoDb
from src.classes.base_model import ModelCreateImdb, ModelUpdateImdb, ModelFindImdb
from src.classes.integrate_api import IntegrateApi
from src.classes.secret_manager import SecretManager

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =  './src/apt-theme-402300-32506a51a70d.json'

colleciont_name = 'imdb'
project_id = "apt-theme-402300"
secret_id = "mongo_db"

router_imdb = APIRouter(prefix='/imdb')
secret = SecretManager()
mongo_credentials = secret.access_secret_json_file(project_id, secret_id)

mongo = MongoDb(
    host= mongo_credentials['host'],
    port= mongo_credentials['port'],
    user= mongo_credentials['user'],
    password=  mongo_credentials['password'],
    database=  mongo_credentials['database']
)
integrate_api = IntegrateApi()


@router_imdb.post('/select' , tags=["IMDB"], summary="Select IMDB" )
def select(
    params : ModelFindImdb,
    page: int = Query(1, description='Numero da pagina', ge=1), 
    page_size: int = Query(10, description='Quantidade itens por pagina', ge=5, le=100)):

    dict_params = integrate_api.params_to_dict(params)
    collection = mongo.find_many_pagination(colleciont_name, page= page, size=page_size, query=dict_params)
    count_documents = mongo.count_documents(colleciont_name, query=dict_params)

    response = {}
    response['items'] = collection
    response['total pages'] = (count_documents // page_size) + 1
    response['page'] = page 
    response['size'] = page_size
    return response

@router_imdb.post('/create', tags=["IMDB"], summary="Create IMDB" )
def create(ls_params : List[ModelCreateImdb]):
    ls_treat_params = integrate_api.list_params_to_dict(ls_params)
    inserted_documents = mongo.insert_documents(colleciont_name, ls_treat_params)
    return inserted_documents

@router_imdb.put('/' , tags=["IMDB"], summary="Update IMDB" )
def update(update_params : ModelUpdateImdb):
    treated_update_params = integrate_api.update_params_to_dict(update_params)
    updated_documents = mongo.update(
        colleciont_name, 
        new_document= treated_update_params['new_document'],
        query=treated_update_params['query']
        )
    return updated_documents

@router_imdb.delete('/' , tags=["IMDB"], summary="Delete IMDB" )
def delete(params : ModelFindImdb):

    dict_params = integrate_api.params_to_dict(params)
    deleted_documents = mongo.delete_documents(colleciont_name, query=dict_params)
    return deleted_documents