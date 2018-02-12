# populatedb.py

from constants import Const

from bson.json_util import loads
from os.path import isfile
from pymongo import MongoClient
from sys import exit

def get_songs_collection():
    return MongoClient()[Const.SONGS_DB][Const.SONGS_COLLECTION]

def load_songs():
    if not isfile(Const.SONGS_FILE):
        print("File {} not found.".format(Const.SONGS_FILE))
        exit()
    songs = []
    with open(Const.SONGS_FILE) as file:
        for line in file:
            songs.append(loads(line.rstrip('\n')))
    return songs

def main():
    print("Loading contents of file '{}' into 'MongoDB.{}.{}'..."
        .format(Const.SONGS_FILE, Const.SONGS_DB, Const.SONGS_COLLECTION))
    get_songs_collection().drop()
    get_songs_collection().insert_many(load_songs())

if __name__ == "__main__":
    main()
