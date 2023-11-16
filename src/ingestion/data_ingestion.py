import pandas as pd 
import os
from fastapi import APIRouter


from src.classes.mongo_db import MongoDb
from src.classes.secret_manager import SecretManager

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =  './src/apt-theme-402300-32506a51a70d.json'

colleciont_name = 'imdb'
project_id = "apt-theme-402300"
secret_id = "mongo_db"

secret = SecretManager()
mongo_credentials = secret.access_secret_json_file(project_id, secret_id)
mongo = MongoDb(
    host= mongo_credentials['host'],
    port= mongo_credentials['port'],
    user= mongo_credentials['user'],
    password=  mongo_credentials['password'],
    database=  mongo_credentials['database']
)

file_path = './src/ingestion/'
list_files = os.listdir(file_path)
list_files = list(filter(lambda file: 'json' in file, list_files))
ls_dfs = []
for file in list_files:
    complete_path = file_path + file 
    with open(complete_path, 'r') as arquivo:
        df = pd.read_json(complete_path)
        ls_dfs.append(df)

df_contenate = pd.concat(ls_dfs)

def str_to_number(string):
    number = ''.join(list(filter(lambda letter : letter.isnumeric() or '.' == letter, string)))
    if number == '':
        return None 
    else:
        return int(number)
df['year'] = df['year'].apply(str_to_number)
df['runtime'] = df['runtime'].apply(str_to_number)
df = df.astype({'year' : 'int', 'runtime' : 'float'})
df['runtime'] = df['runtime'].fillna(0)
json_data = df.to_dict(orient='records')


router_ingestion = APIRouter(prefix='/ingestion')

@router_ingestion.post('/select' , tags=["Ingestion"], summary="Insert files to MongoDB to Test API" )
def data_ingestion():
    try:
        mongo.insert_documents('imdb', json_data)
        return({'info' :'Data Ingestion done with sucess'})
    except:
        return({'info' : 'Data Already in DataBase' } )