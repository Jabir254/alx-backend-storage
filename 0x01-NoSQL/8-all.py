#!/usr/bin/python3

'''List all documents'''

import pymongo


def list_all(mongo_collection):
    '''To list all docs'''

    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [post for post in docs]
