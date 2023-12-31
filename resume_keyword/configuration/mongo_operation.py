import sys
from json import loads
from typing import Collection
from pandas import DataFrame
from pymongo.database import Database
import pandas as pd
from pymongo import MongoClient
from resume_keyword.constants import DB_URL
from resume_keyword.exception import ResumeKeywordException
import logging

# initializing logger
logger = logging.getLogger(__name__)


class MongoDBOperation:
    def __init__(self):
        self.DB_URL = DB_URL
        self.client = MongoClient(self.DB_URL)

    def get_database(self, db_name) -> Database:

        """
        Method Name :   get_database
        
        Description :   This method gets database from MongoDB from the db_name
        
        Output      :   A database is created in MongoDB with name as db_name
        """
        logger.info("Entered get_database method of MongoDB_Operation class")

        try:
            # Getting the DB
            db = self.client[db_name]

            logger.info(f"Created {db_name} database in MongoDB")
            logger.info("Exited get_database method MongoDB_Operation class")
            return db

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    @staticmethod
    def get_collection(database, collection_name) -> Collection:

        """
        Method Name :   get_collection
        
        Description :   This method gets collection from the particular database and collection name
        
        Output      :   A collection is returned from database with name as collection name
        """
        logger.info("Entered get_collection method of MongoDB_Operation class")

        try:
            # Getting the collection name
            collection = database[collection_name]

            logger.info(f"Created {collection_name} collection in mongodb")
            logger.info("Exited get_collection method of MongoDB_Operation class ")
            return collection

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    def get_collection_as_dataframe(self, db_name, collection_name) -> DataFrame:

        """
        Method Name :   get_collection_as_dataframe
        
        Description :   This method is used for converting the selected collection to dataframe
        
        Output      :   A collection is returned from the selected db_name and collection_name
        """
        logger.info(
            "Entered get_collection_as_dataframe method of MongoDB_Operation class"
        )
        try:
            # Getting the database
            database = self.get_database(db_name)

            # Getting the colleciton name
            collection = database.get_collection(name=collection_name)

            # Reading the dataframe and dropping the _id column
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            logger.info("Converted collection to dataframe")
            logger.info(
                "Exited get_collection_as_dataframe method of MongoDB_Operation class"
            )
            return df

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    def insert_dataframe_as_record(self, data_frame, db_name, collection_name) -> None:
        """
        Method Name :   insert_dataframe_as_record
        
        Description :   This method inserts the dataframe as record in database collection
        
        Output      :   The dataframe is inserted in database collection
        """
        logger.info("Entered insert_dataframe_as_record method of MongoDB_Operation")

        try:
            # Converting dataframe into json
            records = loads(data_frame.T.to_json()).values()
            logger.info(f"Converted dataframe to json records")

            # Getting the database and collection
            database = self.get_database(db_name)
            collection = database.get_collection(collection_name)
            logger.info("Inserting records to MongoDB",)

            # Inserting data to MongoDB database
            collection.insert_many(records)
            logger.info("Inserted records to MongoDB")
            logger.info(
                "Exited the insert_dataframe_as_record method of MongoDB_Operation"
            )

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e
        

    def insert_dict_as_record(self, dictionary , db_name, collection_name) -> None:
        """
        Method Name :   insert_dict_as_record
        
        Description :   This method inserts the dictionary as record in database collection
        
        Output      :   The dictionary is inserted in database collection
        """
        logger.info("Entered insert_dict_as_record method of MongoDB_Operation")

        try:
            # Getting the database and collection
            database = self.get_database(db_name)
            collection = database.get_collection(collection_name)
            logger.info("Inserting records to MongoDB",)

            # Inserting data to MongoDB database
            collection.insert_many(dictionary)
            logger.info("Inserted records to MongoDB")
            logger.info(
                "Exited the insert_dict_as_record method of MongoDB_Operation"
            )

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e