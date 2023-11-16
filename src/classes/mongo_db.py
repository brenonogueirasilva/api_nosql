import pymongo

class MongoDb:
    def __init__(self, host, port, user, password, database ):
        self.host = host 
        self.port = port 
        self.user = user 
        self.password = password
        self.database = database
        self.client = pymongo.MongoClient(f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/?authSource={self.database}&authMechanism=SCRAM-SHA-256")
        self.database = self.client[self.database]

    def list_database_names(self):
        return self.client.list_database_names()
    
    def list_collections(self):
        return self.database.list_collection_names()
    
    def find_one(self, collection, query = {}):
        collection = self.database[collection]
        return collection.find_one(query)

    def find_many(self, collection, query = {}):
        collection = self.database[collection]
        cursor = collection.find(query)
        ls_documents = []
        for document in cursor:
            ls_documents.append(document)
        return ls_documents
    
    def find_many_pagination(self, collection, page, size, query = {}):
        collection = self.database[collection]
        skip_value = (page -1 ) * size 
        cursor = collection.find(query).skip(skip_value).limit(size)
        ls_documents = []
        for document in cursor:
            ls_documents.append(document)
        return ls_documents
    
    def find_many_limit(self, collection, query = {}, limit = None):
        collection = self.database[collection]
        if limit is None:
            cursor = collection.find(query)
        else:
            cursor = collection.find(query).limit(limit)

        ls_documents = []
        for document in cursor:
            ls_documents.append(document)
        return ls_documents
    
    def count_documents(self, collection, query={}):
        collection = self.database[collection]
        return collection.count_documents(query)
    
    def insert_one_document(self, collection, document):
        collection = self.database[collection]
        collection.insert_one(document)
        return 'one documented inserted'

    def insert_documents(self, collection, ls_documents):
        collection = self.database[collection]
        insert_many = collection.insert_many(ls_documents)
        return f"Inserted Documents : {insert_many.inserted_ids}"

    def delete_one_document(self, collection, query = {}):
        collection = self.database[collection]
        collection.delete_one(query)
        return 'One Documented deleted'

    def delete_documents(self, collection, query = {}):
        collection = self.database[collection]
        deleted_documents = collection.delete_many(query).deleted_count
        return f"Deleted Documents : {deleted_documents}"
    
    def update_one(self, collection,  new_document, query = {}):
        collection = self.database[collection]
        new_document = {"$set" : new_document}
        collection.update_one(query, new_document)
        return 'One Document Updated'

    def update(self, collection,  new_document, query = {}):
        collection = self.database[collection]
        new_document = {"$set" : new_document}
        collection.update_many(query, new_document)
        return 'Documented Updateds'
    
    def drop_collection(self, collection):
        collection = self.database[collection]
        collection.drop()
        return 'Collection Dropped with Success'
    