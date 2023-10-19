#!/usr/bin/env python3
'''inserts a new document in a collection'''
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert a documents into a collection
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
