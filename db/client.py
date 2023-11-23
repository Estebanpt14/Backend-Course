from pymongo import MongoClient
from db.models.user import User
from db.schemas.user_db import *
from bson.objectid import ObjectId

db_client = MongoClient()

schema = db_client.local.users


def get_all_users():
    return users_schema(schema.find())


def insert_user(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    return schema.insert_one(user_dict).inserted_id


def find_user(id_user: str):
    user = schema.find_one({"_id": ObjectId(id_user)})
    if user is not None:
        return User(**user_schema(user))
    else:
        return user


def find_user_name(name: str):
    user = schema.find_one({"name": name})
    if user is not None:
        return User(**user_schema(user))
    else:
        return user


def delete_user(id_user: str):
    user = schema.find_one_and_delete({"_id": ObjectId(id_user)})
    return user


def replace_user(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    user_replaced = schema.find_one_and_replace(
        {"_id": ObjectId(user.id)}, user_dict)
    return user_replaced
