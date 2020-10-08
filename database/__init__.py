import pymongo
from env import mongo_user, mongo_pass, mongo_url, db_name

def database():
    """Created Database connection"""
    client = pymongo.MongoClient(
        mongo_url,
        username=mongo_user,
        password=mongo_pass
    )
    db = client[db_name]
    return db