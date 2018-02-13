# populatedb.py

from constants import Const

from bson.json_util import loads
from os.path import isfile
from pymongo import MongoClient
from sys import exit


def get_songs_db():
    return MongoClient()[Const.SONGS_DB]


def get_songs_collection():
    return get_songs_db()[Const.SONGS_COLLECTION]


def get_ratings_collection():
    return get_songs_db()[Const.RATINGS_COLLECTION]


def load_songs():
    if not isfile(Const.SONGS_FILE):
        print("File {} not found.".format(Const.SONGS_FILE))
        exit()
    songs = []
    with open(Const.SONGS_FILE) as file:
        for line in file:
            songs.append(loads(line.rstrip('\n')))
    return songs


def clean_up_collection(collection, name):
    print("Cleaning up 'MongoDB.{}.{}'...".format(Const.SONGS_DB, name))
    collection.drop()


def main():
    clean_up_collection(get_ratings_collection(), Const.RATINGS_COLLECTION)
    clean_up_collection(get_songs_collection(), Const.SONGS_COLLECTION)
    print("Populating 'MongoDB.{}.{}' with items from file {}..."
        .format(Const.SONGS_DB, Const.SONGS_COLLECTION, Const.SONGS_FILE))
    get_songs_collection().insert_many(load_songs())
    print("Done!")


if __name__ == "__main__":
    main()
