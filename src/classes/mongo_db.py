import pymongo

class MongoDb:
    """
    A class to interact with MongoDB, providing methods for various database operations.
    Attributes:
        host (str): The MongoDB server host.
        port (int): The MongoDB server port.
        user (str): The MongoDB user.
        password (str): The MongoDB user's password.
        database (str): The name of the MongoDB database.
    """
    def __init__(self, host: str, port: int, user: str, password: str, database: str ):
        self.host = host 
        self.port = port 
        self.user = user 
        self.password = password
        self.database = database
        self.client = pymongo.MongoClient(f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/?authSource={self.database}&authMechanism=SCRAM-SHA-256")
        self.database = self.client[self.database]

    def list_database_names(self) -> list:
        """
        Lists all the available database names.
        Returns:
            list: A list of database names.
        """
        return self.client.list_database_names()
    
    def list_collections(self) -> list:
        """
        Lists all the collections in the current database.
        Returns:
            list: A list of collection names.
        """
        return self.database.list_collection_names()
    
    def find_one(self, collection : str, query : dict = {}) -> dict or None:
        """
        Finds a single document in the specified collection based on the given query.
        Args:
            collection (str): The name of the collection.
            query (dict): The query to filter documents.
        Returns:
            dict or None: The found document or None if not found.
        """
        collection = self.database[collection]
        return collection.find_one(query)

    def find_many(self, collection : str, query : dict = {}) -> list:
        """
        Finds multiple documents in the specified collection based on the given query.
        Args:
            collection (str): The name of the collection.
            query (dict): The query to filter documents.
        Returns:
            list: A list of found documents.
        """
        collection = self.database[collection]
        cursor = collection.find(query)
        ls_documents = []
        for document in cursor:
            ls_documents.append(document)
        return ls_documents
    
    def find_many_pagination(self, collection : str, page: int, size: int, query : dict = {}) -> list:
        """
        Finds multiple documents with pagination in the specified collection based on the given query.
        Args:
            collection (str): The name of the collection.
            page (int): The page number for pagination.
            size (int): The number of documents per page.
            query (dict): The query to filter documents.
        Returns:
            list: A list of found documents for the specified page.
        """
        collection = self.database[collection]
        skip_value = (page -1 ) * size 
        cursor = collection.find(query).skip(skip_value).limit(size)
        ls_documents = []
        for document in cursor:
            ls_documents.append(document)
        return ls_documents
    
    def find_many_limit(self, collection: str, query: dict = {}, limit: int or None = None) -> list:
        """
        Finds multiple documents in the specified collection with an optional limit.
        Args:
            collection (str): The name of the collection.
            query (dict): The query to filter documents.
            limit (int or None): The maximum number of documents to return.
        Returns:
            list: A list of found documents.
        """
        collection = self.database[collection]
        if limit is None:
            cursor = collection.find(query)
        else:
            cursor = collection.find(query).limit(limit)

        ls_documents = []
        for document in cursor:
            ls_documents.append(document)
        return ls_documents
    
    def count_documents(self, collection: str, query: dict = {}) -> int:
        """
        Counts the number of documents in the specified collection based on the given query.
        Args:
            collection (str): The name of the collection.
            query (dict): The query to filter documents.
        Returns:
            int: The count of documents.
        """
        collection = self.database[collection]
        return collection.count_documents(query)
    
    def insert_one_document(self, collection: str, document: dict) -> str:
        """
        Inserts a single document into the specified collection.
        Args:
            collection (str): The name of the collection.
            document (dict): The document to be inserted.
        Returns:
            str: A success message.
        """
        collection = self.database[collection]
        collection.insert_one(document)
        return 'one documented inserted'

    def insert_documents(self, collection: str, ls_documents: list) -> str:
        """
        Inserts multiple documents into the specified collection.
        Args:
            collection (str): The name of the collection.
            ls_documents (list): The list of documents to be inserted.
        Returns:
            str: A success message with the count of inserted documents.
        """
        collection = self.database[collection]
        insert_many = collection.insert_many(ls_documents)
        return f"Inserted Documents : {insert_many.inserted_ids}"

    def delete_one_document(self, collection: str, query: dict = {}) -> str:
        """
        Deletes a single document from the specified collection based on the given query.
        Args:
            collection (str): The name of the collection.
            query (dict): The query to filter documents.
        Returns:
            str: A success message.
        """
        collection = self.database[collection]
        collection.delete_one(query)
        return 'One Documented deleted'

    def delete_documents(self, collection: str, query: dict = {}) -> str:
        """
        Deletes multiple documents from the specified collection based on the given query.
        Args:
            collection (str): The name of the collection.
            query (dict): The query to filter documents.
        Returns:
            str: A success message with the count of deleted documents.
        """
        collection = self.database[collection]
        deleted_documents = collection.delete_many(query).deleted_count
        return f"Deleted Documents : {deleted_documents}"
    
    def update_one(self, collection: str, new_document: dict, query: dict = {}) -> str:
        """
        Updates a single document in the specified collection based on the given query.
        Args:
            collection (str): The name of the collection.
            new_document (dict): The updated document.
            query (dict): The query to filter documents.
        Returns:
            str: A success message.
        """
        collection = self.database[collection]
        new_document = {"$set" : new_document}
        collection.update_one(query, new_document)
        return 'One Document Updated'

    def update(self, collection: str, new_document: dict, query: dict = {}) -> str:
        """
        Updates multiple documents in the specified collection based on the given query.
        Args:
            collection (str): The name of the collection.
            new_document (dict): The updated document.
            query (dict): The query to filter documents.
        Returns:
            str: A success message.
        """
        collection = self.database[collection]
        new_document = {"$set" : new_document}
        collection.update_many(query, new_document)
        return 'Documented Updateds'
    
    def drop_collection(self, collection: str) -> str:
        """
        Drops the specified collection.
        Args:
            collection (str): The name of the collection to be dropped.
        Returns:
            str: A success message.
        """
        collection = self.database[collection]
        collection.drop()
        return 'Collection Dropped with Success'
    